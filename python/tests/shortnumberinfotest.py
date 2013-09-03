#!/usr/bin/env python
"""Unit tests for shortnumberinfo.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/ShortNumberInfoTest.java
# Copyright (C) 2013 The Libphonenumber Authors
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

from phonenumbers import connects_to_emergency_number, is_emergency_number, ShortNumberCost
from phonenumbers import is_possible_short_number, is_possible_short_number_object
from phonenumbers import is_valid_short_number, is_valid_short_number_object
from phonenumbers import expected_cost
from phonenumbers import shortnumberinfo, ShortNumberCost, PhoneNumber
from .testmetadatatest import TestMetadataTestCase


# Note that these test use real metadata for short numbers, but test metadata o/w.
class ShortNumberInfoTest(TestMetadataTestCase):
    """Unit tests for shortnumberinfo.py"""
    def testIsPossibleShortNumber(self):
        possibleNumber = PhoneNumber(country_code=33, national_number=123456)
        self.assertTrue(is_possible_short_number_object(possibleNumber))
        self.assertTrue(is_possible_short_number("123456", "FR"))

        impossibleNumber = PhoneNumber(country_code=33, national_number=9)
        self.assertFalse(is_possible_short_number_object(impossibleNumber))
        self.assertFalse(is_possible_short_number("9", "FR"))

        # Python version extra test: check invalid region code
        self.assertFalse(is_possible_short_number("123456", "XY"))
        # Python version extra test: multiple regions with same calling code
        self.assertTrue(is_possible_short_number_object(
                PhoneNumber(country_code=44, national_number=18001)))
        # Python version extra test: multiple regions with same calling code, hit none
        self.assertFalse(is_possible_short_number_object(
                PhoneNumber(country_code=44, national_number=58001)))

    def testIsValidShortNumber(self):
        self.assertTrue(is_valid_short_number_object(
                PhoneNumber(country_code=33, national_number=1010)))
        self.assertTrue(is_valid_short_number("1010", "FR"))
        self.assertFalse(is_valid_short_number_object(
                PhoneNumber(country_code=33, national_number=123456)))
        self.assertFalse(is_valid_short_number("123456", "FR"))

        # Note that GB and GG share the country calling code 44.
        self.assertTrue(is_valid_short_number_object(
                PhoneNumber(country_code=44, national_number=18001)))

        # Python version extra test: check invalid region code
        self.assertFalse(is_valid_short_number("123456", "XY"))
        # Python version extra test: not matching general desc
        self.assertFalse(is_valid_short_number("2123456", "US"))

    def testGetExpectedCost(self):
        premiumRateNumber = PhoneNumber(country_code=33,
                                        national_number=int(shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.PREMIUM_RATE)))
        self.assertEqual(ShortNumberCost.PREMIUM_RATE, expected_cost(premiumRateNumber))

        standardRateNumber = PhoneNumber(country_code=33,
                                         national_number=int(shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.STANDARD_RATE)))
        self.assertEqual(ShortNumberCost.STANDARD_RATE, expected_cost(standardRateNumber))

        tollFreeNumber = PhoneNumber(country_code=33,
                                     national_number=int(shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.TOLL_FREE)))
        self.assertEqual(ShortNumberCost.TOLL_FREE, expected_cost(tollFreeNumber))

        unknownCostNumber = PhoneNumber(country_code=33, national_number=12345)
        self.assertEqual(ShortNumberCost.UNKNOWN_COST, expected_cost(unknownCostNumber))

        # Test that an invalid number may nevertheless have a cost other than UNKNOWN_COST.
        invalidNumber = PhoneNumber(country_code=33, national_number=116123)
        self.assertFalse(is_valid_short_number_object(invalidNumber))
        self.assertEqual(ShortNumberCost.TOLL_FREE, expected_cost(invalidNumber))

        # Test a non-existent country code.
        unknownCostNumber.country_code = 123
        unknownCostNumber.national_number = 911
        self.assertEqual(ShortNumberCost.UNKNOWN_COST, expected_cost(unknownCostNumber))

    def testGetExampleShortNumber(self):
        self.assertEqual("8711", shortnumberinfo._example_short_number("AM"))
        self.assertEqual("1010", shortnumberinfo._example_short_number("FR"))
        self.assertEqual("", shortnumberinfo._example_short_number("001"))
        self.assertEqual("", shortnumberinfo._example_short_number(None))

    def testGetExampleShortNumberForCost(self):
        self.assertEqual("3010",
                         shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.TOLL_FREE))
        self.assertEqual("118777",
                         shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.STANDARD_RATE))
        self.assertEqual("3200",
                         shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.PREMIUM_RATE))
        self.assertEqual("",
                         shortnumberinfo._example_short_number_for_cost("FR", ShortNumberCost.UNKNOWN_COST))
        # Python version extra test
        self.assertEqual("",
                         shortnumberinfo._example_short_number_for_cost("XY", ShortNumberCost.UNKNOWN_COST))

    def testConnectsToEmergencyNumber_US(self):
        self.assertTrue(connects_to_emergency_number("911", "US"))
        self.assertTrue(connects_to_emergency_number("112", "US"))
        self.assertFalse(connects_to_emergency_number("999", "US"))

    def testConnectsToEmergencyNumberLongNumber_US(self):
        self.assertTrue(connects_to_emergency_number("9116666666", "US"))
        self.assertTrue(connects_to_emergency_number("1126666666", "US"))
        self.assertFalse(connects_to_emergency_number("9996666666", "US"))

    def testConnectsToEmergencyNumberWithFormatting_US(self):
        self.assertTrue(connects_to_emergency_number("9-1-1", "US"))
        self.assertTrue(connects_to_emergency_number("1-1-2", "US"))
        self.assertFalse(connects_to_emergency_number("9-9-9", "US"))

    def testConnectsToEmergencyNumberWithPlusSign_US(self):
        self.assertFalse(connects_to_emergency_number("+911", "US"))
        self.assertFalse(connects_to_emergency_number(u"\uFF0B911", "US"))
        self.assertFalse(connects_to_emergency_number(" +911", "US"))
        self.assertFalse(connects_to_emergency_number("+112", "US"))
        self.assertFalse(connects_to_emergency_number("+999", "US"))

    def testConnectsToEmergencyNumber_BR(self):
        self.assertTrue(connects_to_emergency_number("911", "BR"))
        self.assertTrue(connects_to_emergency_number("190", "BR"))
        self.assertFalse(connects_to_emergency_number("999", "BR"))

    def testConnectsToEmergencyNumberLongNumber_BR(self):
        # Brazilian emergency numbers don't work when additional digits are appended.
        self.assertFalse(connects_to_emergency_number("9111", "BR"))
        self.assertFalse(connects_to_emergency_number("1900", "BR"))
        self.assertFalse(connects_to_emergency_number("9996", "BR"))

    def testConnectsToEmergencyNumber_CL(self):
        self.assertTrue(connects_to_emergency_number("131", "CL"))
        self.assertTrue(connects_to_emergency_number("133", "CL"))

    def testConnectsToEmergencyNumberLongNumber_CL(self):
        # Chilean emergency numbers don't work when additional digits are appended.
        self.assertFalse(connects_to_emergency_number("1313", "CL"))
        self.assertFalse(connects_to_emergency_number("1330", "CL"))

    def testConnectsToEmergencyNumber_AO(self):
        # Angola doesn't have any metadata for emergency numbers in the test metadata.
        self.assertFalse(connects_to_emergency_number("911", "AO"))
        self.assertFalse(connects_to_emergency_number("222123456", "AO"))
        self.assertFalse(connects_to_emergency_number("923123456", "AO"))

    def testConnectsToEmergencyNumber_ZW(self):
        # Zimbabwe doesn't have any metadata in the test metadata.
        self.assertFalse(connects_to_emergency_number("911", "ZW"))
        self.assertFalse(connects_to_emergency_number("01312345", "ZW"))
        self.assertFalse(connects_to_emergency_number("0711234567", "ZW"))

    def testIsEmergencyNumber_US(self):
        self.assertTrue(is_emergency_number("911", "US"))
        self.assertTrue(is_emergency_number("112", "US"))
        self.assertFalse(is_emergency_number("999", "US"))

    def testIsEmergencyNumberLongNumber_US(self):
        self.assertFalse(is_emergency_number("9116666666", "US"))
        self.assertFalse(is_emergency_number("1126666666", "US"))
        self.assertFalse(is_emergency_number("9996666666", "US"))

    def testIsEmergencyNumberWithFormatting_US(self):
        self.assertTrue(is_emergency_number("9-1-1", "US"))
        self.assertTrue(is_emergency_number("*911", "US"))
        self.assertTrue(is_emergency_number("1-1-2", "US"))
        self.assertTrue(is_emergency_number("*112", "US"))
        self.assertFalse(is_emergency_number("9-9-9", "US"))
        self.assertFalse(is_emergency_number("*999", "US"))

    def testIsEmergencyNumberWithPlusSign_US(self):
        self.assertFalse(is_emergency_number("+911", "US"))
        self.assertFalse(is_emergency_number("\uFF0B911", "US"))
        self.assertFalse(is_emergency_number(" +911", "US"))
        self.assertFalse(is_emergency_number("+119", "US"))
        self.assertFalse(is_emergency_number("+999", "US"))

    def testIsEmergencyNumber_BR(self):
        self.assertTrue(is_emergency_number("911", "BR"))
        self.assertTrue(is_emergency_number("190", "BR"))
        self.assertFalse(is_emergency_number("999", "BR"))

    def testIsEmergencyNumberLongNumber_BR(self):
        self.assertFalse(is_emergency_number("9111", "BR"))
        self.assertFalse(is_emergency_number("1900", "BR"))
        self.assertFalse(is_emergency_number("9996", "BR"))

    def testIsEmergencyNumber_AO(self):
        # Angola doesn't have any metadata for emergency numbers in the test metadata.
        self.assertFalse(is_emergency_number("911", "AO"))
        self.assertFalse(is_emergency_number("222123456", "AO"))
        self.assertFalse(is_emergency_number("923123456", "AO"))

    def testIsEmergencyNumber_ZW(self):
        # Zimbabwe doesn't have any metadata in the test metadata.
        self.assertFalse(is_emergency_number("911", "ZW"))
        self.assertFalse(is_emergency_number("01312345", "ZW"))
        self.assertFalse(is_emergency_number("0711234567", "ZW"))

        # Python version extra test: invalid region code
        self.assertFalse(is_emergency_number("911", "XY"))
