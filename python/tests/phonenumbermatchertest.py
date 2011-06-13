#!/usr/bin/env python
"""Unit tests for phonenumbermatcher.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/PhoneNumberMatchTest.java
#     java/test/com/google/i18n/phonenumbers/PhoneNumberMatcherTest.java
# Copyright (C) 2011 Google Inc.
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

import pathfix
pathfix.fix()

from phonenumbers import PhoneNumberMatch, PhoneNumberMatcher, Leniency
from phonenumbers import PhoneNumber, phonenumberutil
from phonenumberutiltest import insert_test_metadata, reinstate_real_metadata


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

        self.assertEquals(match1, match2)
        self.assertEquals(match1.start, match2.start)
        self.assertEquals(match1.end, match2.end)
        self.assertEquals(match1.number, match2.number)
        self.assertEquals(match1.raw_string, match2.raw_string)
        self.assertEquals("1 800 234 45 67", match1.raw_string)
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

        self.assertEquals("PhoneNumberMatch [10,25) 1 800 234 45 67", str(match))
        # Python version extra test
        self.assertEquals("PhoneNumberMatch(start=10, raw_string='1 800 234 45 67', " +
                          "numobj=PhoneNumber(country_code=None, national_number=None, extension=None, " +
                          "italian_leading_zero=False, country_code_source=None, preferred_domestic_carrier_code=None))", repr(match))


class NumberContext(object):
    """Small class that holds the context of the number we are testing
    against. The test will insert the phone number to be found between
    leadingText and trailingText."""
    def __init__(self, leadingText, trailingText):
        self.leadingText = leadingText
        self.trailingText = trailingText


class PhoneNumberMatcherTest(unittest.TestCase):
    """Tests for PhoneNumberMatcher.

    This only tests basic functionality based on test metadata.  See
    testphonenumberutil.py for the origin of the test data.
    """

    def setUp(self):
        insert_test_metadata()

    def tearDown(self):
        reinstate_real_metadata()

    # See PhoneNumberUtilTest.testParseNationalNumber().
    def testFindNationalNumber(self):
        # same cases as in testParseNationalNumber
        self.doTestFindInContext("033316005", "NZ")
        self.doTestFindInContext("33316005", "NZ")
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
        self.doTestFindInContext("123/45678", "DE")
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
        self.doTestFindInContext(u"\uFF0B1 (650) 333-6000", "SG")
        # The whole number, including punctuation, is here represented in
        # full-width form.
        self.doTestFindInContext(u"\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09" +
                                 u"\u3000\uFF13\uFF13\uFF13\uFF0D\uFF16\uFF10\uFF10\uFF10",
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
        self.doTestFindInContext("(800) 901-3355 , 7246433", "US")
        self.doTestFindInContext("(800) 901-3355 ext: 7246433", "US")

    def testFindInterspersedWithSpace(self):
        self.doTestFindInContext("0 3   3 3 1   6 0 0 5", "NZ")

    # Test matching behavior when starting in the middle of a phone number.
    def testIntermediateParsePositions(self):
        text = "Call 033316005  or 032316005!"
        #       |    |    |    |    |    |
        #       0    5   10   15   20   25

        # Iterate over all possible indices.
        for ii in xrange(6):
            self.assertEqualRange(text, ii, 5, 14)

        # 7 and 8 digits in a row are still parsed as number.
        self.assertEqualRange(text, 6, 6, 14)
        self.assertEqualRange(text, 7, 7, 14)
        # Anything smaller is skipped to the second instance.
        for ii in xrange(8, 20):
            self.assertEqualRange(text, ii, 19, 28)

    def testMatchWithSurroundingZipcodes(self):
        number = "415-666-7777"
        zipPreceding = "My address is CA 34215. " + number + " is my number."
        expectedResult = phonenumberutil.parse(number, "US")

        matcher = PhoneNumberMatcher(zipPreceding, "US")
        if matcher.has_next():
            match = matcher.next()
        else:
            match = None
        self.assertTrue(match is not None,
                        msg="Did not find a number in '" + zipPreceding + "'; expected " + number)
        self.assertEquals(expectedResult, match.number)
        self.assertEquals(number, match.raw_string)

        # Now repeat, but this time the phone number has spaces in it. It should still be found.
        number = "(415) 666 7777"

        zipFollowing = "My number is " + number + ". 34215 is my zip-code."
        matcher = PhoneNumberMatcher(zipFollowing, "US")
        if matcher.has_next():
            matchWithSpaces = matcher.next()
        else:
            matchWithSpaces = None
        self.assertTrue(matchWithSpaces is not None,
                        msg="Did not find a number in '" + zipFollowing + "'; expected " + number)
        self.assertEquals(expectedResult, matchWithSpaces.number)
        self.assertEquals(number, matchWithSpaces.raw_string)

    def testIsLatinLetter(self):
        self.assertTrue(PhoneNumberMatcher._is_latin_letter('c'))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter('C'))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter(u'\u00C9'))
        self.assertTrue(PhoneNumberMatcher._is_latin_letter(u'\u0301'))  # Combining acute accent
        # Punctuation, digits and white-space are not considered "latin letters".
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(':'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('5'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('-'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter('.'))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(' '))
        self.assertFalse(PhoneNumberMatcher._is_latin_letter(u'\u6211'))  # Chinese character

    def testMatchesWithSurroundingLatinChars(self):
        contextPairs = []
        contextPairs.append(NumberContext("abc", "def"))
        contextPairs.append(NumberContext("abc", ""))
        contextPairs.append(NumberContext("", "def"))
        # Latin small letter e with an acute accent.
        contextPairs.append(NumberContext(u"\u00C9", ""))
        # Same character decomposed (with combining mark).
        contextPairs.append(NumberContext(u"e\u0301", ""))

        # Numbers should not be considered valid, if they are surrounded by
        # Latin characters, but should be considered possible.
        self.findMatchesInContexts(contextPairs, False, True)

    def testMatchesWithSurroundingLatinCharsAndLeadingPunctuation(self):
        # Contexts with trailing characters. Leading characters are okay here
        # since the numbers we will insert start with punctuation, but
        # trailing characters are still not allowed.
        possibleOnlyContexts = []
        possibleOnlyContexts.append(NumberContext("abc", "def"))
        possibleOnlyContexts.append(NumberContext("", "def"))
        possibleOnlyContexts.append(NumberContext("", u"\u00C9"))

        # Numbers should not be considered valid, if they have trailing Latin
        # characters, but should be considered possible.
        numberWithPlus = "+14156667777"
        numberWithBrackets = "(415)6667777"
        self.findMatchesInContexts(possibleOnlyContexts, False, True, "US", numberWithPlus)
        self.findMatchesInContexts(possibleOnlyContexts, False, True, "US", numberWithBrackets)

        validContexts = []
        validContexts.append(NumberContext("abc", ""))
        validContexts.append(NumberContext(u"\u00C9", ""))
        validContexts.append(NumberContext(u"\u00C9", "."))  # Trailing punctuation.
        validContexts.append(NumberContext(u"\u00C9", " def"))  # Trailing white-space.

        # Numbers should be considered valid, since they start with punctuation.
        self.findMatchesInContexts(validContexts, True, True, "US", numberWithPlus)
        self.findMatchesInContexts(validContexts, True, True, "US", numberWithBrackets)

    def testMatchesWithSurroundingChineseChars(self):
        validContexts = []
        validContexts.append(NumberContext(u"\u6211\u7684\u7535\u8BDD\u53F7\u7801\u662F", ""))
        validContexts.append(NumberContext("", u"\u662F\u6211\u7684\u7535\u8BDD\u53F7\u7801"))
        validContexts.append(NumberContext(u"\u8BF7\u62E8\u6253", u"\u6211\u5728\u660E\u5929"))

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
                                                                     leniency=Leniency.POSSIBLE, max_tries=sys.maxint)),
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

        matcher = PhoneNumberMatcher(text, region, Leniency.POSSIBLE, sys.maxint)

        self.assertEquals(match1, matcher.next())
        self.assertEquals(match2, matcher.next())
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

        self.assertEquals(expected, actual)

    def testMaxMatchesInvalid(self):
        # Set up text with 10 invalid phone numbers followed by 100 valid.
        numbers = (("My address 949-8945-0" * 10) +
                   ("My info: 415-666-7777," * 100))
        matcher = PhoneNumberMatcher(numbers, "US", Leniency.VALID, 10)
        self.assertFalse(matcher.has_next())

    def testMaxMatchesMixed(self):
        # Set up text with 100 valid numbers inside an invalid number.
        numbers = "My info: 415-666-7777 123 fake street" * 100

        # Only matches the first 5 despite there being 100 numbers due to max matches.
        # There are two false positives per line as "123" is also tried.
        number = phonenumberutil.parse("+14156667777", None)
        expected = [number] * 5

        matcher = PhoneNumberMatcher(numbers, "US", Leniency.VALID, 10)
        actual = [x.number for x in matcher]

        self.assertEquals(expected, actual)

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
        matcher = PhoneNumberMatcher(sub, "NZ", Leniency.POSSIBLE, sys.maxint)

        self.assertTrue(matcher.has_next())
        match = matcher.next()
        self.assertEquals(start - index, match.start)
        self.assertEquals(end - index, match.end)
        self.assertEquals(match.raw_string, sub[match.start:match.end])

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
                        NumberContext("Call me on June 21 at", ""),    # with a Month-Day date
                        # With publication pages.
                        NumberContext("As quoted by Alfonso 12-15 (2009), you may call me at ", ""),
                        NumberContext("As quoted by Alfonso et al. 12-15 (2009), you may call me at ", ""),
                        # With dates, written in the American style.
                        NumberContext("As I said on 03/10/2011, you may call me at ", ""),
                        NumberContext("As I said on 03/27/2011, you may call me at ", ""),
                        NumberContext("As I said on 31/8/2011, you may call me at ", ""),
                        NumberContext("As I said on 1/12/2011, you may call me at ", ""),
                        NumberContext("I was born on 10/12/82. Please call me at ", ""),
                        # With a postfix stripped off as it looks like the start of another number
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
            # With a number Day.Month date
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
            matcher = PhoneNumberMatcher(text, defaultCountry, leniency, sys.maxint)

            if matcher.has_next():
                match = matcher.next()
            else:
                match = None
            self.assertTrue(match is not None,
                            msg="Did not find a number in '" + text + "'; expected '" + number + "'")

            extracted = text[match.start:match.end]
            self.assertEquals(start, match.start,
                              msg="Unexpected phone region in '" + text + "'; extracted '" + extracted + "'")
            self.assertEquals(end, match.end,
                              msg="Unexpected phone region in '" + text + "'; extracted '" + extracted + "'")
            self.assertEquals(number, extracted)
            self.assertEquals(match.raw_string, extracted)

            self.ensureTermination(text, defaultCountry, leniency)

    # Exhaustively searches for phone numbers from each index within text to
    # test that finding matches always terminates.
    def ensureTermination(self, text, defaultCountry, leniency):
        for index in xrange(len(text) + 1):
            sub = text[index:]
            matches = ""
            # Iterates over all matches.
            for match in PhoneNumberMatcher(sub, defaultCountry, leniency, sys.maxint):
                matches += ", " + str(match)

    def hasNoMatches(self, matcher):
        """Returns True if there were no matches found."""
        return not matcher.has_next()

    def testInternals(self):
        # Python-specific test: coverage of internals
        from phonenumbers.phonenumbermatcher import _limit, _verify
        self.assertEqual("{1,2}", _limit(1, 2))
        self.assertRaises(Exception, _limit, *(-1, 2))
        self.assertRaises(Exception, _limit, *(1, 0))
        self.assertRaises(Exception, _limit, *(2, 1))
        number = PhoneNumber(country_code=44, national_number=7912345678L)
        self.assertRaises(Exception, _verify, *(99, number))
        self.assertRaises(ValueError, PhoneNumberMatcher, *("text", "US"), **{"leniency": None})
        self.assertRaises(ValueError, PhoneNumberMatcher, *("text", "US"), **{"max_tries": -2})
