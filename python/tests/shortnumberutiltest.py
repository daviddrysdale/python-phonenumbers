#!/usr/bin/env python
"""Unit tests for shortnumberutil.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/ShortNumberUtilTest.java
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

import unittest

from phonenumbers import connects_to_emergency_number, is_emergency_number
from .phonenumberutiltest import insert_test_metadata, reinstate_real_metadata


class ShortNumberUtilTest(unittest.TestCase):
    """Unit tests for shortnumberutil.py"""

    def setUp(self):
        insert_test_metadata()

    def tearDown(self):
        reinstate_real_metadata()

    def testConnectsToEmergencyNumber_US(self):
        self.assertTrue(connects_to_emergency_number("911", "US"))
        self.assertTrue(connects_to_emergency_number("119", "US"))
        self.assertFalse(connects_to_emergency_number("999", "US"))

    def testConnectsToEmergencyNumberLongNumber_US(self):
        self.assertTrue(connects_to_emergency_number("9116666666", "US"))
        self.assertTrue(connects_to_emergency_number("1196666666", "US"))
        self.assertFalse(connects_to_emergency_number("9996666666", "US"))

    def testConnectsToEmergencyNumberWithFormatting_US(self):
        self.assertTrue(connects_to_emergency_number("9-1-1", "US"))
        self.assertTrue(connects_to_emergency_number("1-1-9", "US"))
        self.assertFalse(connects_to_emergency_number("9-9-9", "US"))

    def testConnectsToEmergencyNumberWithPlusSign_US(self):
        self.assertFalse(connects_to_emergency_number("+911", "US"))
        self.assertFalse(connects_to_emergency_number(u"\uFF0B911", "US"))
        self.assertFalse(connects_to_emergency_number(" +911", "US"))
        self.assertFalse(connects_to_emergency_number("+119", "US"))
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
        self.assertTrue(is_emergency_number("119", "US"))
        self.assertFalse(is_emergency_number("999", "US"))

    def testIsEmergencyNumberLongNumber_US(self):
        self.assertFalse(is_emergency_number("9116666666", "US"))
        self.assertFalse(is_emergency_number("1196666666", "US"))
        self.assertFalse(is_emergency_number("9996666666", "US"))

    def testIsEmergencyNumberWithFormatting_US(self):
        self.assertTrue(is_emergency_number("9-1-1", "US"))
        self.assertTrue(is_emergency_number("*911", "US"))
        self.assertTrue(is_emergency_number("1-1-9", "US"))
        self.assertTrue(is_emergency_number("*119", "US"))
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
