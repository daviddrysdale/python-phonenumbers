#!/usr/bin/env python
"""Unit tests for carrier.py"""

# Based on original Java code:
#     java/carrier/test/com/google/i18n/phonenumbers/PhoneNumberToCarrierMapperTest.java
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

import unittest

from phonenumbers import PhoneNumber, FrozenPhoneNumber
from phonenumbers import carrier
from phonenumbers.carrier import name_for_number, name_for_valid_number, safe_display_name
from phonenumbers.util import u

# Allow override library carrier metadata with the test metadata.
REAL_CARRIER_DATA = carrier.CARRIER_DATA
REAL_CARRIER_LONGEST_PREFIX = carrier.CARRIER_LONGEST_PREFIX
from .testcarrierdata import CARRIER_DATA as TEST_CARRIER_DATA
from .testcarrierdata import CARRIER_LONGEST_PREFIX as TEST_CARRIER_LONGEST_PREFIX


def reinstate_real_carrierdata():
    """Reinstate real phone number carrier metadata"""
    carrier.CARRIER_DATA = REAL_CARRIER_DATA
    carrier.CARRIER_LONGEST_PREFIX = REAL_CARRIER_LONGEST_PREFIX


def insert_test_carrierdata():
    """Insert test carrier metadata into library"""
    carrier.CARRIER_DATA = TEST_CARRIER_DATA
    carrier.CARRIER_LONGEST_PREFIX = TEST_CARRIER_LONGEST_PREFIX


# Set up some test numbers to re-use.
AO_MOBILE1 = FrozenPhoneNumber(country_code=244, national_number=917654321)
AO_MOBILE2 = FrozenPhoneNumber(country_code=244, national_number=927654321)
AO_FIXED1 = FrozenPhoneNumber(country_code=244, national_number=22254321)
AO_FIXED2 = FrozenPhoneNumber(country_code=244, national_number=26254321)
AO_INVALID_NUMBER = FrozenPhoneNumber(country_code=244, national_number=101234)
UK_MOBILE1 = FrozenPhoneNumber(country_code=44, national_number=7387654321)
UK_MOBILE2 = FrozenPhoneNumber(country_code=44, national_number=7487654321)
UK_FIXED1 = FrozenPhoneNumber(country_code=44, national_number=1123456789)
UK_FIXED2 = FrozenPhoneNumber(country_code=44, national_number=2987654321)
UK_INVALID_NUMBER = FrozenPhoneNumber(country_code=44, national_number=7301234)
UK_PAGER = FrozenPhoneNumber(country_code=44, national_number=7601234567)
US_FIXED_OR_MOBILE = FrozenPhoneNumber(country_code=1, national_number=6502123456)
NUMBER_WITH_INVALID_COUNTRY_CODE = FrozenPhoneNumber(country_code=999, national_number=2423651234)
INTERNATIONAL_TOLL_FREE = FrozenPhoneNumber(country_code=800, national_number=12345678)

# Language/country codes
_ENGLISH = "en"
_FRENCH = "fr"


class PhoneNumberToCarrierMapperTest(unittest.TestCase):
    """Unit tests for carrier.py"""

    def setUp(self):
        insert_test_carrierdata()

    def tearDown(self):
        reinstate_real_carrierdata()

    def testGetDescriptionForMobilePortableRegion(self):
        self.assertEqual("British carrier", name_for_number(UK_MOBILE1, _ENGLISH))
        self.assertEqual(u("Brittisk operat\u00F6r"), name_for_number(UK_MOBILE1, "sv", region="SE"))
        self.assertEqual("British carrier", name_for_number(UK_MOBILE1, _FRENCH))
        # Returns an empty string because the UK implements mobile number portability.
        self.assertEqual("", safe_display_name(UK_MOBILE1, _ENGLISH))

    def testGetDescriptionForNonMobilePortableRegion(self):
        self.assertEqual("Angolan carrier", name_for_number(AO_MOBILE1, _ENGLISH))
        self.assertEqual("Angolan carrier", safe_display_name(AO_MOBILE1, _ENGLISH))

    def testGetDescriptionForFixedLineNumber(self):
        self.assertEqual("", name_for_number(AO_FIXED1, _ENGLISH))
        self.assertEqual("", name_for_number(UK_FIXED1, _ENGLISH))
        # If the carrier information is present in the files and the method
        # that assumes a valid number is used, a carrier is returned.
        self.assertEqual("Angolan fixed line carrier", name_for_valid_number(AO_FIXED2, _ENGLISH))
        self.assertEqual("", name_for_valid_number(UK_FIXED2, _ENGLISH))

    def testGetDescriptionForFixedOrMobileNumber(self):
        self.assertEqual("US carrier", name_for_number(US_FIXED_OR_MOBILE, _ENGLISH))

    def testGetDescriptionForPagerNumber(self):
        self.assertEqual("British pager", name_for_number(UK_PAGER, _ENGLISH))

    def testGetDescriptionForNumberWithNoDataFile(self):
        self.assertEqual("", name_for_number(NUMBER_WITH_INVALID_COUNTRY_CODE, _ENGLISH))
        self.assertEqual("", name_for_number(INTERNATIONAL_TOLL_FREE, _ENGLISH))
        self.assertEqual("", name_for_valid_number(NUMBER_WITH_INVALID_COUNTRY_CODE, _ENGLISH))
        self.assertEqual("", name_for_valid_number(INTERNATIONAL_TOLL_FREE, _ENGLISH))

    def testGetDescriptionForNumberWithMissingPrefix(self):
        self.assertEqual("", name_for_number(UK_MOBILE2, _ENGLISH))
        self.assertEqual("", name_for_number(AO_MOBILE2, _ENGLISH))

    def testGetDescriptionForInvalidNumber(self):
        self.assertEqual("", name_for_number(UK_INVALID_NUMBER, _ENGLISH))
        self.assertEqual("", name_for_number(AO_INVALID_NUMBER, _ENGLISH))
