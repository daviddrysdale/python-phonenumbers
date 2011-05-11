#!/usr/bin/env python
"""Unit tests for phonenumberutil.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/PhoneNumberTest.java
# Copyright (C) 2009 Google Inc.
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
import unittest

import pathfix
pathfix.fix()

from phonenumbers import PhoneNumber, CountryCodeSource


class PhoneNumberTest(unittest.TestCase):
    """Tests for the Phonenumber.PhoneNumber object itself."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal_simple_number(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberB = PhoneNumber(country_code=1, national_number=6502530000L)
        self.assertEquals(numberA, numberB)

    def test_equal_with_italian_leading_zero_set_to_default(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.italian_leading_zero = False
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = 6502530000L
        # These should still be equal, since the default value for this field
        # is false.
        self.assertEquals(numberA, numberB)

    def test_equal_with_country_code_source_set(self):
        numberA = PhoneNumber()
        numberA.raw_input = "+1 650 253 00 00"
        numberA.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        numberB = PhoneNumber()
        numberB.raw_input = "+1 650 253 00 00"
        numberB.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertEquals(numberA, numberB)

    def test_non_equal_with_italian_leading_zero_set(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.italian_leading_zero = True
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = 6502530000L
        self.assertNotEqual(numberA, numberB)

    def test_non_equal_with_differing_raw_input(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.raw_input = "+1 650 253 00 00"
        numberA.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        numberB = PhoneNumber()
        # Although these numbers would pass an isNumberMatch test, they are
        # not considered "equal" as objects, since their raw input is
        # different.
        numberB.country_code = 1
        numberB.national_number = 6502530000L
        numberB.raw_input = "+1-650-253-00-00"
        numberB.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertNotEqual(numberA, numberB)
        # Python-specific: Force a test of __ne__() method
        self.assertTrue(numberA != numberB)

    def test_non_equal_with_preferred_dcc_default(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.preferred_domestic_carrier_code = ""
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = 6502530000L
        self.assertNotEqual(numberA, numberB)

    def test_equal_with_preferred_dcc_set(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.preferred_domestic_carrier_code = ""
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = 6502530000L
        numberB.preferred_domestic_carrier_code = ""
        self.assertEquals(numberA, numberB)

    def test_equal_other_objects(self):
        # Python-specific extra tests for equality against other types
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = 6502530000L
        numberA.preferred_domestic_carrier_code = ""
        self.assertNotEqual(numberA, None)
        self.assertNotEqual(numberA, "")
        self.assertNotEqual(numberA, "+16502530000")
        self.assertNotEqual(numberA, 6502530000L)
