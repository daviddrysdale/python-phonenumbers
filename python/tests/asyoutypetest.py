#!/usr/bin/env python
"""Unit tests for asyoutypeformatter.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/PhoneNumberTest.java
# Copyright (C) 2009 The Libphonenumber Authors
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
from phonenumbers import AsYouTypeFormatter
from phonenumbers import PhoneMetadata, PhoneNumberDesc, NumberFormat
# Access internal functions of phonenumberutil.py
from phonenumbers import phonenumberutil
from phonenumbers.util import u
from .testmetadatatest import TestMetadataTestCase


class AsYouTypeFormatterTest(TestMetadataTestCase):
    """Unit tests for AsYouTypeFormatter.java

    Note that these tests use the test metadata, not the normal metadata file,
    so should not be used for regression test purposes - these tests are
    illustrative only and test functionality.
    """

    def testInvalidRegion(self):
        formatter = AsYouTypeFormatter("ZZ")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+4", formatter.input_digit('4'))
        self.assertEqual("+48 ", formatter.input_digit('8'))
        self.assertEqual("+48 8", formatter.input_digit('8'))
        self.assertEqual("+48 88", formatter.input_digit('8'))
        self.assertEqual("+48 88 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 12", formatter.input_digit('2'))
        self.assertEqual("+48 88 123", formatter.input_digit('3'))
        self.assertEqual("+48 88 123 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 123 12", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("6", formatter.input_digit('6'))
        self.assertEqual("65", formatter.input_digit('5'))
        self.assertEqual("650", formatter.input_digit('0'))
        self.assertEqual("6502", formatter.input_digit('2'))
        self.assertEqual("65025", formatter.input_digit('5'))
        self.assertEqual("650253", formatter.input_digit('3'))

    def testInvalidPlusSign(self):
        formatter = AsYouTypeFormatter("ZZ")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+4", formatter.input_digit('4'))
        self.assertEqual("+48 ", formatter.input_digit('8'))
        self.assertEqual("+48 8", formatter.input_digit('8'))
        self.assertEqual("+48 88", formatter.input_digit('8'))
        self.assertEqual("+48 88 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 12", formatter.input_digit('2'))
        self.assertEqual("+48 88 123", formatter.input_digit('3'))
        self.assertEqual("+48 88 123 1", formatter.input_digit('1'))
        # A plus sign can only appear at the beginning of the number;
        # otherwise, no formatting is applied.
        self.assertEqual("+48881231+", formatter.input_digit('+'))
        self.assertEqual("+48881231+2", formatter.input_digit('2'))

    def testTooLongNumberMatchingMultipleLeadingDigits(self):
        # See https://github.com/googlei18n/libphonenumber/issues/36
        # The bug occurred last time for countries which have two
        # formatting rules with exactly the same leading digits pattern
        # but differ in length.
        formatter = AsYouTypeFormatter("ZZ")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+81 ", formatter.input_digit('1'))
        self.assertEqual("+81 9", formatter.input_digit('9'))
        self.assertEqual("+81 90", formatter.input_digit('0'))
        self.assertEqual("+81 90 1", formatter.input_digit('1'))
        self.assertEqual("+81 90 12", formatter.input_digit('2'))
        self.assertEqual("+81 90 123", formatter.input_digit('3'))
        self.assertEqual("+81 90 1234", formatter.input_digit('4'))
        self.assertEqual("+81 90 1234 5", formatter.input_digit('5'))
        self.assertEqual("+81 90 1234 56", formatter.input_digit('6'))
        self.assertEqual("+81 90 1234 567", formatter.input_digit('7'))
        self.assertEqual("+81 90 1234 5678", formatter.input_digit('8'))
        self.assertEqual("+81 90 12 345 6789", formatter.input_digit('9'))
        self.assertEqual("+81901234567890", formatter.input_digit('0'))
        self.assertEqual("+819012345678901", formatter.input_digit('1'))

    def testCountryWithSpaceInNationalPrefixFormattingRule(self):
        formatter = AsYouTypeFormatter("BY")
        self.assertEqual("8", formatter.input_digit('8'))
        self.assertEqual("88", formatter.input_digit('8'))
        self.assertEqual("881", formatter.input_digit('1'))
        self.assertEqual("8 819", formatter.input_digit('9'))
        self.assertEqual("8 8190", formatter.input_digit('0'))
        # The formatting rule for 5 digit numbers states that no space should
        # be present after the national prefix.
        self.assertEqual("881 901", formatter.input_digit('1'))
        self.assertEqual("8 819 012", formatter.input_digit('2'))
        # Too long, no formatting rule applies.
        self.assertEqual("88190123", formatter.input_digit('3'))

    def testCountryWithSpaceInNationalPrefixFormattingRuleAndLongNdd(self):
        formatter = AsYouTypeFormatter("BY")
        self.assertEqual("9", formatter.input_digit('9'))
        self.assertEqual("99", formatter.input_digit('9'))
        self.assertEqual("999", formatter.input_digit('9'))
        self.assertEqual("9999", formatter.input_digit('9'))
        self.assertEqual("99999 ", formatter.input_digit('9'))
        self.assertEqual("99999 1", formatter.input_digit('1'))
        self.assertEqual("99999 12", formatter.input_digit('2'))
        self.assertEqual("99999 123", formatter.input_digit('3'))
        self.assertEqual("99999 1234", formatter.input_digit('4'))
        self.assertEqual("99999 12 345", formatter.input_digit('5'))

    def testAYTFUS(self):
        formatter = AsYouTypeFormatter("US")
        self.assertEqual("6", formatter.input_digit('6'))
        self.assertEqual("65", formatter.input_digit('5'))
        self.assertEqual("650", formatter.input_digit('0'))
        self.assertEqual("650 2", formatter.input_digit('2'))
        self.assertEqual("650 25", formatter.input_digit('5'))
        self.assertEqual("650 253", formatter.input_digit('3'))
        # Note this is how a US local number (without area code) should be formatted.
        self.assertEqual("650 2532", formatter.input_digit('2'))
        self.assertEqual("650 253 22", formatter.input_digit('2'))
        self.assertEqual("650 253 222", formatter.input_digit('2'))
        self.assertEqual("650 253 2222", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("16", formatter.input_digit('6'))
        self.assertEqual("1 65", formatter.input_digit('5'))
        self.assertEqual("1 650", formatter.input_digit('0'))
        self.assertEqual("1 650 2", formatter.input_digit('2'))
        self.assertEqual("1 650 25", formatter.input_digit('5'))
        self.assertEqual("1 650 253", formatter.input_digit('3'))
        self.assertEqual("1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("1 650 253 2222", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011 ", formatter.input_digit('1'))
        self.assertEqual("011 4", formatter.input_digit('4'))
        self.assertEqual("011 44 ", formatter.input_digit('4'))
        self.assertEqual("011 44 6", formatter.input_digit('6'))
        self.assertEqual("011 44 61", formatter.input_digit('1'))
        self.assertEqual("011 44 6 12", formatter.input_digit('2'))
        self.assertEqual("011 44 6 123", formatter.input_digit('3'))
        self.assertEqual("011 44 6 123 1", formatter.input_digit('1'))
        self.assertEqual("011 44 6 123 12", formatter.input_digit('2'))
        self.assertEqual("011 44 6 123 123", formatter.input_digit('3'))
        self.assertEqual("011 44 6 123 123 1", formatter.input_digit('1'))
        self.assertEqual("011 44 6 123 123 12", formatter.input_digit('2'))
        self.assertEqual("011 44 6 123 123 123", formatter.input_digit('3'))

        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011 ", formatter.input_digit('1'))
        self.assertEqual("011 5", formatter.input_digit('5'))
        self.assertEqual("011 54 ", formatter.input_digit('4'))
        self.assertEqual("011 54 9", formatter.input_digit('9'))
        self.assertEqual("011 54 91", formatter.input_digit('1'))
        self.assertEqual("011 54 9 11", formatter.input_digit('1'))
        self.assertEqual("011 54 9 11 2", formatter.input_digit('2'))
        self.assertEqual("011 54 9 11 23", formatter.input_digit('3'))
        self.assertEqual("011 54 9 11 231", formatter.input_digit('1'))
        self.assertEqual("011 54 9 11 2312", formatter.input_digit('2'))
        self.assertEqual("011 54 9 11 2312 1", formatter.input_digit('1'))
        self.assertEqual("011 54 9 11 2312 12", formatter.input_digit('2'))
        self.assertEqual("011 54 9 11 2312 123", formatter.input_digit('3'))
        self.assertEqual("011 54 9 11 2312 1234", formatter.input_digit('4'))

        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011 ", formatter.input_digit('1'))
        self.assertEqual("011 2", formatter.input_digit('2'))
        self.assertEqual("011 24", formatter.input_digit('4'))
        self.assertEqual("011 244 ", formatter.input_digit('4'))
        self.assertEqual("011 244 2", formatter.input_digit('2'))
        self.assertEqual("011 244 28", formatter.input_digit('8'))
        self.assertEqual("011 244 280", formatter.input_digit('0'))
        self.assertEqual("011 244 280 0", formatter.input_digit('0'))
        self.assertEqual("011 244 280 00", formatter.input_digit('0'))
        self.assertEqual("011 244 280 000", formatter.input_digit('0'))
        self.assertEqual("011 244 280 000 0", formatter.input_digit('0'))
        self.assertEqual("011 244 280 000 00", formatter.input_digit('0'))
        self.assertEqual("011 244 280 000 000", formatter.input_digit('0'))

        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+4", formatter.input_digit('4'))
        self.assertEqual("+48 ", formatter.input_digit('8'))
        self.assertEqual("+48 8", formatter.input_digit('8'))
        self.assertEqual("+48 88", formatter.input_digit('8'))
        self.assertEqual("+48 88 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 12", formatter.input_digit('2'))
        self.assertEqual("+48 88 123", formatter.input_digit('3'))
        self.assertEqual("+48 88 123 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 123 12", formatter.input_digit('2'))
        self.assertEqual("+48 88 123 12 1", formatter.input_digit('1'))
        self.assertEqual("+48 88 123 12 12", formatter.input_digit('2'))

        # Python version extra test: invalid country code after IDD
        formatter.clear()
        self.assertEqual('0', formatter.input_digit('0'))
        self.assertEqual('01', formatter.input_digit('1'))
        self.assertEqual('011 ', formatter.input_digit('1'))
        self.assertEqual('011 4', formatter.input_digit('4'))
        self.assertEqual('011 42', formatter.input_digit('2'))
        self.assertEqual('011 422', formatter.input_digit('2'))
        self.assertEqual('011 4221', formatter.input_digit('1'))
        self.assertEqual('011 42212', formatter.input_digit('2'))
        self.assertEqual('011 422123', formatter.input_digit('3'))

    def testAYTFUSFullWidthCharacters(self):
        formatter = AsYouTypeFormatter("US")
        self.assertEqual(u("\uFF16"), formatter.input_digit(u("\uFF16")))
        self.assertEqual(u("\uFF16\uFF15"), formatter.input_digit(u("\uFF15")))
        self.assertEqual("650", formatter.input_digit(u("\uFF10")))
        self.assertEqual("650 2", formatter.input_digit(u("\uFF12")))
        self.assertEqual("650 25", formatter.input_digit(u("\uFF15")))
        self.assertEqual("650 253", formatter.input_digit(u("\uFF13")))
        self.assertEqual("650 2532", formatter.input_digit(u("\uFF12")))
        self.assertEqual("650 253 22", formatter.input_digit(u("\uFF12")))
        self.assertEqual("650 253 222", formatter.input_digit(u("\uFF12")))
        self.assertEqual("650 253 2222", formatter.input_digit(u("\uFF12")))

    def testAYTFUSMobileShortCode(self):
        formatter = AsYouTypeFormatter("US")
        self.assertEqual("*", formatter.input_digit('*'))
        self.assertEqual("*1", formatter.input_digit('1'))
        self.assertEqual("*12", formatter.input_digit('2'))
        self.assertEqual("*121", formatter.input_digit('1'))
        self.assertEqual("*121#", formatter.input_digit('#'))

    def testAYTFUSVanityNumber(self):
        formatter = AsYouTypeFormatter("US")
        self.assertEqual("8", formatter.input_digit('8'))
        self.assertEqual("80", formatter.input_digit('0'))
        self.assertEqual("800", formatter.input_digit('0'))
        self.assertEqual("800 ", formatter.input_digit(' '))
        self.assertEqual("800 M", formatter.input_digit('M'))
        self.assertEqual("800 MY", formatter.input_digit('Y'))
        self.assertEqual("800 MY ", formatter.input_digit(' '))
        self.assertEqual("800 MY A", formatter.input_digit('A'))
        self.assertEqual("800 MY AP", formatter.input_digit('P'))
        self.assertEqual("800 MY APP", formatter.input_digit('P'))
        self.assertEqual("800 MY APPL", formatter.input_digit('L'))
        self.assertEqual("800 MY APPLE", formatter.input_digit('E'))

    def testAYTFAndRememberPositionUS(self):
        formatter = AsYouTypeFormatter("US")
        self.assertEqual("1", formatter.input_digit('1', remember_position=True))
        self.assertEqual(1, formatter.get_remembered_position())
        self.assertEqual("16", formatter.input_digit('6'))
        self.assertEqual("1 65", formatter.input_digit('5'))
        self.assertEqual(1, formatter.get_remembered_position())
        self.assertEqual("1 650", formatter.input_digit('0', remember_position=True))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("1 650 2", formatter.input_digit('2'))
        self.assertEqual("1 650 25", formatter.input_digit('5'))
        # Note the remembered position for digit "0" changes from 4 to 5, because a space is now
        # inserted in the front.
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("1 650 253", formatter.input_digit('3'))
        self.assertEqual("1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("1 650 253 22", formatter.input_digit('2'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("1 650 253 222", formatter.input_digit('2', remember_position=True))
        self.assertEqual(13, formatter.get_remembered_position())
        self.assertEqual("1 650 253 2222", formatter.input_digit('2'))
        self.assertEqual(13, formatter.get_remembered_position())
        self.assertEqual("165025322222", formatter.input_digit('2'))
        self.assertEqual(10, formatter.get_remembered_position())
        self.assertEqual("1650253222222", formatter.input_digit('2'))
        self.assertEqual(10, formatter.get_remembered_position())

        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("16", formatter.input_digit('6', remember_position=True))
        self.assertEqual(2, formatter.get_remembered_position())
        self.assertEqual("1 65", formatter.input_digit('5'))
        self.assertEqual("1 650", formatter.input_digit('0'))
        self.assertEqual(3, formatter.get_remembered_position())
        self.assertEqual("1 650 2", formatter.input_digit('2'))
        self.assertEqual("1 650 25", formatter.input_digit('5'))
        self.assertEqual(3, formatter.get_remembered_position())
        self.assertEqual("1 650 253", formatter.input_digit('3'))
        self.assertEqual("1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("1 650 253 22", formatter.input_digit('2'))
        self.assertEqual(3, formatter.get_remembered_position())
        self.assertEqual("1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("1 650 253 2222", formatter.input_digit('2'))
        self.assertEqual("165025322222", formatter.input_digit('2'))
        self.assertEqual(2, formatter.get_remembered_position())
        self.assertEqual("1650253222222", formatter.input_digit('2'))
        self.assertEqual(2, formatter.get_remembered_position())

        formatter.clear()
        self.assertEqual("6", formatter.input_digit('6'))
        self.assertEqual("65", formatter.input_digit('5'))
        self.assertEqual("650", formatter.input_digit('0'))
        self.assertEqual("650 2", formatter.input_digit('2'))
        self.assertEqual("650 25", formatter.input_digit('5'))
        self.assertEqual("650 253", formatter.input_digit('3'))
        self.assertEqual("650 2532", formatter.input_digit('2', remember_position=True))
        self.assertEqual(8, formatter.get_remembered_position())
        self.assertEqual("650 253 22", formatter.input_digit('2'))
        self.assertEqual(9, formatter.get_remembered_position())
        self.assertEqual("650 253 222", formatter.input_digit('2'))
        # No more formatting when semicolon is entered.
        self.assertEqual("650253222;", formatter.input_digit(';'))
        self.assertEqual(7, formatter.get_remembered_position())
        self.assertEqual("650253222;2", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("6", formatter.input_digit('6'))
        self.assertEqual("65", formatter.input_digit('5'))
        self.assertEqual("650", formatter.input_digit('0'))
        # No more formatting when users choose to do their own formatting.
        self.assertEqual("650-", formatter.input_digit('-'))
        self.assertEqual("650-2", formatter.input_digit('2', remember_position=True))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("650-25", formatter.input_digit('5'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("650-253", formatter.input_digit('3'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("650-253-", formatter.input_digit('-'))
        self.assertEqual("650-253-2", formatter.input_digit('2'))
        self.assertEqual("650-253-22", formatter.input_digit('2'))
        self.assertEqual("650-253-222", formatter.input_digit('2'))
        self.assertEqual("650-253-2222", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011 ", formatter.input_digit('1'))
        self.assertEqual("011 4", formatter.input_digit('4', remember_position=True))
        self.assertEqual("011 48 ", formatter.input_digit('8'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("011 48 8", formatter.input_digit('8'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("011 48 88", formatter.input_digit('8'))
        self.assertEqual("011 48 88 1", formatter.input_digit('1'))
        self.assertEqual("011 48 88 12", formatter.input_digit('2'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("011 48 88 123", formatter.input_digit('3'))
        self.assertEqual("011 48 88 123 1", formatter.input_digit('1'))
        self.assertEqual("011 48 88 123 12", formatter.input_digit('2'))
        self.assertEqual("011 48 88 123 12 1", formatter.input_digit('1'))
        self.assertEqual("011 48 88 123 12 12", formatter.input_digit('2'))

        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+1", formatter.input_digit('1'))
        self.assertEqual("+1 6", formatter.input_digit('6', remember_position=True))
        self.assertEqual("+1 65", formatter.input_digit('5'))
        self.assertEqual("+1 650", formatter.input_digit('0'))
        self.assertEqual(4, formatter.get_remembered_position())
        self.assertEqual("+1 650 2", formatter.input_digit('2'))
        self.assertEqual(4, formatter.get_remembered_position())
        self.assertEqual("+1 650 25", formatter.input_digit('5'))
        self.assertEqual("+1 650 253", formatter.input_digit('3', remember_position=True))
        self.assertEqual("+1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("+1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("+1 650 253 222", formatter.input_digit('2'))
        self.assertEqual(10, formatter.get_remembered_position())

        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+1", formatter.input_digit('1'))
        self.assertEqual("+1 6", formatter.input_digit('6', remember_position=True))
        self.assertEqual("+1 65", formatter.input_digit('5'))
        self.assertEqual("+1 650", formatter.input_digit('0'))
        self.assertEqual(4, formatter.get_remembered_position())
        self.assertEqual("+1 650 2", formatter.input_digit('2'))
        self.assertEqual(4, formatter.get_remembered_position())
        self.assertEqual("+1 650 25", formatter.input_digit('5'))
        self.assertEqual("+1 650 253", formatter.input_digit('3'))
        self.assertEqual("+1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("+1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("+1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("+1650253222;", formatter.input_digit(';'))
        self.assertEqual(3, formatter.get_remembered_position())

    def testAYTFGBFixedLine(self):
        formatter = AsYouTypeFormatter("GB")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("02", formatter.input_digit('2'))
        self.assertEqual("020", formatter.input_digit('0'))
        self.assertEqual("020 7", formatter.input_digit('7', remember_position=True))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("020 70", formatter.input_digit('0'))
        self.assertEqual("020 703", formatter.input_digit('3'))
        self.assertEqual(5, formatter.get_remembered_position())
        self.assertEqual("020 7031", formatter.input_digit('1'))
        self.assertEqual("020 7031 3", formatter.input_digit('3'))
        self.assertEqual("020 7031 30", formatter.input_digit('0'))
        self.assertEqual("020 7031 300", formatter.input_digit('0'))
        self.assertEqual("020 7031 3000", formatter.input_digit('0'))

    def testAYTFGBTollFree(self):
        formatter = AsYouTypeFormatter("GB")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("08", formatter.input_digit('8'))
        self.assertEqual("080", formatter.input_digit('0'))
        self.assertEqual("080 7", formatter.input_digit('7'))
        self.assertEqual("080 70", formatter.input_digit('0'))
        self.assertEqual("080 703", formatter.input_digit('3'))
        self.assertEqual("080 7031", formatter.input_digit('1'))
        self.assertEqual("080 7031 3", formatter.input_digit('3'))
        self.assertEqual("080 7031 30", formatter.input_digit('0'))
        self.assertEqual("080 7031 300", formatter.input_digit('0'))
        self.assertEqual("080 7031 3000", formatter.input_digit('0'))

    def testAYTFGBPremiumRate(self):
        formatter = AsYouTypeFormatter("GB")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("09", formatter.input_digit('9'))
        self.assertEqual("090", formatter.input_digit('0'))
        self.assertEqual("090 7", formatter.input_digit('7'))
        self.assertEqual("090 70", formatter.input_digit('0'))
        self.assertEqual("090 703", formatter.input_digit('3'))
        self.assertEqual("090 7031", formatter.input_digit('1'))
        self.assertEqual("090 7031 3", formatter.input_digit('3'))
        self.assertEqual("090 7031 30", formatter.input_digit('0'))
        self.assertEqual("090 7031 300", formatter.input_digit('0'))
        self.assertEqual("090 7031 3000", formatter.input_digit('0'))

    def testAYTFNZMobile(self):
        formatter = AsYouTypeFormatter("NZ")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("02", formatter.input_digit('2'))
        self.assertEqual("021", formatter.input_digit('1'))
        self.assertEqual("02-11", formatter.input_digit('1'))
        self.assertEqual("02-112", formatter.input_digit('2'))
        # Note the unittest is using fake metadata which might produce non-ideal results.
        self.assertEqual("02-112 3", formatter.input_digit('3'))
        self.assertEqual("02-112 34", formatter.input_digit('4'))
        self.assertEqual("02-112 345", formatter.input_digit('5'))
        self.assertEqual("02-112 3456", formatter.input_digit('6'))

    def testAYTFDE(self):
        formatter = AsYouTypeFormatter("DE")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("03", formatter.input_digit('3'))
        self.assertEqual("030", formatter.input_digit('0'))
        self.assertEqual("030/1", formatter.input_digit('1'))
        self.assertEqual("030/12", formatter.input_digit('2'))
        self.assertEqual("030/123", formatter.input_digit('3'))
        self.assertEqual("030/1234", formatter.input_digit('4'))

        # 04134 1234
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("04", formatter.input_digit('4'))
        self.assertEqual("041", formatter.input_digit('1'))
        self.assertEqual("041 3", formatter.input_digit('3'))
        self.assertEqual("041 34", formatter.input_digit('4'))
        self.assertEqual("04134 1", formatter.input_digit('1'))
        self.assertEqual("04134 12", formatter.input_digit('2'))
        self.assertEqual("04134 123", formatter.input_digit('3'))
        self.assertEqual("04134 1234", formatter.input_digit('4'))

        # 08021 2345
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("08", formatter.input_digit('8'))
        self.assertEqual("080", formatter.input_digit('0'))
        self.assertEqual("080 2", formatter.input_digit('2'))
        self.assertEqual("080 21", formatter.input_digit('1'))
        self.assertEqual("08021 2", formatter.input_digit('2'))
        self.assertEqual("08021 23", formatter.input_digit('3'))
        self.assertEqual("08021 234", formatter.input_digit('4'))
        self.assertEqual("08021 2345", formatter.input_digit('5'))

        # 00 1 650 253 2250
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("00 1 ", formatter.input_digit('1'))
        self.assertEqual("00 1 6", formatter.input_digit('6'))
        self.assertEqual("00 1 65", formatter.input_digit('5'))
        self.assertEqual("00 1 650", formatter.input_digit('0'))
        self.assertEqual("00 1 650 2", formatter.input_digit('2'))
        self.assertEqual("00 1 650 25", formatter.input_digit('5'))
        self.assertEqual("00 1 650 253", formatter.input_digit('3'))
        self.assertEqual("00 1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("00 1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("00 1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("00 1 650 253 2222", formatter.input_digit('2'))

    def testAYTFAR(self):
        formatter = AsYouTypeFormatter("AR")
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011", formatter.input_digit('1'))
        self.assertEqual("011 7", formatter.input_digit('7'))
        self.assertEqual("011 70", formatter.input_digit('0'))
        self.assertEqual("011 703", formatter.input_digit('3'))
        self.assertEqual("011 7031", formatter.input_digit('1'))
        self.assertEqual("011 7031-3", formatter.input_digit('3'))
        self.assertEqual("011 7031-30", formatter.input_digit('0'))
        self.assertEqual("011 7031-300", formatter.input_digit('0'))
        self.assertEqual("011 7031-3000", formatter.input_digit('0'))

    def testAYTFARMobile(self):
        formatter = AsYouTypeFormatter("AR")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+54 ", formatter.input_digit('4'))
        self.assertEqual("+54 9", formatter.input_digit('9'))
        self.assertEqual("+54 91", formatter.input_digit('1'))
        self.assertEqual("+54 9 11", formatter.input_digit('1'))
        self.assertEqual("+54 9 11 2", formatter.input_digit('2'))
        self.assertEqual("+54 9 11 23", formatter.input_digit('3'))
        self.assertEqual("+54 9 11 231", formatter.input_digit('1'))
        self.assertEqual("+54 9 11 2312", formatter.input_digit('2'))
        self.assertEqual("+54 9 11 2312 1", formatter.input_digit('1'))
        self.assertEqual("+54 9 11 2312 12", formatter.input_digit('2'))
        self.assertEqual("+54 9 11 2312 123", formatter.input_digit('3'))
        self.assertEqual("+54 9 11 2312 1234", formatter.input_digit('4'))

    def testAYTFKR(self):
        # +82 51 234 5678
        formatter = AsYouTypeFormatter("KR")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+82 ", formatter.input_digit('2'))
        self.assertEqual("+82 5", formatter.input_digit('5'))
        self.assertEqual("+82 51", formatter.input_digit('1'))
        self.assertEqual("+82 51-2", formatter.input_digit('2'))
        self.assertEqual("+82 51-23", formatter.input_digit('3'))
        self.assertEqual("+82 51-234", formatter.input_digit('4'))
        self.assertEqual("+82 51-234-5", formatter.input_digit('5'))
        self.assertEqual("+82 51-234-56", formatter.input_digit('6'))
        self.assertEqual("+82 51-234-567", formatter.input_digit('7'))
        self.assertEqual("+82 51-234-5678", formatter.input_digit('8'))

        # +82 2 531 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+82 ", formatter.input_digit('2'))
        self.assertEqual("+82 2", formatter.input_digit('2'))
        self.assertEqual("+82 25", formatter.input_digit('5'))
        self.assertEqual("+82 2-53", formatter.input_digit('3'))
        self.assertEqual("+82 2-531", formatter.input_digit('1'))
        self.assertEqual("+82 2-531-5", formatter.input_digit('5'))
        self.assertEqual("+82 2-531-56", formatter.input_digit('6'))
        self.assertEqual("+82 2-531-567", formatter.input_digit('7'))
        self.assertEqual("+82 2-531-5678", formatter.input_digit('8'))

        # +82 2 3665 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+82 ", formatter.input_digit('2'))
        self.assertEqual("+82 2", formatter.input_digit('2'))
        self.assertEqual("+82 23", formatter.input_digit('3'))
        self.assertEqual("+82 2-36", formatter.input_digit('6'))
        self.assertEqual("+82 2-366", formatter.input_digit('6'))
        self.assertEqual("+82 2-3665", formatter.input_digit('5'))
        self.assertEqual("+82 2-3665-5", formatter.input_digit('5'))
        self.assertEqual("+82 2-3665-56", formatter.input_digit('6'))
        self.assertEqual("+82 2-3665-567", formatter.input_digit('7'))
        self.assertEqual("+82 2-3665-5678", formatter.input_digit('8'))

        # 02-114
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("02", formatter.input_digit('2'))
        self.assertEqual("021", formatter.input_digit('1'))
        self.assertEqual("02-11", formatter.input_digit('1'))
        self.assertEqual("02-114", formatter.input_digit('4'))

        # 02-1300
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("02", formatter.input_digit('2'))
        self.assertEqual("021", formatter.input_digit('1'))
        self.assertEqual("02-13", formatter.input_digit('3'))
        self.assertEqual("02-130", formatter.input_digit('0'))
        self.assertEqual("02-1300", formatter.input_digit('0'))

        # 011-456-7890
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011", formatter.input_digit('1'))
        self.assertEqual("011-4", formatter.input_digit('4'))
        self.assertEqual("011-45", formatter.input_digit('5'))
        self.assertEqual("011-456", formatter.input_digit('6'))
        self.assertEqual("011-456-7", formatter.input_digit('7'))
        self.assertEqual("011-456-78", formatter.input_digit('8'))
        self.assertEqual("011-456-789", formatter.input_digit('9'))
        self.assertEqual("011-456-7890", formatter.input_digit('0'))

        # 011-9876-7890
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011", formatter.input_digit('1'))
        self.assertEqual("011-9", formatter.input_digit('9'))
        self.assertEqual("011-98", formatter.input_digit('8'))
        self.assertEqual("011-987", formatter.input_digit('7'))
        self.assertEqual("011-9876", formatter.input_digit('6'))
        self.assertEqual("011-9876-7", formatter.input_digit('7'))
        self.assertEqual("011-9876-78", formatter.input_digit('8'))
        self.assertEqual("011-9876-789", formatter.input_digit('9'))
        self.assertEqual("011-9876-7890", formatter.input_digit('0'))

    def testAYTF_MX(self):
        formatter = AsYouTypeFormatter("MX")
        # +52 800 123 4567
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 8", formatter.input_digit('8'))
        self.assertEqual("+52 80", formatter.input_digit('0'))
        self.assertEqual("+52 800", formatter.input_digit('0'))
        self.assertEqual("+52 800 1", formatter.input_digit('1'))
        self.assertEqual("+52 800 12", formatter.input_digit('2'))
        self.assertEqual("+52 800 123", formatter.input_digit('3'))
        self.assertEqual("+52 800 123 4", formatter.input_digit('4'))
        self.assertEqual("+52 800 123 45", formatter.input_digit('5'))
        self.assertEqual("+52 800 123 456", formatter.input_digit('6'))
        self.assertEqual("+52 800 123 4567", formatter.input_digit('7'))

        # +52 55 1234 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 5", formatter.input_digit('5'))
        self.assertEqual("+52 55", formatter.input_digit('5'))
        self.assertEqual("+52 55 1", formatter.input_digit('1'))
        self.assertEqual("+52 55 12", formatter.input_digit('2'))
        self.assertEqual("+52 55 123", formatter.input_digit('3'))
        self.assertEqual("+52 55 1234", formatter.input_digit('4'))
        self.assertEqual("+52 55 1234 5", formatter.input_digit('5'))
        self.assertEqual("+52 55 1234 56", formatter.input_digit('6'))
        self.assertEqual("+52 55 1234 567", formatter.input_digit('7'))
        self.assertEqual("+52 55 1234 5678", formatter.input_digit('8'))

        # +52 212 345 6789
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 2", formatter.input_digit('2'))
        self.assertEqual("+52 21", formatter.input_digit('1'))
        self.assertEqual("+52 212", formatter.input_digit('2'))
        self.assertEqual("+52 212 3", formatter.input_digit('3'))
        self.assertEqual("+52 212 34", formatter.input_digit('4'))
        self.assertEqual("+52 212 345", formatter.input_digit('5'))
        self.assertEqual("+52 212 345 6", formatter.input_digit('6'))
        self.assertEqual("+52 212 345 67", formatter.input_digit('7'))
        self.assertEqual("+52 212 345 678", formatter.input_digit('8'))
        self.assertEqual("+52 212 345 6789", formatter.input_digit('9'))

        # +52 1 55 1234 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 1", formatter.input_digit('1'))
        self.assertEqual("+52 15", formatter.input_digit('5'))
        self.assertEqual("+52 1 55", formatter.input_digit('5'))
        self.assertEqual("+52 1 55 1", formatter.input_digit('1'))
        self.assertEqual("+52 1 55 12", formatter.input_digit('2'))
        self.assertEqual("+52 1 55 123", formatter.input_digit('3'))
        self.assertEqual("+52 1 55 1234", formatter.input_digit('4'))
        self.assertEqual("+52 1 55 1234 5", formatter.input_digit('5'))
        self.assertEqual("+52 1 55 1234 56", formatter.input_digit('6'))
        self.assertEqual("+52 1 55 1234 567", formatter.input_digit('7'))
        self.assertEqual("+52 1 55 1234 5678", formatter.input_digit('8'))

        # +52 1 541 234 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 1", formatter.input_digit('1'))
        self.assertEqual("+52 15", formatter.input_digit('5'))
        self.assertEqual("+52 1 54", formatter.input_digit('4'))
        self.assertEqual("+52 1 541", formatter.input_digit('1'))
        self.assertEqual("+52 1 541 2", formatter.input_digit('2'))
        self.assertEqual("+52 1 541 23", formatter.input_digit('3'))
        self.assertEqual("+52 1 541 234", formatter.input_digit('4'))
        self.assertEqual("+52 1 541 234 5", formatter.input_digit('5'))
        self.assertEqual("+52 1 541 234 56", formatter.input_digit('6'))
        self.assertEqual("+52 1 541 234 567", formatter.input_digit('7'))
        self.assertEqual("+52 1 541 234 5678", formatter.input_digit('8'))

    def testAYTF_International_Toll_Free(self):
        formatter = AsYouTypeFormatter("US")
        # +800 1234 5678
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+80", formatter.input_digit('0'))
        self.assertEqual("+800 ", formatter.input_digit('0'))
        self.assertEqual("+800 1", formatter.input_digit('1'))
        self.assertEqual("+800 12", formatter.input_digit('2'))
        self.assertEqual("+800 123", formatter.input_digit('3'))
        self.assertEqual("+800 1234", formatter.input_digit('4'))
        self.assertEqual("+800 1234 5", formatter.input_digit('5'))
        self.assertEqual("+800 1234 56", formatter.input_digit('6'))
        self.assertEqual("+800 1234 567", formatter.input_digit('7'))
        self.assertEqual("+800 1234 5678", formatter.input_digit('8'))
        self.assertEqual("+800123456789", formatter.input_digit('9'))

    def testAYTFMultipleLeadingDigitPatterns(self):
        # +81 50 2345 6789
        formatter = AsYouTypeFormatter("JP")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+81 ", formatter.input_digit('1'))
        self.assertEqual("+81 5", formatter.input_digit('5'))
        self.assertEqual("+81 50", formatter.input_digit('0'))
        self.assertEqual("+81 50 2", formatter.input_digit('2'))
        self.assertEqual("+81 50 23", formatter.input_digit('3'))
        self.assertEqual("+81 50 234", formatter.input_digit('4'))
        self.assertEqual("+81 50 2345", formatter.input_digit('5'))
        self.assertEqual("+81 50 2345 6", formatter.input_digit('6'))
        self.assertEqual("+81 50 2345 67", formatter.input_digit('7'))
        self.assertEqual("+81 50 2345 678", formatter.input_digit('8'))
        self.assertEqual("+81 50 2345 6789", formatter.input_digit('9'))

        # +81 222 12 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+81 ", formatter.input_digit('1'))
        self.assertEqual("+81 2", formatter.input_digit('2'))
        self.assertEqual("+81 22", formatter.input_digit('2'))
        self.assertEqual("+81 22 2", formatter.input_digit('2'))
        self.assertEqual("+81 22 21", formatter.input_digit('1'))
        self.assertEqual("+81 2221 2", formatter.input_digit('2'))
        self.assertEqual("+81 222 12 5", formatter.input_digit('5'))
        self.assertEqual("+81 222 12 56", formatter.input_digit('6'))
        self.assertEqual("+81 222 12 567", formatter.input_digit('7'))
        self.assertEqual("+81 222 12 5678", formatter.input_digit('8'))

        # 011113
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("01", formatter.input_digit('1'))
        self.assertEqual("011", formatter.input_digit('1'))
        self.assertEqual("011 1", formatter.input_digit('1'))
        self.assertEqual("011 11", formatter.input_digit('1'))
        self.assertEqual("011113", formatter.input_digit('3'))

        # +81 3332 2 5678
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+81 ", formatter.input_digit('1'))
        self.assertEqual("+81 3", formatter.input_digit('3'))
        self.assertEqual("+81 33", formatter.input_digit('3'))
        self.assertEqual("+81 33 3", formatter.input_digit('3'))
        self.assertEqual("+81 3332", formatter.input_digit('2'))
        self.assertEqual("+81 3332 2", formatter.input_digit('2'))
        self.assertEqual("+81 3332 2 5", formatter.input_digit('5'))
        self.assertEqual("+81 3332 2 56", formatter.input_digit('6'))
        self.assertEqual("+81 3332 2 567", formatter.input_digit('7'))
        self.assertEqual("+81 3332 2 5678", formatter.input_digit('8'))

    def testAYTFLongIDD_AU(self):
        formatter = AsYouTypeFormatter("AU")
        # 0011 1 650 253 2250
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("001", formatter.input_digit('1'))
        self.assertEqual("0011", formatter.input_digit('1'))
        self.assertEqual("0011 1 ", formatter.input_digit('1'))
        self.assertEqual("0011 1 6", formatter.input_digit('6'))
        self.assertEqual("0011 1 65", formatter.input_digit('5'))
        self.assertEqual("0011 1 650", formatter.input_digit('0'))
        self.assertEqual("0011 1 650 2", formatter.input_digit('2'))
        self.assertEqual("0011 1 650 25", formatter.input_digit('5'))
        self.assertEqual("0011 1 650 253", formatter.input_digit('3'))
        self.assertEqual("0011 1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("0011 1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("0011 1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("0011 1 650 253 2222", formatter.input_digit('2'))

        # 0011 81 3332 2 5678
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("001", formatter.input_digit('1'))
        self.assertEqual("0011", formatter.input_digit('1'))
        self.assertEqual("00118", formatter.input_digit('8'))
        self.assertEqual("0011 81 ", formatter.input_digit('1'))
        self.assertEqual("0011 81 3", formatter.input_digit('3'))
        self.assertEqual("0011 81 33", formatter.input_digit('3'))
        self.assertEqual("0011 81 33 3", formatter.input_digit('3'))
        self.assertEqual("0011 81 3332", formatter.input_digit('2'))
        self.assertEqual("0011 81 3332 2", formatter.input_digit('2'))
        self.assertEqual("0011 81 3332 2 5", formatter.input_digit('5'))
        self.assertEqual("0011 81 3332 2 56", formatter.input_digit('6'))
        self.assertEqual("0011 81 3332 2 567", formatter.input_digit('7'))
        self.assertEqual("0011 81 3332 2 5678", formatter.input_digit('8'))

        # 0011 244 250 253 222
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("001", formatter.input_digit('1'))
        self.assertEqual("0011", formatter.input_digit('1'))
        self.assertEqual("00112", formatter.input_digit('2'))
        self.assertEqual("001124", formatter.input_digit('4'))
        self.assertEqual("0011 244 ", formatter.input_digit('4'))
        self.assertEqual("0011 244 2", formatter.input_digit('2'))
        self.assertEqual("0011 244 25", formatter.input_digit('5'))
        self.assertEqual("0011 244 250", formatter.input_digit('0'))
        self.assertEqual("0011 244 250 2", formatter.input_digit('2'))
        self.assertEqual("0011 244 250 25", formatter.input_digit('5'))
        self.assertEqual("0011 244 250 253", formatter.input_digit('3'))
        self.assertEqual("0011 244 250 253 2", formatter.input_digit('2'))
        self.assertEqual("0011 244 250 253 22", formatter.input_digit('2'))
        self.assertEqual("0011 244 250 253 222", formatter.input_digit('2'))

    def testAYTFLongIDD_KR(self):
        formatter = AsYouTypeFormatter("KR")
        # 00300 1 650 253 2222
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("003", formatter.input_digit('3'))
        self.assertEqual("0030", formatter.input_digit('0'))
        self.assertEqual("00300", formatter.input_digit('0'))
        self.assertEqual("00300 1 ", formatter.input_digit('1'))
        self.assertEqual("00300 1 6", formatter.input_digit('6'))
        self.assertEqual("00300 1 65", formatter.input_digit('5'))
        self.assertEqual("00300 1 650", formatter.input_digit('0'))
        self.assertEqual("00300 1 650 2", formatter.input_digit('2'))
        self.assertEqual("00300 1 650 25", formatter.input_digit('5'))
        self.assertEqual("00300 1 650 253", formatter.input_digit('3'))
        self.assertEqual("00300 1 650 253 2", formatter.input_digit('2'))
        self.assertEqual("00300 1 650 253 22", formatter.input_digit('2'))
        self.assertEqual("00300 1 650 253 222", formatter.input_digit('2'))
        self.assertEqual("00300 1 650 253 2222", formatter.input_digit('2'))

    def testAYTFLongNDD_KR(self):
        formatter = AsYouTypeFormatter("KR")
        # 08811-9876-7890
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("08", formatter.input_digit('8'))
        self.assertEqual("088", formatter.input_digit('8'))
        self.assertEqual("0881", formatter.input_digit('1'))
        self.assertEqual("08811", formatter.input_digit('1'))
        self.assertEqual("08811-9", formatter.input_digit('9'))
        self.assertEqual("08811-98", formatter.input_digit('8'))
        self.assertEqual("08811-987", formatter.input_digit('7'))
        self.assertEqual("08811-9876", formatter.input_digit('6'))
        self.assertEqual("08811-9876-7", formatter.input_digit('7'))
        self.assertEqual("08811-9876-78", formatter.input_digit('8'))
        self.assertEqual("08811-9876-789", formatter.input_digit('9'))
        self.assertEqual("08811-9876-7890", formatter.input_digit('0'))

        # 08500 11-9876-7890
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("08", formatter.input_digit('8'))
        self.assertEqual("085", formatter.input_digit('5'))
        self.assertEqual("0850", formatter.input_digit('0'))
        self.assertEqual("08500 ", formatter.input_digit('0'))
        self.assertEqual("08500 1", formatter.input_digit('1'))
        self.assertEqual("08500 11", formatter.input_digit('1'))
        self.assertEqual("08500 11-9", formatter.input_digit('9'))
        self.assertEqual("08500 11-98", formatter.input_digit('8'))
        self.assertEqual("08500 11-987", formatter.input_digit('7'))
        self.assertEqual("08500 11-9876", formatter.input_digit('6'))
        self.assertEqual("08500 11-9876-7", formatter.input_digit('7'))
        self.assertEqual("08500 11-9876-78", formatter.input_digit('8'))
        self.assertEqual("08500 11-9876-789", formatter.input_digit('9'))
        self.assertEqual("08500 11-9876-7890", formatter.input_digit('0'))

    def testAYTFLongNDD_SG(self):
        formatter = AsYouTypeFormatter("SG")
        # 777777 9876 7890
        self.assertEqual("7", formatter.input_digit('7'))
        self.assertEqual("77", formatter.input_digit('7'))
        self.assertEqual("777", formatter.input_digit('7'))
        self.assertEqual("7777", formatter.input_digit('7'))
        self.assertEqual("77777", formatter.input_digit('7'))
        self.assertEqual("777777 ", formatter.input_digit('7'))
        self.assertEqual("777777 9", formatter.input_digit('9'))
        self.assertEqual("777777 98", formatter.input_digit('8'))
        self.assertEqual("777777 987", formatter.input_digit('7'))
        self.assertEqual("777777 9876", formatter.input_digit('6'))
        self.assertEqual("777777 9876 7", formatter.input_digit('7'))
        self.assertEqual("777777 9876 78", formatter.input_digit('8'))
        self.assertEqual("777777 9876 789", formatter.input_digit('9'))
        self.assertEqual("777777 9876 7890", formatter.input_digit('0'))

    def testAYTFNoNationalPrefixFormattingRule(self):
        formatter = AsYouTypeFormatter("AO")
        self.assertEqual("3", formatter.input_digit('3'))
        self.assertEqual("33", formatter.input_digit('3'))
        self.assertEqual("333", formatter.input_digit('3'))
        self.assertEqual("333 3", formatter.input_digit('3'))
        self.assertEqual("333 33", formatter.input_digit('3'))
        self.assertEqual("333 333", formatter.input_digit('3'))

    def testAYTFShortNumberFormattingFix_AU(self):
        # For Australia, the national prefix is not optional when formatting.
        formatter = AsYouTypeFormatter("AU")

        # 1234567890 - For leading digit 1, the national prefix formatting
        # rule has first group only.
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("12", formatter.input_digit('2'))
        self.assertEqual("123", formatter.input_digit('3'))
        self.assertEqual("1234", formatter.input_digit('4'))
        self.assertEqual("1234 5", formatter.input_digit('5'))
        self.assertEqual("1234 56", formatter.input_digit('6'))
        self.assertEqual("1234 567", formatter.input_digit('7'))
        self.assertEqual("1234 567 8", formatter.input_digit('8'))
        self.assertEqual("1234 567 89", formatter.input_digit('9'))
        self.assertEqual("1234 567 890", formatter.input_digit('0'))

        # +61 1234 567 890 - Test the same number, but with the country code.
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+6", formatter.input_digit('6'))
        self.assertEqual("+61 ", formatter.input_digit('1'))
        self.assertEqual("+61 1", formatter.input_digit('1'))
        self.assertEqual("+61 12", formatter.input_digit('2'))
        self.assertEqual("+61 123", formatter.input_digit('3'))
        self.assertEqual("+61 1234", formatter.input_digit('4'))
        self.assertEqual("+61 1234 5", formatter.input_digit('5'))
        self.assertEqual("+61 1234 56", formatter.input_digit('6'))
        self.assertEqual("+61 1234 567", formatter.input_digit('7'))
        self.assertEqual("+61 1234 567 8", formatter.input_digit('8'))
        self.assertEqual("+61 1234 567 89", formatter.input_digit('9'))
        self.assertEqual("+61 1234 567 890", formatter.input_digit('0'))

        # 212345678 - For leading digit 2, the national prefix formatting rule
        # puts the national prefix before the first group.
        formatter.clear()
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("02", formatter.input_digit('2'))
        self.assertEqual("021", formatter.input_digit('1'))
        self.assertEqual("02 12", formatter.input_digit('2'))
        self.assertEqual("02 123", formatter.input_digit('3'))
        self.assertEqual("02 1234", formatter.input_digit('4'))
        self.assertEqual("02 1234 5", formatter.input_digit('5'))
        self.assertEqual("02 1234 56", formatter.input_digit('6'))
        self.assertEqual("02 1234 567", formatter.input_digit('7'))
        self.assertEqual("02 1234 5678", formatter.input_digit('8'))

        # 212345678 - Test the same number, but without the leading 0.
        formatter.clear()
        self.assertEqual("2", formatter.input_digit('2'))
        self.assertEqual("21", formatter.input_digit('1'))
        self.assertEqual("212", formatter.input_digit('2'))
        self.assertEqual("2123", formatter.input_digit('3'))
        self.assertEqual("21234", formatter.input_digit('4'))
        self.assertEqual("212345", formatter.input_digit('5'))
        self.assertEqual("2123456", formatter.input_digit('6'))
        self.assertEqual("21234567", formatter.input_digit('7'))
        self.assertEqual("212345678", formatter.input_digit('8'))

        # +61 2 1234 5678 - Test the same number, but with the country code.
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+6", formatter.input_digit('6'))
        self.assertEqual("+61 ", formatter.input_digit('1'))
        self.assertEqual("+61 2", formatter.input_digit('2'))
        self.assertEqual("+61 21", formatter.input_digit('1'))
        self.assertEqual("+61 2 12", formatter.input_digit('2'))
        self.assertEqual("+61 2 123", formatter.input_digit('3'))
        self.assertEqual("+61 2 1234", formatter.input_digit('4'))
        self.assertEqual("+61 2 1234 5", formatter.input_digit('5'))
        self.assertEqual("+61 2 1234 56", formatter.input_digit('6'))
        self.assertEqual("+61 2 1234 567", formatter.input_digit('7'))
        self.assertEqual("+61 2 1234 5678", formatter.input_digit('8'))

    def testAYTFShortNumberFormattingFix_KR(self):
        # For Korea, the national prefix is not optional when formatting, and
        # the national prefix formatting rule doesn't consist of only the
        # first group.
        formatter = AsYouTypeFormatter("KR")

        # 111
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("11", formatter.input_digit('1'))
        self.assertEqual("111", formatter.input_digit('1'))

        # 114
        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("11", formatter.input_digit('1'))
        self.assertEqual("114", formatter.input_digit('4'))

        # 13121234 - Test a mobile number without the national prefix. Even
        # though it is not an emergency number, it should be formatted as a
        # block.
        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("13", formatter.input_digit('3'))
        self.assertEqual("131", formatter.input_digit('1'))
        self.assertEqual("1312", formatter.input_digit('2'))
        self.assertEqual("13121", formatter.input_digit('1'))
        self.assertEqual("131212", formatter.input_digit('2'))
        self.assertEqual("1312123", formatter.input_digit('3'))
        self.assertEqual("13121234", formatter.input_digit('4'))

        # +82 131-2-1234 - Test the same number, but with the country code.
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+82 ", formatter.input_digit('2'))
        self.assertEqual("+82 1", formatter.input_digit('1'))
        self.assertEqual("+82 13", formatter.input_digit('3'))
        self.assertEqual("+82 131", formatter.input_digit('1'))
        self.assertEqual("+82 131-2", formatter.input_digit('2'))
        self.assertEqual("+82 131-2-1", formatter.input_digit('1'))
        self.assertEqual("+82 131-2-12", formatter.input_digit('2'))
        self.assertEqual("+82 131-2-123", formatter.input_digit('3'))
        self.assertEqual("+82 131-2-1234", formatter.input_digit('4'))

    def testAYTFShortNumberFormattingFix_MX(self):
        # For Mexico, the national prefix is optional when formatting.
        formatter = AsYouTypeFormatter("MX")

        # 911
        self.assertEqual("9", formatter.input_digit('9'))
        self.assertEqual("91", formatter.input_digit('1'))
        self.assertEqual("911", formatter.input_digit('1'))

        # 800 123 4567 - Test a toll-free number, which should have a
        # formatting rule applied to it even though it doesn't begin with the
        # national prefix.
        formatter.clear()
        self.assertEqual("8", formatter.input_digit('8'))
        self.assertEqual("80", formatter.input_digit('0'))
        self.assertEqual("800", formatter.input_digit('0'))
        self.assertEqual("800 1", formatter.input_digit('1'))
        self.assertEqual("800 12", formatter.input_digit('2'))
        self.assertEqual("800 123", formatter.input_digit('3'))
        self.assertEqual("800 123 4", formatter.input_digit('4'))
        self.assertEqual("800 123 45", formatter.input_digit('5'))
        self.assertEqual("800 123 456", formatter.input_digit('6'))
        self.assertEqual("800 123 4567", formatter.input_digit('7'))

        # +52 800 123 4567 - Test the same number, but with the country code.
        formatter.clear()
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+5", formatter.input_digit('5'))
        self.assertEqual("+52 ", formatter.input_digit('2'))
        self.assertEqual("+52 8", formatter.input_digit('8'))
        self.assertEqual("+52 80", formatter.input_digit('0'))
        self.assertEqual("+52 800", formatter.input_digit('0'))
        self.assertEqual("+52 800 1", formatter.input_digit('1'))
        self.assertEqual("+52 800 12", formatter.input_digit('2'))
        self.assertEqual("+52 800 123", formatter.input_digit('3'))
        self.assertEqual("+52 800 123 4", formatter.input_digit('4'))
        self.assertEqual("+52 800 123 45", formatter.input_digit('5'))
        self.assertEqual("+52 800 123 456", formatter.input_digit('6'))
        self.assertEqual("+52 800 123 4567", formatter.input_digit('7'))

    def testAYTFNoNationalPrefix(self):
        formatter = AsYouTypeFormatter("IT")
        self.assertEqual("3", formatter.input_digit('3'))
        self.assertEqual("33", formatter.input_digit('3'))
        self.assertEqual("333", formatter.input_digit('3'))
        self.assertEqual("333 3", formatter.input_digit('3'))
        self.assertEqual("333 33", formatter.input_digit('3'))
        self.assertEqual("333 333", formatter.input_digit('3'))

    def testAYTFShortNumberFormattingFix_US(self):
        # For the US, an initial 1 is treated specially.
        formatter = AsYouTypeFormatter("US")

        # 101 - Test that the initial 1 is not treated as a national prefix.
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("10", formatter.input_digit('0'))
        self.assertEqual("101", formatter.input_digit('1'))

        # 112 - Test that the initial 1 is not treated as a national prefix.
        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("11", formatter.input_digit('1'))
        self.assertEqual("112", formatter.input_digit('2'))

        # 122 - Test that the initial 1 is treated as a national prefix.
        formatter.clear()
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("12", formatter.input_digit('2'))
        self.assertEqual("1 22", formatter.input_digit('2'))

    def testAYTFClearNDDAfterIDDExtraction(self):
        formatter = AsYouTypeFormatter("KR")

        # Check that when we have successfully extracted an IDD, the
        # previously extracted NDD is cleared since it is no longer valid.
        self.assertEqual("0", formatter.input_digit('0'))
        self.assertEqual("00", formatter.input_digit('0'))
        self.assertEqual("007", formatter.input_digit('7'))
        self.assertEqual("0070", formatter.input_digit('0'))
        self.assertEqual("00700", formatter.input_digit('0'))
        self.assertEqual("0", formatter._extracted_national_prefix)

        # Once the IDD "00700" has been extracted, it no longer makes sense
        # for the initial "0" to be treated as an NDD.
        self.assertEqual("00700 1 ", formatter.input_digit('1'))
        self.assertEqual("", formatter._extracted_national_prefix)

        self.assertEqual("00700 1 2", formatter.input_digit('2'))
        self.assertEqual("00700 1 23", formatter.input_digit('3'))
        self.assertEqual("00700 1 234", formatter.input_digit('4'))
        self.assertEqual("00700 1 234 5", formatter.input_digit('5'))
        self.assertEqual("00700 1 234 56", formatter.input_digit('6'))
        self.assertEqual("00700 1 234 567", formatter.input_digit('7'))
        self.assertEqual("00700 1 234 567 8", formatter.input_digit('8'))
        self.assertEqual("00700 1 234 567 89", formatter.input_digit('9'))
        self.assertEqual("00700 1 234 567 890", formatter.input_digit('0'))
        self.assertEqual("00700 1 234 567 8901", formatter.input_digit('1'))
        self.assertEqual("00700123456789012", formatter.input_digit('2'))
        self.assertEqual("007001234567890123", formatter.input_digit('3'))
        self.assertEqual("0070012345678901234", formatter.input_digit('4'))
        self.assertEqual("00700123456789012345", formatter.input_digit('5'))
        self.assertEqual("007001234567890123456", formatter.input_digit('6'))
        self.assertEqual("0070012345678901234567", formatter.input_digit('7'))

    def testAYTFNumberPatternsBecomingInvalidShouldNotResultInDigitLoss(self):
        formatter = AsYouTypeFormatter("CN")
        self.assertEqual("+", formatter.input_digit('+'))
        self.assertEqual("+8", formatter.input_digit('8'))
        self.assertEqual("+86 ", formatter.input_digit('6'))
        self.assertEqual("+86 9", formatter.input_digit('9'))
        self.assertEqual("+86 98", formatter.input_digit('8'))
        self.assertEqual("+86 988", formatter.input_digit('8'))
        self.assertEqual("+86 988 1", formatter.input_digit('1'))
        # Now the number pattern is no longer valid because there are multiple
        # leading digit patterns; when we try again to extract a country code
        # we should ensure we use the last leading digit pattern, rather than
        # the first one such that it *thinks* it's found a valid formatting
        # rule again.
        # https://github.com/googlei18n/libphonenumber/issues/437
        self.assertEqual("+8698812", formatter.input_digit('2'))
        self.assertEqual("+86988123", formatter.input_digit('3'))
        self.assertEqual("+869881234", formatter.input_digit('4'))
        self.assertEqual("+8698812345", formatter.input_digit('5'))

    def testAYTFShortNumberFormatting_AR(self):
        # Python version extra test: use real metadata
        formatter = AsYouTypeFormatter("AR")
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("10", formatter.input_digit('0'))
        self.assertEqual("101", formatter.input_digit('1'))

    def testEdgeCases(self):
        # Python version extra tests for coverage
        metadataXX = PhoneMetadata(id='XX', country_code=384, international_prefix='011',
                                   general_desc=PhoneNumberDesc(national_number_pattern='\\d{10}', possible_number_pattern='\\d{6,10}'),
                                   fixed_line=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
                                   mobile=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
                                   national_prefix=u("0"),
                                   national_prefix_for_parsing=u("0"),
                                   number_format=[NumberFormat(pattern='([135][246]|[246][123])(\\d{4})(\\d{4})',
                                                               format=u("\\1 \\2 \\3"),
                                                               leading_digits_pattern=['[1-59]|[78]0'],
                                                               national_prefix_formatting_rule=u("\\1"))])
        PhoneMetadata._region_metadata['XX'] = metadataXX
        phonenumberutil.SUPPORTED_REGIONS.add("XX")
        phonenumberutil.COUNTRY_CODE_TO_REGION_CODE[384] = ("XX",)
        formatter = AsYouTypeFormatter('XX')
        # A pattern with "|" in it doesn't get formatting
        self.assertEqual('1', formatter.input_digit('1'))
        self.assertEqual('12', formatter.input_digit('2'))
        self.assertEqual('123', formatter.input_digit('3'))
        self.assertEqual('1234', formatter.input_digit('4'))
        # Hit internal error arms
        self.assertEqual("1234", formatter._input_accrued_national_number())
        formatter._national_number = ""
        self.assertEqual("", formatter._input_accrued_national_number())
        # Restore normality
        del phonenumberutil.COUNTRY_CODE_TO_REGION_CODE[384]
        phonenumberutil.SUPPORTED_REGIONS.remove('XX')
        del PhoneMetadata._region_metadata['XX']
