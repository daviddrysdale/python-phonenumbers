#!/usr/bin/env python
"""Unit tests for timezone.py"""

# Based on original Java code:
#     java/geocoder/test/com/google/i18n/phonenumbers/geocoding/PhoneNumberToTimeZonesMapperTest.java
# Copyright (C) 2012 The Libphonenumber Authors
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
from phonenumbers import timezone
from phonenumbers.timezone import time_zones_for_geographical_number
from phonenumbers.timezone import time_zones_for_number
from phonenumbers.timezone import _UNKNOWN_TIME_ZONE_LIST

# Allow override library timezone metadata with the test metadata.
REAL_TIMEZONE_DATA = timezone.TIMEZONE_DATA
REAL_TIMEZONE_LONGEST_PREFIX = timezone.TIMEZONE_LONGEST_PREFIX
from .testtzdata import TIMEZONE_DATA as TEST_TIMEZONE_DATA
from .testtzdata import TIMEZONE_LONGEST_PREFIX as TEST_TIMEZONE_LONGEST_PREFIX


def reinstate_real_tzdata():
    """Reinstate real phone number timezone metadata"""
    timezone.TIMEZONE_DATA = REAL_TIMEZONE_DATA
    timezone.TIMEZONE_LONGEST_PREFIX = REAL_TIMEZONE_LONGEST_PREFIX


def insert_test_tzdata():
    """Insert test timezone metadata into library"""
    timezone.TIMEZONE_DATA = TEST_TIMEZONE_DATA
    timezone.TIMEZONE_LONGEST_PREFIX = TEST_TIMEZONE_LONGEST_PREFIX


# Set up some test numbers to re-use.
AU_NUMBER = FrozenPhoneNumber(country_code=61, national_number=236618300)
CA_NUMBER = FrozenPhoneNumber(country_code=1, national_number=6048406565)
KO_NUMBER = FrozenPhoneNumber(country_code=82, national_number=22123456)
KO_INVALID_NUMBER = FrozenPhoneNumber(country_code=82, national_number=1234)
US_NUMBER1 = FrozenPhoneNumber(country_code=1, national_number=6509600000)
US_NUMBER2 = FrozenPhoneNumber(country_code=1, national_number=2128120000)
US_NUMBER3 = FrozenPhoneNumber(country_code=1, national_number=6174240000)
US_INVALID_NUMBER = FrozenPhoneNumber(country_code=1, national_number=123456789)
NUMBER_WITH_INVALID_COUNTRY_CODE = FrozenPhoneNumber(country_code=999, national_number=2423651234)
INTERNATIONAL_TOLL_FREE = FrozenPhoneNumber(country_code=800, national_number=12345678)

# NANPA time zones.
_CHICAGO_TZ = "America/Chicago"
_LOS_ANGELES_TZ = "America/Los_Angeles"
_NEW_YORK_TZ = "America/New_York"
_WINNIPEG_TZ = "America/Winnipeg"
_NANPA_TZ_LIST = (_NEW_YORK_TZ, _CHICAGO_TZ, _WINNIPEG_TZ, _LOS_ANGELES_TZ)

# Non NANPA time zones.
_SEOUL_TZ = "Asia/Seoul"
_SYDNEY_TZ = "Australia/Sydney"


class PhoneNumberToTimeZonesMapperTest(unittest.TestCase):
    """Unit tests for timezone.py"""

    def setUp(self):
        insert_test_tzdata()

    def tearDown(self):
        reinstate_real_tzdata()

    def testGetTimeZonesForNumber(self):
        # Test with invalid numbers even when their country code prefixes exist in the mapper.
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_number(US_INVALID_NUMBER))
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_number(KO_INVALID_NUMBER))
        # Test with valid prefixes.
        self.assertEqual((_SYDNEY_TZ,), time_zones_for_number(AU_NUMBER))
        self.assertEqual((_SEOUL_TZ,), time_zones_for_number(KO_NUMBER))
        self.assertEqual((_WINNIPEG_TZ,), time_zones_for_number(CA_NUMBER))
        self.assertEqual((_LOS_ANGELES_TZ,), time_zones_for_number(US_NUMBER1))
        self.assertEqual((_NEW_YORK_TZ,), time_zones_for_number(US_NUMBER2))
        # Test with an invalid country code.
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_number(NUMBER_WITH_INVALID_COUNTRY_CODE))
        # Test with a non geographical phone number.
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_number(INTERNATIONAL_TOLL_FREE))
        # Python version extra test: check a number that can't geocoded; falls back to per-country
        kr_mobile_number = FrozenPhoneNumber(country_code=82, national_number=801234567)
        self.assertEqual((_SEOUL_TZ,), time_zones_for_number(kr_mobile_number))

    def testGetTimeZonesForValidNumber(self):
        # Test with invalid numbers even when their country code prefixes exist in the mapper.
        self.assertEqual(_NANPA_TZ_LIST, time_zones_for_geographical_number(US_INVALID_NUMBER))
        self.assertEqual((_SEOUL_TZ,), time_zones_for_geographical_number(KO_INVALID_NUMBER))
        # Test with valid prefixes.
        self.assertEqual((_SYDNEY_TZ,), time_zones_for_geographical_number(AU_NUMBER))
        self.assertEqual((_SEOUL_TZ,), time_zones_for_geographical_number(KO_NUMBER))
        self.assertEqual((_WINNIPEG_TZ,), time_zones_for_geographical_number(CA_NUMBER))
        self.assertEqual((_LOS_ANGELES_TZ,), time_zones_for_geographical_number(US_NUMBER1))
        self.assertEqual((_NEW_YORK_TZ,), time_zones_for_geographical_number(US_NUMBER2))
        # Test with an invalid country code.
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_geographical_number(NUMBER_WITH_INVALID_COUNTRY_CODE))
        # Test with a non geographical phone number.
        self.assertEqual(_UNKNOWN_TIME_ZONE_LIST, time_zones_for_geographical_number(INTERNATIONAL_TOLL_FREE))

    def testGetTimeZonesForValidNumberSearchingAtCountryCodeLevel(self):
        # Test that the country level time zones are returned when the number passed in is valid but
        # not covered by any non-country level prefixes in the mapper.
        self.assertEqual(time_zones_for_number(US_NUMBER3), _NANPA_TZ_LIST)
