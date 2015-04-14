#!/usr/bin/env python
"""Unit tests for phonenumbermatcher.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/PhoneNumberMatchTest.java
#     java/test/com/google/i18n/phonenumbers/PhoneNumberMatcherTest.java
# Copyright (C) 2011 The Libphonenumber Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import unittest

from phonenumbers import PhoneNumberMatch, PhoneNumberMatcher, Leniency
from phonenumbers import PhoneNumber, NumberFormat, phonenumberutil
from phonenumbers import phonenumbermatcher, CountryCodeSource
from phonenumbers.util import u
from .testmetadatatest import TestMetadataTestCase


class PhoneNumberMatchTest(unittest.TestCase):
    """Tests the value type semantics for PhoneNumberMatch.

    Equality must be based on the covered range and corresponding phone
    number. Range and number correctness are tested by PhoneNumberMatcherTest.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValueTypeSemantics(self):
        number = PhoneNumber()
        match1 = PhoneNumberMatch(10, "1 800 234 45 67", number)
        match2 = PhoneNumberMatch(10, "1 800 234 45 67", number)
        match3 = PhoneNumberMatch(10, "1 801 234 45 67", number)

        self.assertEqual(match1, match2)
        self.assertEqual(match1.start, match2.start)
        self.assertEqual(match1.end, match2.end)
        self.assertEqual(match1.number, match2.number)
        self.assertEqual(match1.raw_string, match2.raw_string)
        self.assertEqual("1 800 234 45 67", match1.raw_string)
        # Python-specific: check __ne__()
        self.assertNotEqual(match1, match3)
        self.assertTrue(match1 != match3)
        # Python-specific: Check only comparisons of the same type work
        self.assertNotEqual(match1, None)
        self.assertNotEqual(match1, "")
        self.assertNotEqual(match1, "1 800 234 45 67")
        self.assertNotEqual(match1, 0)

    def testIllegalArguments(self):
        """Tests the value type semantics for matches with a None number."""
        try:
            PhoneNumberMatch(-110, "1 800 234 45 67", PhoneNumber())
            self.fail("Expected failed constructor")
        except Exception:
            pass

        try:
            PhoneNumberMatch(10, "1 800 234 45 67", None)
            self.fail("Expected failed constructor")
        except Exception:
            pass

        try:
            PhoneNumberMatch(10, None, PhoneNumber())
            self.fail("Expected failed constructor")
        except Exception:
            pass

        try:
            PhoneNumberMatch(10, None, None)
            self.fail("Expected failed constructor")
        except Exception:
            pass

    def testStringConvert(self):
        """Check string conversion"""
        number = PhoneNumber()
        match = PhoneNumberMatch(10, "1 800 234 45 67", number)

        self.assertEqual("PhoneNumberMatch [10,25) 1 800 234 45 67", str(match))
        # Python version extra test
        self.assertEqual("PhoneNumberMatch(start=10, raw_string='1 800 234 45 67', "
                         "numobj=PhoneNumber(country_code=None, national_number=None, extension=None, "
                         "italian_leading_zero=None, number_of_leading_zeros=None, "
                         "country_code_source=None, preferred_domestic_carrier_code=None))", repr(match))


class NumberContext(object):
    """Small class that holds the context of the number we are testing
    against. The test will insert the phone number to be found between
    leadingText and trailingText."""
    def __init__(self, leadingText, trailingText):
        self.leadingText = leadingText
        self.trailingText = trailingText


class NumberTest(object):
    """Small class that holds the number we want to test and the region for
    which it should be valid."""
    def __init__(self, rawString, region):
        self.rawString = rawString
        self.region = region

    def __str__(self):
        return "%s (%s)" % (self.rawString, self.region)


# Strings with number-like things that shouldn't be found under any level.
IMPOSSIBLE_CASES = [NumberTest("12345", "US"),
                    NumberTest("23456789", "US"),
                    NumberTest("234567890112", "US"),
                    NumberTest("650+253+1234", "US"),
                    NumberTest("3/10/1984", "CA"),
                    NumberTest("03/27/2011", "US"),
                    NumberTest("31/8/2011", "US"),
                    NumberTest("1/12/2011", "US"),
                    NumberTest("10/12/82", "DE"),
                    NumberTest("650x2531234", "US"),
                    NumberTest("2012-01-02 08:00", "US"),
                    NumberTest("2012/01/02 08:00", "US"),
                    NumberTest("20120102 08:00", "US"),
                    NumberTest("2014-04-12 04:04 PM", "US"),
                    NumberTest("2014-04-12 &nbsp;04:04 PM", "US"),
                    NumberTest("2014-04-12 &nbsp;04:04 PM", "US"),
                    NumberTest("2014-04-12  04:04 PM", "US"),
                    ]

# Strings with number-like things that should only be found under "possible".
POSSIBLE_ONLY_CASES = [NumberTest("7121115678", "US"),  # US numbers cannot start with 7 in the test metadata to be valid.
                       # 'X' should not be found in numbers at leniencies stricter than POSSIBLE, unless it represents
                       # a carrier code or extension.
                       NumberTest("1650 x 253 - 1234", "US"),
                       NumberTest("650 x 253 - 1234", "US"),
                       NumberTest("6502531x234", "US"),
                       NumberTest("(20) 3346 1234", "GB"),  # Non-optional NP omitted
                       ]

# Strings with number-like things that should only be found up to and
# including the "valid" leniency level.
VALID_CASES = [NumberTest("65 02 53 00 00", "US"),
               NumberTest("6502 538365", "US"),
               NumberTest("650//253-1234", "US"),  # 2 slashes are illegal at higher levels
               NumberTest("650/253/1234", "US"),
               NumberTest("9002309. 158", "US"),
               NumberTest("12 7/8 - 14 12/34 - 5", "US"),
               NumberTest("12.1 - 23.71 - 23.45", "US"),
               NumberTest("800 234 1 111x1111", "US"),
               NumberTest("1979-2011 100", "US"),
               NumberTest("+494949-4-94", "DE"),  # National number in wrong format
               NumberTest(u("\uFF14\uFF11\uFF15\uFF16\uFF16\uFF16\uFF16-\uFF17\uFF17\uFF17"), "US"),
               NumberTest("2012-0102 08", "US"),  # Very strange formatting.
               NumberTest("2012-01-02 08", "US"),
               # Breakdown assistance number with unexpected formatting.
               NumberTest("1800-1-0-10 22", "AU"),
               NumberTest("030-3-2 23 12 34", "DE"),
               NumberTest("03 0 -3 2 23 12 34", "DE"),
               NumberTest("(0)3 0 -3 2 23 12 34", "DE"),
               NumberTest("0 3 0 -3 2 23 12 34", "DE"),
               ]

# Strings with number-like things that should only be found up to and
# including the "strict_grouping" leniency level.
STRICT_GROUPING_CASES = [NumberTest("(415) 6667777", "US"),
                         NumberTest("415-6667777", "US"),
                         # Should be found by strict grouping but not exact
                         # grouping, as the last two groups are formatted
                         # together as a block.
                         NumberTest("0800-2491234", "DE"),
                         # Doesn't match any formatting in the test file, but
                         # almost matches an alternate format (the last two
                         # groups have been squashed together here).
                         NumberTest("0900-1 123123", "DE"),
                         NumberTest("(0)900-1 123123", "DE"),
                         NumberTest("0 900-1 123123", "DE"),
                         # NDC also found as part of the country calling code;
                         # this shouldn't ruin the grouping expectations.
                         NumberTest("+33 3 34 2312", "FR"),
                         ]

# Strings with number-like things that should be found at all levels.
EXACT_GROUPING_CASES = [NumberTest(u("\uFF14\uFF11\uFF15\uFF16\uFF16\uFF16\uFF17\uFF17\uFF17\uFF17"), "US"),
                        NumberTest(u("\uFF14\uFF11\uFF15-\uFF16\uFF16\uFF16-\uFF17\uFF17\uFF17\uFF17"), "US"),
                        NumberTest("4156667777", "US"),
                        NumberTest("4156667777 x 123", "US"),
                        NumberTest("415-666-7777", "US"),
                        NumberTest("415/666-7777", "US"),
                        NumberTest("415-666-7777 ext. 503", "US"),
                        NumberTest("1 415 666 7777 x 123", "US"),
                        NumberTest("+1 415-666-7777", "US"),
                        NumberTest("+494949 49", "DE"),
                        NumberTest("+49-49-34", "DE"),
                        NumberTest("+49-4931-49", "DE"),
                        NumberTest("04931-49", "DE"),  # With National Prefix
                        NumberTest("+49-494949", "DE"),  # One group with country code
                        NumberTest("+49-494949 ext. 49", "DE"),
                        NumberTest("+49494949 ext. 49", "DE"),
                        NumberTest("0494949", "DE"),
                        NumberTest("0494949 ext. 49", "DE"),
                        NumberTest("01 (33) 3461 2234", "MX"),  # Optional NP present
                        NumberTest("(33) 3461 2234", "MX"),  # Optional NP omitted
                        NumberTest("1800-10-10 22", "AU"),  # Breakdown assistance number.
                        # Doesn't match any formatting in the test file, but
                        # matches an alternate format exactly.
                        NumberTest("0900-1 123 123", "DE"),
                        NumberTest("(0)900-1 123 123", "DE"),
                        NumberTest("0 900-1 123 123", "DE"),
                        NumberTest("+33 3 34 23 12", "FR"),
                        ]


class PhoneNumberMatcherTest(TestMetadataTestCase):
    """Tests for PhoneNumberMatcher.

    This only tests basic functionality based on test metadata.  See
    testphonenumberutil.py for the origin of the test data.
    """
    def testContainsMoreThanOneSlashInNationalNumber(self):
        # A date should return true.
        number = PhoneNumber(country_code=1,
                             country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY)
        candidate = "1/05/2013"
        self.assertTrue(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        # Here, the country code source thinks it started with a country calling code, but this is not
        # the same as the part before the slash, so it's still true.
        number = PhoneNumber(country_code=274,
                             country_code_source=CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN)
        candidate = "27/4/2013"
        self.assertTrue(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        # Now it should be false, because the first slash is after the country calling code.
        number = PhoneNumber(country_code=49,
                             country_code_source=CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN)
        candidate = "49/69/2013"
        self.assertFalse(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        number = PhoneNumber(country_code=49,
                             country_code_source=CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN)
        candidate = "+49/69/2013"
        self.assertFalse(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        candidate = "+ 49/69/2013"
        self.assertFalse(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        candidate = "+ 49/69/20/13"
        self.assertTrue(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

        # Here, the first group is not assumed to be the country calling code, even though it is the
        # same as it, so this should return true.
        number = PhoneNumber(country_code=49,
                             country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY)
        candidate = "49/69/2013"
        self.assertTrue(phonenumbermatcher._contains_more_than_one_slash_in_national_number(number, candidate))

    # See PhoneNumberUtilTest.testParseNationalNumber().
    def testFindNationalNumber(self):
        # same cases as in testParseNationalNumber
        self.doTestFindInContext("033316005", "NZ")
        # self.doTestFindInContext("33316005", "NZ") is omitted since the
        # national prefix is obligatory for these types of numbers in New Zealand.
        # National prefix attached and some formatting present.
        self.doTestFindInContext("03-331 6005", "NZ")
        self.doTestFindInContext("03 331 6005", "NZ")
        # Testing international prefixes.
        # Should strip country code.
        self.doTestFindInContext("0064 3 331 6005", "NZ")
        # Try again, but this time we have an international number with Region
        # Code US. It should recognize the country code and parse accordingly.
        self.doTestFindInContext("01164 3 331 6005", "US")
        self.doTestFindInContext("+64 3 331 6005", "US")

        self.doTestFindInContext("64(0)64123456", "NZ")
        # Check that using a "/" is fine in a phone number.
        # Note that real Polish numbers do *not* start with a 0.
        self.doTestFindInContext("0123/456789", "PL")
        self.doTestFindInContext("123-456-7890", "US")

    # See PhoneNumberUtilTest.testParseWithInternationalPrefixes().
    def testFindWithInternationalPrefixes(self):
        self.doTestFindInContext("+1 (650) 333-6000", "NZ")
        self.doTestFindInContext("1-650-333-6000", "US")
        # Calling the US number from Singapore by using different service
        # providers
        # 1st test: calling using SingTel IDD service (IDD is 001)
        self.doTestFindInContext("0011-650-333-6000", "SG")
        # 2nd test: calling using StarHub IDD service (IDD is 008)
        self.doTestFindInContext("0081-650-333-6000", "SG")
        # 3rd test: calling using SingTel V019 service (IDD is 019)
        self.doTestFindInContext("0191-650-333-6000", "SG")
        # Calling the US number from Poland
        self.doTestFindInContext("0~01-650-333-6000", "PL")
        # Using "++" at the start.
        self.doTestFindInContext("++1 (650) 333-6000", "PL")
        # Using a full-width plus sign.
        self.doTestFindInContext(u("\uFF0B1 (650) 333-6000"), "SG")
        # The whole number, including punctuation, is here represented in
        # full-width form.
        self.doTestFindInContext(u("\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09") +
                                 u("\u3000\uFF13\uFF13\uFF13\uFF0D\uFF16\uFF10\uFF10\uFF10"),
                                 "SG")

    # See PhoneNumberUtilTest.testParseWithLeadingZero().
    def testFindWithLeadingZero(self):
        self.doTestFindInContext("+39 02-36618 300", "NZ")
        self.doTestFindInContext("02-36618 300", "IT")
        self.doTestFindInContext("312 345 678", "IT")

    # See PhoneNumberUtilTest.testParseNationalNumberArgentina().
    def testFindNationalNumberArgentina(self):
        # Test parsing mobile numbers of Argentina.
        self.doTestFindInContext("+54 9 343 555 1212", "AR")
        self.doTestFindInContext("0343 15 555 1212", "AR")

        self.doTestFindInContext("+54 9 3715 65 4320", "AR")
        self.doTestFindInContext("03715 15 65 4320", "AR")

        # Test parsing fixed-line numbers of Argentina.
        self.doTestFindInContext("+54 11 3797 0000", "AR")
        self.doTestFindInContext("011 3797 0000", "AR")

        self.doTestFindInContext("+54 3715 65 4321", "AR")
        self.doTestFindInContext("03715 65 4321", "AR")

        self.doTestFindInContext("+54 23 1234 0000", "AR")
        self.doTestFindInContext("023 1234 0000", "AR")

    # See PhoneNumberUtilTest.testParseWithXInNumber().
    def testFindWithXInNumber(self):
        self.doTestFindInContext("(0xx) 123456789", "AR")
        # A case where x denotes both carrier codes and extension symbol.
        self.doTestFindInContext("(0xx) 123456789 x 1234", "AR")

        # This test is intentionally constructed such that the number of digit
        # after xx is larger than 7, so that the number won't be mistakenly
        # treated as an extension, as we allow extensions up to 7 digits. This
        # assumption is okay for now as all the countries where a carrier
        # selection code is written in the form of xx have a national
        # significant number of length larger than 7.
        self.doTestFindInContext("011xx5481429712", "US")

    # See PhoneNumberUtilTest.testParseNumbersMexico().
    def testFindNumbersMexico(self):
        # Test parsing fixed-line numbers of Mexico.
        self.doTestFindInContext("+52 (449)978-0001", "MX")
        self.doTestFindInContext("01 (449)978-0001", "MX")
        self.doTestFindInContext("(449)978-0001", "MX")

        # Test parsing mobile numbers of Mexico.
        self.doTestFindInContext("+52 1 33 1234-5678", "MX")
        self.doTestFindInContext("044 (33) 1234-5678", "MX")
        self.doTestFindInContext("045 33 1234-5678", "MX")

    # See PhoneNumberUtilTest.testParseNumbersWithPlusWithNoRegion().
    def testFindNumbersWithPlusWithNoRegion(self):
        # "ZZ" is allowed only if the number starts with a '+' - then the
        # country code can be calculated.
        self.doTestFindInContext("+64 3 331 6005", "ZZ")
        # None is also allowed for the region code in these cases.
        self.doTestFindInContext("+64 3 331 6005", None)

    # See PhoneNumberUtilTest.testParseExtensions().
    def testFindExtensions(self):
        self.doTestFindInContext("03 331 6005 ext 3456", "NZ")
        self.doTestFindInContext("03-3316005x3456", "NZ")
        self.doTestFindInContext("03-3316005 int.3456", "NZ")
        self.doTestFindInContext("03 3316005 #3456", "NZ")
        self.doTestFindInContext("0~0 1800 7493 524", "PL")
        self.doTestFindInContext("(1800) 7493.524", "US")
        # Check that the last instance of an extension token is matched.
        self.doTestFindInContext("0~0 1800 7493 524 ~1234", "PL")
        # Verifying bug-fix where the last digit of a number was previously omitted if it was a 0 when
        # extracting the extension. Also verifying a few different cases of extensions.
        self.doTestFindInContext("+44 2034567890x456", "NZ")
        self.doTestFindInContext("+44 2034567890x456", "GB")
        self.doTestFindInContext("+44 2034567890 x456", "GB")
        self.doTestFindInContext("+44 2034567890 X456", "GB")
        self.doTestFindInContext("+44 2034567890 X 456", "GB")
        self.doTestFindInContext("+44 2034567890 X    456", "GB")
        self.doTestFindInContext("+44 2034567890    X 456", "GB")

        self.doTestFindInContext("(800) 901-3355 x 7246433", "US")
        self.doTestFindInContext("(800) 901-3355 , ext 7246433", "US")
        self.doTestFindInContext("(800) 901-3355 ,extension 7246433", "US")
        # The next test differs from phonenumberutil -> when matching we don't
        # consider a lone comma to indicate an extension, although we accept
        # it when parsing.
        self.doTestFindInContext("(800) 901-3355 ,x 7246433", "US")
        self.doTestFindInContext("(800) 901-3355 ext: 7246433", "US")

    def testFindInterspersedWithSpace(self):
        self.doTestFindInContext("0 3   3 3 1   6 0 0 5", "NZ")

    # Test matching behavior when starting in the middle of a phone number.
    def testIntermediateParsePositions(self):
        text = "Call 033316005  or 032316005!"
        #       |    |    |    |    |    |
        #       0    5   10   15   20   25

        # Iterate over all possible indices.
        for ii in range(6):
            self.assertEqualRange(text, ii, 5, 14)

        # 7 and 8 digits in a row are still parsed as number.
        self.assertEqualRange(text, 6, 6, 14)
        self.assertEqualRange(text, 7, 7, 14)
        # Anything smaller is skipped to the second instance.
        for ii in range(8, 20):
            self.assertEqualRange(text, ii, 19, 28)

    def testFourMatchesInARow(self):
        number1 = "415-666-7777"
        number2 = "800-443-1223"
        number3 = "212-443-1223"
        number4 = "650-443-1223"
        text = number1 + " - " + number2 + " - " + number3 + " - " + number4

        matcher = PhoneNumberMatcher(text, "US")
        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number1, "US")

        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number2, "US")

        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number3, "US")

        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number4, "US")

    def testMatchesFoundWithMultipleSpaces(self):
        number1 = "(415) 666-7777"
        number2 = "(800) 443-1223"
        text = number1 + " " + number2

        matcher = PhoneNumberMatcher(text, "US")
        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number1, "US")

        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, text, number2, "US")

    def testMatchWithSurroundingZipcodes(self):
        number = "415-666-7777"
        zipPreceding = "My address is CA 34215 - " + number + " is my number."

        matcher = PhoneNumberMatcher(zipPreceding, "US")
        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, zipPreceding, number, "US")

        # Now repeat, but this time the phone number has spaces in it. It should still be found.
        number = "(415) 666 7777"

        zipFollowing = "My number is " + number + ". 34215 is my zip-code."
        matcher = PhoneNumberMatcher(zipFollowing, "US")
        match = matcher.next() if matcher.has_next() else None
        self.assertMatchProperties(match, zipFollowing, number, "US")

    def testIsLatinLetter(self):
        self.assertTrue(PhoneNumberMatcher._is_latin_letter('c'))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter('C'))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter(u("\u00C9")))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter(u("\u0301")))  # Combining acute accent
        # Punctuation, digits and white-space are not considered "latin letters".
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(':'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('5'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('-'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('.'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(' '))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(u("\u6211")))  # Chinese character
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(u("\u306E")))  # Hiragana letter no

    def testMatchesWithSurroundingLatinChars(self):
        possibleOnlyContexts = []
        possibleOnlyContexts.append(NumberContext("abc", "def"))
        possibleOnlyContexts.append(NumberContext("abc", ""))
        possibleOnlyContexts.append(NumberContext("", "def"))
        # Latin capital letter e with an acute accent.
        possibleOnlyContexts.append(NumberContext(u("\u00C9"), ""))
        # e with an acute accent decomposed (with combining mark).
        possibleOnlyContexts.append(NumberContext(u("e\u0301"), ""))

        # Numbers should not be considered valid, if they are surrounded by
        # Latin characters, but should be considered possible.
        self.findMatchesInContexts(possibleOnlyContexts, False, True)

    def testMoneyNotSeenAsPhoneNumber(self):
        possibleOnlyContexts = []
        possibleOnlyContexts.append(NumberContext("$", ""))
        possibleOnlyContexts.append(NumberContext("", "$"))
        possibleOnlyContexts.append(NumberContext(u("\u00A3"), ""))  # Pound sign
        possibleOnlyContexts.append(NumberContext(u("\u00A5"), ""))  # Yen sign
        self.findMatchesInContexts(possibleOnlyContexts, False, True)

    def testPercentageNotSeenAsPhoneNumber(self):
        possibleOnlyContexts = []
        possibleOnlyContexts.append(NumberContext("", "%"))
        # Numbers followed by % should be dropped.
        self.findMatchesInContexts(possibleOnlyContexts, False, True)

    def testPhoneNumberWithLeadingOrTrailingMoneyMatches(self):
        # Because of the space after the 20 (or before the 100) these dollar
        # amounts should not stop the actual number from being found.
        contexts = []
        contexts.append(NumberContext("$20 ", ""))
        contexts.append(NumberContext("", " 100$"))
        self.findMatchesInContexts(contexts, True, True)

    def testMatchesWithSurroundingLatinCharsAndLeadingPunctuation(self):
        # Contexts with trailing characters. Leading characters are okay here
        # since the numbers we will insert start with punctuation, but
        # trailing characters are still not allowed.
        possibleOnlyContexts = []
        possibleOnlyContexts.append(NumberContext("abc", "def"))
        possibleOnlyContexts.append(NumberContext("", "def"))
        possibleOnlyContexts.append(NumberContext("", u("\u00C9")))

        # Numbers should not be considered valid, if they have trailing Latin
        # characters, but should be considered possible.
        numberWithPlus = "+14156667777"
        numberWithBrackets = "(415)6667777"
        self.findMatchesInContexts(possibleOnlyContexts, False, True, "US", numberWithPlus)
        self.findMatchesInContexts(possibleOnlyContexts, False, True, "US", numberWithBrackets)

        validContexts = []
        validContexts.append(NumberContext("abc", ""))
        validContexts.append(NumberContext(u("\u00C9"), ""))
        validContexts.append(NumberContext(u("\u00C9"), "."))  # Trailing punctuation.
        validContexts.append(NumberContext(u("\u00C9"), " def"))  # Trailing white-space.

        # Numbers should be considered valid, since they start with punctuation.
        self.findMatchesInContexts(validContexts, True, True, "US", numberWithPlus)
        self.findMatchesInContexts(validContexts, True, True, "US", numberWithBrackets)

    def testMatchesWithSurroundingChineseChars(self):
        validContexts = []
        validContexts.append(NumberContext(u("\u6211\u7684\u7535\u8BDD\u53F7\u7801\u662F"), ""))
        validContexts.append(NumberContext("", u("\u662F\u6211\u7684\u7535\u8BDD\u53F7\u7801")))
        validContexts.append(NumberContext(u("\u8BF7\u62E8\u6253"), u("\u6211\u5728\u660E\u5929")))

        # Numbers should be considered valid, since they are surrounded by Chinese.
        self.findMatchesInContexts(validContexts, True, True)

    def testMatchesWithSurroundingPunctuation(self):
        validContexts = []
        validContexts.append(NumberContext("My number-", ""))    # At end of text.
        validContexts.append(NumberContext("", ".Nice day."))    # At start of text.
        validContexts.append(NumberContext("Tel:", "."))    # Punctuation surrounds number.
        validContexts.append(NumberContext("Tel: ", " on Saturdays."))    # White-space is also fine.

        # Numbers should be considered valid, since they are surrounded by punctuation.
        self.findMatchesInContexts(validContexts, True, True)

    def testMatchesMultiplePhoneNumbersSeparatedByPhoneNumberPunctuation(self):
        text = "Call 650-253-4561 -- 455-234-3451"
        region = "US"
        number1 = PhoneNumber(country_code=phonenumberutil.country_code_for_region(region),
                              national_number=6502534561)
        match1 = PhoneNumberMatch(5, "650-253-4561", number1)
        number2 = PhoneNumber(country_code=phonenumberutil.country_code_for_region(region),
                              national_number=4552343451)
        match2 = PhoneNumberMatch(21, "455-234-3451", number2)

        matches = PhoneNumberMatcher(text, region)
        self.assertEqual(match1, matches.next())
        self.assertEqual(match2, matches.next())

    def testDoesNotMatchMultiplePhoneNumbersSeparatedWithNoWhiteSpace(self):
        # No white-space found between numbers - neither is found.
        text = "Call 650-253-4561--455-234-3451"
        region = "US"
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher(text, region)))

    def testMatchesWithPossibleLeniency(self):
        testCases = STRICT_GROUPING_CASES + EXACT_GROUPING_CASES + VALID_CASES + POSSIBLE_ONLY_CASES
        self._doTestNumberMatchesForLeniency(testCases, Leniency.POSSIBLE)

    def testNonMatchesWithPossibleLeniency(self):
        testCases = IMPOSSIBLE_CASES
        self._doTestNumberNonMatchesForLeniency(testCases, Leniency.POSSIBLE)

    def testMatchesWithValidLeniency(self):
        testCases = STRICT_GROUPING_CASES + EXACT_GROUPING_CASES + VALID_CASES
        self._doTestNumberMatchesForLeniency(testCases, Leniency.VALID)

    def testNonMatchesWithValidLeniency(self):
        testCases = IMPOSSIBLE_CASES + POSSIBLE_ONLY_CASES
        self._doTestNumberNonMatchesForLeniency(testCases, Leniency.VALID)

    def testMatchesWithStrictGroupingLeniency(self):
        testCases = STRICT_GROUPING_CASES + EXACT_GROUPING_CASES
        self._doTestNumberMatchesForLeniency(testCases, Leniency.STRICT_GROUPING)

    def testNonMatchesWithStrictGroupLeniency(self):
        testCases = IMPOSSIBLE_CASES + POSSIBLE_ONLY_CASES + VALID_CASES
        self._doTestNumberNonMatchesForLeniency(testCases, Leniency.STRICT_GROUPING)

    def testMatchesWithExactGroupingLeniency(self):
        testCases = EXACT_GROUPING_CASES
        self._doTestNumberMatchesForLeniency(testCases, Leniency.EXACT_GROUPING)

    def testNonMatchesExactGroupLeniency(self):
        testCases = IMPOSSIBLE_CASES + POSSIBLE_ONLY_CASES + VALID_CASES + STRICT_GROUPING_CASES
        self._doTestNumberNonMatchesForLeniency(testCases, Leniency.EXACT_GROUPING)

    def _doTestNumberMatchesForLeniency(self, testCases, leniency):
        noMatchFoundCount = 0
        wrongMatchFoundCount = 0
        for test in testCases:
            iterator = self.findNumbersForLeniency(test.rawString, test.region, leniency)
            match = iterator.next() if iterator.has_next() else None
            if match is None:
                noMatchFoundCount += 1
                prnt("No match found in  %s for leniency: %s" % (test, leniency), file=sys.stderr)
            else:
                if test.rawString != match.raw_string:
                    wrongMatchFoundCount += 1
                    prnt("Found wrong match in test %s. Found %s" % (test, match), file=sys.stderr)
        self.assertEqual(0, noMatchFoundCount)
        self.assertEqual(0, wrongMatchFoundCount)

    def _doTestNumberNonMatchesForLeniency(self, testCases, leniency):
        matchFoundCount = 0
        for test in testCases:
            iterator = self.findNumbersForLeniency(test.rawString, test.region, leniency)
            match = iterator.next() if iterator.has_next() else None
            if match is not None:
                matchFoundCount += 1
                prnt("Match found in %s for leniency: %s" % (test, leniency), file=sys.stderr)
        self.assertEqual(0, matchFoundCount)

    def findMatchesInContexts(self, contexts, isValid, isPossible,
                              region="US", number="415-666-7777"):
        """Helper method which tests the contexts provided and ensures
        that:
         - if isValid is True, they all find a test number inserted in the
           middle when leniency of matching is set to VALID; else no test
           number should be extracted at that leniency level
         - if isPossible is True, they all find a test number inserted in the
           middle when leniency of matching is set to POSSIBLE; else no test
           number should be extracted at that leniency level"""
        if isValid:
            self.doTestInContext(number, region, contexts, Leniency.VALID)
        else:
            for context in contexts:
                text = context.leadingText + number + context.trailingText
                self.assertTrue(self.hasNoMatches(PhoneNumberMatcher(text, region)),
                                msg="Should not have found a number in " + text)
        if isPossible:
            self.doTestInContext(number, region, contexts, Leniency.POSSIBLE)
        else:
            for context in contexts:
                text = context.leadingText + number + context.trailingText
                self.assertTrue(self.hasNoMatches(PhoneNumberMatcher(text, region,
                                                                     leniency=Leniency.POSSIBLE, max_tries=65535)),
                                msg="Should not have found a number in " + text)

    def testNonMatchingBracketsAreInvalid(self):
        # The digits up to the ", " form a valid US number, but it shouldn't
        # be matched as one since there was a non-matching bracket present.
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("80.585 [79.964, 81.191]", "US")))

        # The trailing "]" is thrown away before parsing, so the resultant
        # number, while a valid US number, does not have matching brackets.
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("80.585 [79.964]", "US")))

        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("80.585 ((79.964)", "US")))

        # This case has too many sets of brackets to be valid.
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("(80).(585) (79).(9)64", "US")))

    def testNoMatchIfRegionIsNone(self):
        # Fail on non-international prefix if region code is None.
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("Random text body - number is 0331 6005, see you there", None)))

    def testNoMatchInEmptyString(self):
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("", "US")))
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("  ", "US")))

    def testNoMatchIfNoNumber(self):
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher("Random text body - number is foobar, see you there", "US")))

    def testSequences(self):
        # Test multiple occurrences.
        text = "Call 033316005  or 032316005!"
        region = "NZ"

        number1 = PhoneNumber()
        number1.country_code = phonenumberutil.country_code_for_region(region)
        number1.national_number = 33316005
        match1 = PhoneNumberMatch(5, "033316005", number1)

        number2 = PhoneNumber()
        number2.country_code = phonenumberutil.country_code_for_region(region)
        number2.national_number = 32316005
        match2 = PhoneNumberMatch(19, "032316005", number2)

        matcher = PhoneNumberMatcher(text, region, Leniency.POSSIBLE, 65535)

        self.assertEqual(match1, matcher.next())
        self.assertEqual(match2, matcher.next())
        self.assertFalse(matcher.has_next())

    def testNoneInput(self):
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher(None, "US")))
        self.assertTrue(self.hasNoMatches(PhoneNumberMatcher(None, None)))

    def testMaxMatches(self):
        # Set up text with 100 valid phone numbers.
        numbers = "My info: 415-666-7777," * 100

        # Matches all 100. Max only applies to failed cases.
        number = phonenumberutil.parse("+14156667777", None)
        expected = [number] * 100

        matcher = PhoneNumberMatcher(numbers, "US", Leniency.VALID, 10)
        actual = [x.number for x in matcher]

        self.assertEqual(expected, actual)

    def testMaxMatchesInvalid(self):
        # Set up text with 10 invalid phone numbers followed by 100 valid.
        numbers = (("My address 949-8945-0" * 10) +
                   ("My info: 415-666-7777," * 100))
        matcher = PhoneNumberMatcher(numbers, "US", Leniency.VALID, 10)
        self.assertFalse(matcher.has_next())

    def testMaxMatchesMixed(self):
        # Set up text with 100 valid numbers inside an invalid number.
        numbers = "My info: 415-666-7777 123 fake street" * 100

        # Only matches the first 10 despite there being 100 numbers due to max matches.
        number = phonenumberutil.parse("+14156667777", None)
        expected = [number] * 10

        matcher = PhoneNumberMatcher(numbers, "US", Leniency.VALID, 10)
        actual = [x.number for x in matcher]

        self.assertEqual(expected, actual)

    def testNonPlusPrefixedNumbersNotFoundForInvalidRegion(self):
        # Does not start with a "+", we won't match it.
        matcher = PhoneNumberMatcher("1 456 764 156", "ZZ")
        self.assertFalse(matcher.has_next())
        try:
            matcher.next()
            self.fail("Violation of the Iterator contract.")
        except Exception:
            # Success
            pass
        self.assertFalse(matcher.has_next())

    def testEmptyIteration(self):
        matcher = PhoneNumberMatcher("", "ZZ")
        self.assertFalse(matcher.has_next())
        self.assertFalse(matcher.has_next())
        try:
            matcher.next()
            self.fail("Violation of the iterator contract.")
        except Exception:
            # Success
            pass
        self.assertFalse(matcher.has_next())

    def testSingleIteration(self):
        matcher = PhoneNumberMatcher("+14156667777", "ZZ")

        # With hasNext() -> next().
        # Double hasNext() to ensure it does not advance.
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.next() is not None)
        self.assertFalse(matcher.has_next())
        try:
            matcher.next()
            self.fail("Violation of the Matcher contract.")
        except Exception:
            # Success
            pass
        self.assertFalse(matcher.has_next())

        # With next() only.
        matcher = PhoneNumberMatcher("+14156667777", "ZZ")
        self.assertTrue(matcher.next() is not None)
        try:
            matcher.next()
            self.fail("Violation of the Matcher contract.")
        except Exception:
            # Success
            pass

    def testDoubleIteration(self):
        matcher = PhoneNumberMatcher("+14156667777 foobar +14156667777 ", "ZZ")

        # With hasNext() -> next().
        # Double hasNext() to ensure it does not advance.
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.next() is not None)
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.has_next())
        self.assertTrue(matcher.next() is not None)
        self.assertFalse(matcher.has_next())
        try:
            matcher.next()
            self.fail("Violation of the Matcher contract.")
        except Exception:
            # Success
            pass
        self.assertFalse(matcher.has_next())

        # With next() only.
        matcher = PhoneNumberMatcher("+14156667777 foobar +14156667777 ", "ZZ")
        self.assertTrue(matcher.next() is not None)
        self.assertTrue(matcher.next() is not None)
        try:
            matcher.next()
            self.fail("Violation of the Matcher contract.")
        except Exception:
            # Success
            pass

    def assertEqualRange(self, text, index, start, end):
        """Asserts that another number can be found in text starting at index, and that
        its corresponding range is [start, end).
        """
        sub = text[index:]
        matcher = PhoneNumberMatcher(sub, "NZ", Leniency.POSSIBLE, 65535)

        self.assertTrue(matcher.has_next())
        match = matcher.next()
        self.assertEqual(start - index, match.start)
        self.assertEqual(end - index, match.end)
        self.assertEqual(sub[match.start:match.end], match.raw_string)

    def assertMatchProperties(self, match, text, number, region):
        """Asserts that the expected match is non-null, and that the raw string
        and expected proto buffer are set appropriately."""
        expectedResult = phonenumberutil.parse(number, region)
        self.assertTrue(match is not None,
                        msg="Did not find a number in '" + text + "'; expected " + number)
        self.assertEqual(expectedResult, match.number)
        self.assertEqual(number, match.raw_string)

    def doTestFindInContext(self, number, defaultCountry):
        """Tests numbers found by PhoneNumberMatcher in various textual contexts"""
        self.findPossibleInContext(number, defaultCountry)
        parsed = phonenumberutil.parse(number, defaultCountry)
        if phonenumberutil.is_valid_number(parsed):
            self.findValidInContext(number, defaultCountry)

    def findPossibleInContext(self, number, defaultCountry):
        """Tests valid numbers in contexts that should pass for Leniency.POSSIBLE"""
        contextPairs = [NumberContext("", ""),    # no context
                        NumberContext("     ", "\t"),    # whitespace only
                        NumberContext("Hello ", ""),    # no context at end
                        NumberContext("", " to call me!"),    # no context at start
                        NumberContext("Hi there, call ", " to reach me!"),    # no context at start
                        NumberContext("Hi there, call ", ", or don't"),    # with commas
                        # Three examples without whitespace around the number.
                        NumberContext("Hi call", ""),
                        NumberContext("", "forme"),
                        NumberContext("Hi call", "forme"),
                        # With other small numbers.
                        NumberContext("It's cheap! Call ", " before 6:30"),
                        # With a second number later.
                        NumberContext("Call ", " or +1800-123-4567!"),
                        NumberContext("Call me on June 2 at", ""),    # with a Month-Day date
                        # With publication pages.
                        NumberContext("As quoted by Alfonso 12-15 (2009), you may call me at ", ""),
                        NumberContext("As quoted by Alfonso et al. 12-15 (2009), you may call me at ", ""),
                        # With dates, written in the American style.
                        NumberContext("As I said on 03/10/2011, you may call me at ", ""),
                        # With trailing numbers after a comma. The 45 should not be considered an extension.
                        NumberContext("", ", 45 days a year"),
                        # With a postfix stripped off as it looks like the start of another number.
                        NumberContext("Call ", "/x12 more"),
                        ]

        self.doTestInContext(number, defaultCountry, contextPairs, Leniency.POSSIBLE)

    def findValidInContext(self, number, defaultCountry):
        """Tests valid numbers in contexts that fail for Leniency.POSSIBLE but
        are valid for Leniency.VALID."""
        contextPairs = [
            # With other small numbers.
            NumberContext("It's only 9.99! Call ", " to buy"),
            # With a number Day.Month.Year date.
            NumberContext("Call me on 21.6.1984 at ", ""),
            # With a number Month/Day date.
            NumberContext("Call me on 06/21 at ", ""),
            # With a number Day.Month date.
            NumberContext("Call me on 21.6. at ", ""),
            # With a number Month/Day/Year date.
            NumberContext("Call me on 06/21/84 at ", ""),
        ]
        self.doTestInContext(number, defaultCountry, contextPairs, Leniency.VALID)

    def doTestInContext(self, number, defaultCountry, contextPairs, leniency):
        for context in contextPairs:
            prefix = context.leadingText
            text = prefix + number + context.trailingText

            start = len(prefix)
            end = start + len(number)
            matcher = PhoneNumberMatcher(text, defaultCountry, leniency, 65535)

            match = matcher.next() if matcher.has_next() else None
            self.assertTrue(match is not None,
                            msg="Did not find a number in '" + text + "'; expected '" + number + "'")

            extracted = text[match.start:match.end]
            self.assertEqual(start, match.start,
                             msg="Unexpected phone region in '" + text + "'; extracted '" + extracted + "'")
            self.assertEqual(end, match.end,
                             msg="Unexpected phone region in '" + text + "'; extracted '" + extracted + "'")
            self.assertEqual(number, extracted)
            self.assertEqual(match.raw_string, extracted)

            self.ensureTermination(text, defaultCountry, leniency)

    # Exhaustively searches for phone numbers from each index within text to
    # test that finding matches always terminates.
    def ensureTermination(self, text, defaultCountry, leniency):
        for index in range(len(text) + 1):
            sub = text[index:]
            matches = ""
            # Iterates over all matches.
            for match in PhoneNumberMatcher(sub, defaultCountry, leniency, 65535):
                matches += ", " + str(match)

    def findNumbersForLeniency(self, text, defaultCountry, leniency):
        return PhoneNumberMatcher(text, defaultCountry, leniency, 65535)

    def hasNoMatches(self, matcher):
        """Returns True if there were no matches found."""
        return not matcher.has_next()

    def testDoubleExtensionX(self):
        # Python version extra test - multiple x for extension marker
        xx_ext = "800 234 1 111 xx 1111"
        # This gives different results for different leniency values (and so
        # can't be used in a NumberTest).
        m0 = PhoneNumberMatcher(xx_ext, "US", leniency=Leniency.POSSIBLE).next()
        self.assertEqual(xx_ext, m0.raw_string)
        matcher2 = PhoneNumberMatcher(xx_ext, "US", leniency=Leniency.STRICT_GROUPING)
        self.assertFalse(matcher2.has_next())

    def testInternals(self):
        # Python-specific test: coverage of internals
        from phonenumbers.phonenumbermatcher import _limit, _verify, _is_national_prefix_present_if_required, _get_national_number_groups
        from phonenumbers import CountryCodeSource
        self.assertEqual("{1,2}", _limit(1, 2))
        self.assertRaises(Exception, _limit, *(-1, 2))
        self.assertRaises(Exception, _limit, *(1, 0))
        self.assertRaises(Exception, _limit, *(2, 1))
        number = PhoneNumber(country_code=44, national_number=7912345678)
        self.assertRaises(Exception, _verify, *(99, number, "12345678"))
        self.assertRaises(ValueError, PhoneNumberMatcher, *("text", "US"), **{"leniency": None})
        self.assertRaises(ValueError, PhoneNumberMatcher, *("text", "US"), **{"max_tries": -2})
        # Invalid country looks like national prefix is present (no way to tell)
        number2 = PhoneNumber(country_code=99, national_number=12345678, country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY)
        self.assertTrue(_is_national_prefix_present_if_required(number2))
        # National prefix rule has no lead digits
        number3 = PhoneNumber(country_code=61, national_number=1234567890, country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY)
        self.assertTrue(_is_national_prefix_present_if_required(number3))
        # Coverage for _get_national_number_groups() with a formatting pattern provided
        us_number = PhoneNumber(country_code=1, national_number=6502530000)
        num_format = NumberFormat(pattern="(\\d{3})(\\d{3})(\\d{4})", format="\\1-\\2-\\3")
        self.assertEqual(["650", "253", "0000"],
                         _get_national_number_groups(us_number, num_format))
