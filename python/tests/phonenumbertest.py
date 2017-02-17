#!/usr/bin/env python
"""Unit tests for phonenumberutil.py"""

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
import unittest

from phonenumbers import PhoneNumber, CountryCodeSource, FrozenPhoneNumber
from phonenumbers.util import to_long


class PhoneNumberTest(unittest.TestCase):
    """Tests for the Phonenumber.PhoneNumber object itself."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal_simple_number(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberB = PhoneNumber(country_code=1, national_number=6502530000)
        self.assertEqual(numberA, numberB)

    def test_equal_with_italian_leading_zero_set_to_default(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.italian_leading_zero = False
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = to_long(6502530000)
        # These should still be equal, since the default value for this field
        # is false.
        self.assertEqual(numberA, numberB)

    def test_equal_with_country_code_source_set(self):
        numberA = PhoneNumber()
        numberA.raw_input = "+1 650 253 00 00"
        numberA.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        numberB = PhoneNumber()
        numberB.raw_input = "+1 650 253 00 00"
        numberB.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertEqual(numberA, numberB)

    def test_non_equal_with_italian_leading_zero_set(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.italian_leading_zero = True
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = to_long(6502530000)
        self.assertNotEqual(numberA, numberB)

    def test_non_equal_with_differing_raw_input(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.raw_input = "+1 650 253 00 00"
        numberA.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        numberB = PhoneNumber()
        # Although these numbers would pass an isNumberMatch test, they are
        # not considered "equal" as objects, since their raw input is
        # different.
        numberB.country_code = 1
        numberB.national_number = to_long(6502530000)
        numberB.raw_input = "+1-650-253-00-00"
        numberB.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertNotEqual(numberA, numberB)
        # Python-specific: Force a test of __ne__() method
        self.assertTrue(numberA != numberB)

    def test_non_equal_with_preferred_dcc_default(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.preferred_domestic_carrier_code = ""
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = to_long(6502530000)
        self.assertNotEqual(numberA, numberB)

    def test_equal_with_preferred_dcc_set(self):
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.preferred_domestic_carrier_code = ""
        numberB = PhoneNumber()
        numberB.country_code = 1
        numberB.national_number = to_long(6502530000)
        numberB.preferred_domestic_carrier_code = ""
        self.assertEqual(numberA, numberB)

    def test_equal_other_objects(self):
        # Python-specific extra tests for equality against other types
        numberA = PhoneNumber()
        numberA.country_code = 1
        numberA.national_number = to_long(6502530000)
        numberA.preferred_domestic_carrier_code = ""
        self.assertNotEqual(numberA, None)
        self.assertNotEqual(numberA, "")
        self.assertNotEqual(numberA, "+16502530000")
        self.assertNotEqual(numberA, to_long(6502530000))

    def testMergeFrom(self):
        # Python version extra test
        full_number = PhoneNumber(country_code=44, national_number=7912345678, extension=123,
                                  italian_leading_zero=True, number_of_leading_zeros=3,
                                  raw_input="+440007912345678 ext 123",
                                  country_code_source=CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN,
                                  preferred_domestic_carrier_code="7912")
        other = PhoneNumber()
        other.merge_from(full_number)
        self.assertEqual(other, full_number)

    def testFrozenPhoneNumber(self):
        # Python version extra tests
        gb_mobile = PhoneNumber(country_code=44, national_number=7912345678)
        it_number = PhoneNumber(country_code=39, national_number=236618300, italian_leading_zero=True)
        frozen_gb_mobile1 = FrozenPhoneNumber(country_code=44, national_number=7912345678)
        frozen_it_number1 = FrozenPhoneNumber(country_code=39, national_number=236618300, italian_leading_zero=True)
        frozen_gb_mobile2 = FrozenPhoneNumber(gb_mobile)
        frozen_it_number2 = FrozenPhoneNumber(it_number)
        self.assertEqual(frozen_gb_mobile1, gb_mobile)
        self.assertEqual(frozen_gb_mobile2, gb_mobile)
        self.assertEqual(frozen_gb_mobile1, frozen_gb_mobile2)
        self.assertEqual(frozen_it_number1, it_number)
        self.assertEqual(frozen_it_number2, it_number)
        self.assertEqual(frozen_it_number1, frozen_it_number2)
        self.assertEqual(hash(frozen_it_number1), hash(frozen_it_number2))
        self.assertNotEqual(hash(frozen_it_number1), hash(frozen_gb_mobile1))
        phonedict = {frozen_it_number1: 1, frozen_gb_mobile1: 2}
        self.assertEqual(phonedict[frozen_it_number1], 1)
        try:
            frozen_gb_mobile1.country_code = 12
            self.fail("Should not be able to modify FrozenPhoneNubmer")
        except TypeError:
            pass
        try:
            frozen_gb_mobile2.raw_input = ""
            self.fail("Should not be able to modify FrozenPhoneNubmer")
        except TypeError:
            pass
        try:
            frozen_gb_mobile1.clear()
            self.fail("Should not be able to modify FrozenPhoneNubmer")
        except TypeError:
            pass
        try:
            frozen_gb_mobile1.merge_from(frozen_it_number1)
            self.fail("Should not be able to modify FrozenPhoneNubmer")
        except TypeError:
            pass
        try:
            del frozen_gb_mobile1.country_code
            self.fail("Should not be able to modify FrozenPhoneNubmer")
        except TypeError:
            pass
        # Coverage test
        frozen_gb_mobile1._mutable = True
        del frozen_gb_mobile1.country_code
