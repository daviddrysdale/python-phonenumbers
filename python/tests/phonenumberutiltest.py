#!/usr/bin/env python
"""Unit tests for phonenumberutil.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/PhoneNumberUtilTest.java
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
import sys
import unittest

import phonenumbers
from phonenumbers import PhoneNumber, PhoneMetadata
from phonenumbers import FrozenPhoneNumber, PhoneNumberDesc
from phonenumbers import PhoneNumberType, PhoneNumberFormat, NumberParseException
from phonenumbers import ValidationResult, NumberFormat, CountryCodeSource
# Access internal functions of phonenumberutil.py
from phonenumbers import phonenumberutil

# Override library metadata with the test metadata.
REAL_REGION_METADATA = PhoneMetadata.region_metadata
REAL_CC_TO_RC = phonenumberutil.COUNTRY_CODE_TO_REGION_CODE

PhoneMetadata.region_metadata = {}
phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = {}

# Import the test data; this will re-populate the
# PhoneMetadata.region_metadata map
from .testdata import _COUNTRY_CODE_TO_REGION_CODE as TEST_CC_TO_RC
TEST_REGION_METADATA = PhoneMetadata.region_metadata

if sys.version_info >= (3, 0):
    # Python 3 has unlimited-precision int, so no 'L' suffix
    _LS = ''
    # Python 3 has all strings unicode, so no 'u' prefix
    _UP = ''
else:
    _LS = 'L'
    _UP = 'u'


def reinstate_real_metadata():
    """Reinstate real phone number metadata"""
    phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = REAL_CC_TO_RC
    PhoneMetadata.region_metadata = REAL_REGION_METADATA


def insert_test_metadata():
    """Insert test metadata into library"""
    phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = TEST_CC_TO_RC
    PhoneMetadata.region_metadata = TEST_REGION_METADATA

# Reinstate the real metadata so any importers of this module are not affected
reinstate_real_metadata()

# Set up some test numbers to re-use.
ALPHA_NUMERIC_NUMBER = FrozenPhoneNumber(country_code=1, national_number=80074935247L)
AR_MOBILE = FrozenPhoneNumber(country_code=54, national_number=91187654321L)
AR_NUMBER = FrozenPhoneNumber(country_code=54, national_number=1187654321)
AU_NUMBER = FrozenPhoneNumber(country_code=61, national_number=236618300L)
BS_MOBILE = FrozenPhoneNumber(country_code=1, national_number=2423570000L)
BS_NUMBER = FrozenPhoneNumber(country_code=1, national_number=2423651234L)
# Note that this is the same as the example number for DE in the metadata.
DE_NUMBER = FrozenPhoneNumber(country_code=49, national_number=30123456L)
DE_SHORT_NUMBER = FrozenPhoneNumber(country_code=49, national_number=1234L)
GB_MOBILE = FrozenPhoneNumber(country_code=44, national_number=7912345678L)
GB_NUMBER = FrozenPhoneNumber(country_code=44, national_number=2070313000L)
IT_MOBILE = FrozenPhoneNumber(country_code=39, national_number=345678901L)
IT_NUMBER = FrozenPhoneNumber(country_code=39, national_number=236618300L, italian_leading_zero=True)
JP_STAR_NUMBER = FrozenPhoneNumber(country_code=81, national_number=2345L)
# Numbers to test the formatting rules from Mexico.
MX_MOBILE1 = FrozenPhoneNumber(country_code=52, national_number=12345678900L)
MX_MOBILE2 = FrozenPhoneNumber(country_code=52, national_number=15512345678L)
MX_NUMBER1 = FrozenPhoneNumber(country_code=52, national_number=3312345678L)
MX_NUMBER2 = FrozenPhoneNumber(country_code=52, national_number=8211234567L)
NZ_NUMBER = FrozenPhoneNumber(country_code=64, national_number=33316005L)
SG_NUMBER = FrozenPhoneNumber(country_code=65, national_number=65218000L)
# A too-long and hence invalid US number.
US_LONG_NUMBER = FrozenPhoneNumber(country_code=1, national_number=65025300001L)
US_NUMBER = FrozenPhoneNumber(country_code=1, national_number=6502530000L)
US_PREMIUM = FrozenPhoneNumber(country_code=1, national_number=9002530000L)
# Too short, but still possible US numbers.
US_LOCAL_NUMBER = FrozenPhoneNumber(country_code=1, national_number=2530000L)
US_SHORT_BY_ONE_NUMBER = FrozenPhoneNumber(country_code=1, national_number=650253000L)
US_TOLLFREE = FrozenPhoneNumber(country_code=1, national_number=8002530000L)
US_SPOOF = FrozenPhoneNumber(country_code=1, national_number=0L)
US_SPOOF_WITH_RAW_INPUT = FrozenPhoneNumber(country_code=1, national_number=0L, raw_input="000-000-0000")
INTERNATIONAL_TOLL_FREE = FrozenPhoneNumber(country_code=800, national_number=12345678L)
INTERNATIONAL_TOLL_FREE_TOO_LONG = FrozenPhoneNumber(country_code=800, national_number=1234567890L)
# A number with an invalid region code
XY_NUMBER = FrozenPhoneNumber(country_code=999, national_number=1234567890L)


class PhoneNumberUtilTest(unittest.TestCase):
    """Unit tests for phonenumbers/__init__.py

    Note that these tests use the metadata contained in the files in
    tests/data, not the normal metadata files, so should not be used for
    regression test purposes - these tests are illustrative only and test
    functionality.
    """
    def setUp(self):
        insert_test_metadata()

    def tearDown(self):
        reinstate_real_metadata()

    def testSupportedRegions(self):
        self.assertTrue(len(phonenumbers.SUPPORTED_REGIONS) > 0)
        # Python version extra test
        # Check the pseudo-code for non-geographic entities is not supported
        self.assertFalse("001" in phonenumbers.SUPPORTED_REGIONS)
        # Check a non-US NANPA country is correctly listed as supported
        self.assertTrue("BS" in phonenumbers.SUPPORTED_REGIONS)

    def testGetInstanceLoadUSMetadata(self):
        metadata = PhoneMetadata.region_metadata["US"]
        self.assertEqual("US", metadata.id)
        self.assertEqual(1, metadata.country_code)
        self.assertEqual("011", metadata.international_prefix)
        self.assertTrue(metadata.national_prefix is not None)
        self.assertEqual(2, len(metadata.number_format))
        self.assertEqual("(\\d{3})(\\d{3})(\\d{4})", metadata.number_format[1].pattern)
        self.assertEqual("\\1 \\2 \\3", metadata.number_format[1].format)
        self.assertEqual("[13-689]\\d{9}|2[0-35-9]\\d{8}",
                         metadata.general_desc.national_number_pattern)
        self.assertEqual("\\d{7}(?:\\d{3})?", metadata.general_desc.possible_number_pattern)
        self.assertTrue(metadata.general_desc == metadata.fixed_line)
        self.assertEqual("\\d{10}", metadata.toll_free.possible_number_pattern)
        self.assertEqual("900\\d{7}", metadata.premium_rate.national_number_pattern)
        # No shared-cost data is available, so it should be initialised to "NA".
        self.assertEqual("NA", metadata.shared_cost.national_number_pattern)
        self.assertEqual("NA", metadata.shared_cost.possible_number_pattern)

    def testGetInstanceLoadDEMetadata(self):
        metadata = PhoneMetadata.region_metadata["DE"]
        self.assertEqual("DE", metadata.id)
        self.assertEqual(49, metadata.country_code)
        self.assertEqual("00", metadata.international_prefix)
        self.assertEqual("0", metadata.national_prefix)
        self.assertEqual(6, len(metadata.number_format))
        self.assertEqual(1, len(metadata.number_format[5].leading_digits_pattern))
        self.assertEqual("900", metadata.number_format[5].leading_digits_pattern[0])
        self.assertEqual("(\\d{3})(\\d{3,4})(\\d{4})",
                         metadata.number_format[5].pattern)
        self.assertEqual("\\1 \\2 \\3", metadata.number_format[5].format)
        self.assertEqual("(?:[24-6]\\d{2}|3[03-9]\\d|[789](?:[1-9]\\d|0[2-9]))\\d{1,8}",
                         metadata.fixed_line.national_number_pattern)
        self.assertEqual("\\d{2,14}", metadata.fixed_line.possible_number_pattern)
        self.assertEqual("30123456", metadata.fixed_line.example_number)
        self.assertEqual("\\d{10}", metadata.toll_free.possible_number_pattern)
        self.assertEqual("900([135]\\d{6}|9\\d{7})", metadata.premium_rate.national_number_pattern)

    def testGetInstanceLoadARMetadata(self):
        metadata = PhoneMetadata.region_metadata["AR"]
        self.assertEqual("AR", metadata.id)
        self.assertEqual(54, metadata.country_code)
        self.assertEqual("00", metadata.international_prefix)
        self.assertEqual("0", metadata.national_prefix)
        self.assertEqual("0(?:(11|343|3715)15)?", metadata.national_prefix_for_parsing)
        self.assertEqual("9\\1", metadata.national_prefix_transform_rule)
        self.assertEqual("\\2 15 \\3-\\4", metadata.number_format[2].format)
        self.assertEqual("(9)(\\d{4})(\\d{2})(\\d{4})",
                         metadata.number_format[3].pattern)
        self.assertEqual("(9)(\\d{4})(\\d{2})(\\d{4})",
                         metadata.intl_number_format[3].pattern)
        self.assertEqual("\\1 \\2 \\3 \\4", metadata.intl_number_format[3].format)

    def testGetInstanceLoadInternationalTollFreeMetadata(self):
        metadata = PhoneMetadata.country_code_metadata[800]
        self.assertEqual("001", metadata.id)
        self.assertEqual(800, metadata.country_code)
        self.assertEqual("\\1 \\2", metadata.number_format[0].format)
        self.assertEqual("(\\d{4})(\\d{4})", metadata.number_format[0].pattern)
        self.assertEqual("12345678", metadata.general_desc.example_number)
        self.assertEqual("12345678", metadata.toll_free.example_number)

    def testIsLeadingZeroPossible(self):
        self.assertTrue(phonenumberutil._is_leading_zero_possible(39))  # Italy
        self.assertFalse(phonenumberutil._is_leading_zero_possible(1))  # USA
        self.assertFalse(phonenumberutil._is_leading_zero_possible(800))
        self.assertFalse(phonenumberutil._is_leading_zero_possible(888))  # Not in metadata file, just default to False

    def testGetLengthOfGeographicalAreaCode(self):
        # Google MTV, which has area code "650".
        self.assertEqual(3, phonenumbers.length_of_geographical_area_code(US_NUMBER))
        # A North America toll-free number, which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(US_TOLLFREE))
        # Google London, which has area code "20".
        self.assertEqual(2, phonenumbers.length_of_geographical_area_code(GB_NUMBER))
        # A UK mobile phone, which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(GB_MOBILE))
        # Google Buenos Aires, which has area code "11".
        self.assertEqual(2, phonenumbers.length_of_geographical_area_code(AR_NUMBER))
        # Google Sydney, which has area code "2".
        self.assertEqual(1, phonenumbers.length_of_geographical_area_code(AU_NUMBER))
        # Google Singapore. Singapore has no area code and no national prefix.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(SG_NUMBER))
        # An invalid US number (1 digit shorter), which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(US_SHORT_BY_ONE_NUMBER))
        # An international toll free number, which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(INTERNATIONAL_TOLL_FREE))

    def testGetLengthOfNationalDestinationCode(self):
        # Google MTV, which has national destination code (NDC) "650".
        self.assertEqual(3, phonenumbers.length_of_national_destination_code(US_NUMBER))

        # A North America toll-free number, which has NDC "800".
        self.assertEqual(3, phonenumbers.length_of_national_destination_code(US_TOLLFREE))

        # Google London, which has NDC "20".
        self.assertEqual(2, phonenumbers.length_of_national_destination_code(GB_NUMBER))

        # A UK mobile phone, which has NDC "7912".
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(GB_MOBILE))

        # Google Buenos Aires, which has NDC "11".
        self.assertEqual(2, phonenumbers.length_of_national_destination_code(AR_NUMBER))

        # An Argentinian mobile which has NDC "911".
        self.assertEqual(3, phonenumbers.length_of_national_destination_code(AR_MOBILE))

        # Google Sydney, which has NDC "2".
        self.assertEqual(1, phonenumbers.length_of_national_destination_code(AU_NUMBER))

        # Google Singapore, which has NDC "6521".
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(SG_NUMBER))

        # An invalid US number (1 digit shorter), which has no NDC.
        self.assertEqual(0, phonenumbers.length_of_national_destination_code(US_SHORT_BY_ONE_NUMBER))

        # A number containing an invalid country calling code, which shouldn't have any NDC.
        number = PhoneNumber(country_code=123, national_number=6502530000L)
        self.assertEqual(0, phonenumbers.length_of_national_destination_code(number))

        # An international toll free number, which has NDC "1234".
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(INTERNATIONAL_TOLL_FREE))

        # Python version extra test
        # A number with an extension; still has NDC "7912"
        number2 = PhoneNumber()
        number2.merge_from(GB_MOBILE)
        number2.extension = "1234"
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(number2))

    def testGetNationalSignificantNumber(self):
        self.assertEqual("6502530000", phonenumbers.national_significant_number(US_NUMBER))
        # An Italian mobile number.
        self.assertEqual("345678901", phonenumbers.national_significant_number(IT_MOBILE))

        # An Italian fixed line number.
        self.assertEqual("0236618300", phonenumbers.national_significant_number(IT_NUMBER))

        self.assertEqual("12345678", phonenumbers.national_significant_number(INTERNATIONAL_TOLL_FREE))

    def testGetExampleNumber(self):
        self.assertEqual(DE_NUMBER, phonenumbers.example_number("DE"))
        self.assertEqual(DE_NUMBER,
                         phonenumbers.example_number_for_type("DE", PhoneNumberType.FIXED_LINE))
        self.assertEqual(None,
                         phonenumbers.example_number_for_type("DE", PhoneNumberType.MOBILE))
        # For the US, the example number is placed under general description,
        # and hence should be used for both fixed line and mobile, so neither
        # of these should return None.
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.FIXED_LINE) is not None)
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.MOBILE) is not None)
        # CS is an invalid region, so we have no data for it.
        self.assertTrue(phonenumbers.example_number_for_type("CS", PhoneNumberType.MOBILE) is None)
        # Python version extra test
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.UNKNOWN) is not None)

        # RegionCode 001 is reserved for supporting non-geographical country
        # calling code. We don't support getting an example number for it with
        # this method.
        self.assertTrue(phonenumbers.example_number("001") is None)

    def testGetExampleNumberForNonGeoEntity(self):
        self.assertEqual(INTERNATIONAL_TOLL_FREE, phonenumbers.example_number_for_non_geo_entity(800))

    def testConvertAlphaCharactersInNumber(self):
        input = "1800-ABC-DEF"
        # Alpha chars are converted to digits; everything else is left untouched.
        expectedOutput = "1800-222-333"
        self.assertEqual(expectedOutput, phonenumberutil.convert_alpha_characters_in_number(input))

    def testNormaliseRemovePunctuation(self):
        inputNumber = "034-56&+#234"
        expectedOutput = "03456234"
        self.assertEqual(expectedOutput,
                         phonenumberutil._normalize(inputNumber),
                         msg="Conversion did not correctly remove punctuation")

    def testNormaliseReplaceAlphaCharacters(self):
        inputNumber = "034-I-am-HUNGRY"
        expectedOutput = "034426486479"
        self.assertEqual(expectedOutput,
                         phonenumberutil._normalize(inputNumber),
                         msg="Conversion did not correctly replace alpha characters")

    def testNormaliseOtherDigits(self):
        inputNumber = u"\uFF125\u0665"
        expectedOutput = "255"
        self.assertEqual(expectedOutput,
                         phonenumberutil._normalize(inputNumber),
                         msg="Conversion did not correctly replace non-latin digits")
        # Eastern-Arabic digits.
        inputNumber = u"\u06F52\u06F0"
        expectedOutput = "520"
        self.assertEqual(expectedOutput,
                         phonenumberutil._normalize(inputNumber),
                         msg="Conversion did not correctly replace non-latin digits")

    def testNormaliseStripAlphaCharacters(self):
        inputNumber = "034-56&+a#234"
        expectedOutput = "03456234"
        self.assertEqual(expectedOutput,
                         phonenumbers.normalize_digits_only(inputNumber),
                         msg="Conversion did not correctly remove alpha character")

    def testFormatUSNumber(self):
        self.assertEqual("650 253 0000", phonenumbers.format_number(US_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 650 253 0000", phonenumbers.format_number(US_NUMBER, PhoneNumberFormat.INTERNATIONAL))

        self.assertEqual("800 253 0000", phonenumbers.format_number(US_TOLLFREE, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 800 253 0000", phonenumbers.format_number(US_TOLLFREE, PhoneNumberFormat.INTERNATIONAL))

        self.assertEqual("900 253 0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 900 253 0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+1-900-253-0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.RFC3966))
        # Numbers with all zeros in the national number part will be formatted by using the raw_input
        # if that is available no matter which format is specified.
        self.assertEqual("000-000-0000",
                         phonenumbers.format_number(US_SPOOF_WITH_RAW_INPUT, PhoneNumberFormat.NATIONAL))
        self.assertEqual("0", phonenumbers.format_number(US_SPOOF, PhoneNumberFormat.NATIONAL))

    def testFormatBSNumber(self):
        self.assertEqual("242 365 1234", phonenumbers.format_number(BS_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 242 365 1234", phonenumbers.format_number(BS_NUMBER, PhoneNumberFormat.INTERNATIONAL))

    def testFormatGBNumber(self):
        self.assertEqual("(020) 7031 3000", phonenumbers.format_number(GB_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+44 20 7031 3000", phonenumbers.format_number(GB_NUMBER, PhoneNumberFormat.INTERNATIONAL))

        self.assertEqual("(07912) 345 678", phonenumbers.format_number(GB_MOBILE, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+44 7912 345 678", phonenumbers.format_number(GB_MOBILE, PhoneNumberFormat.INTERNATIONAL))

    def testFormatDENumber(self):
        deNumber = PhoneNumber(country_code=49, national_number=301234L)
        self.assertEqual("030/1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 30/1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+49-30-1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.RFC3966))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = 291123L
        self.assertEqual("0291 123", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 291 123", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = 29112345678L
        self.assertEqual("0291 12345678", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 291 12345678", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = 912312345L
        self.assertEqual("09123 12345", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 9123 12345", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))
        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = 80212345L
        self.assertEqual("08021 2345", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 8021 2345", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))
        # Note this number is correctly formatted without national prefix. Most of the numbers that
        # are treated as invalid numbers by the library are short numbers, and they are usually not
        # dialed with national prefix.
        self.assertEqual("1234", phonenumbers.format_number(DE_SHORT_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 1234", phonenumbers.format_number(DE_SHORT_NUMBER, PhoneNumberFormat.INTERNATIONAL))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = 41341234
        self.assertEqual("04134 1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))

    def testFormatITNumber(self):
        self.assertEqual("02 3661 8300", phonenumbers.format_number(IT_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+39 02 3661 8300", phonenumbers.format_number(IT_NUMBER, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+390236618300", phonenumbers.format_number(IT_NUMBER, PhoneNumberFormat.E164))

        self.assertEqual("345 678 901", phonenumbers.format_number(IT_MOBILE, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+39 345 678 901", phonenumbers.format_number(IT_MOBILE, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+39345678901", phonenumbers.format_number(IT_MOBILE, PhoneNumberFormat.E164))

    def testFormatAUNumber(self):
        self.assertEqual("02 3661 8300", phonenumbers.format_number(AU_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+61 2 3661 8300", phonenumbers.format_number(AU_NUMBER, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+61236618300", phonenumbers.format_number(AU_NUMBER, PhoneNumberFormat.E164))

        auNumber = PhoneNumber(country_code=61, national_number=1800123456L)
        self.assertEqual("1800 123 456", phonenumbers.format_number(auNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+61 1800 123 456", phonenumbers.format_number(auNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+611800123456", phonenumbers.format_number(auNumber, PhoneNumberFormat.E164))

    def testFormatARNumber(self):
        self.assertEqual("011 8765-4321", phonenumbers.format_number(AR_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+54 11 8765-4321", phonenumbers.format_number(AR_NUMBER, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+541187654321", phonenumbers.format_number(AR_NUMBER, PhoneNumberFormat.E164))

        self.assertEqual("011 15 8765-4321", phonenumbers.format_number(AR_MOBILE, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+54 9 11 8765 4321", phonenumbers.format_number(AR_MOBILE, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+5491187654321", phonenumbers.format_number(AR_MOBILE, PhoneNumberFormat.E164))

    def testFormatMXNumber(self):
        self.assertEqual("045 234 567 8900", phonenumbers.format_number(MX_MOBILE1, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+52 1 234 567 8900", phonenumbers.format_number(MX_MOBILE1, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+5212345678900", phonenumbers.format_number(MX_MOBILE1, PhoneNumberFormat.E164))

        self.assertEqual("045 55 1234 5678", phonenumbers.format_number(MX_MOBILE2, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+52 1 55 1234 5678", phonenumbers.format_number(MX_MOBILE2, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+5215512345678", phonenumbers.format_number(MX_MOBILE2, PhoneNumberFormat.E164))

        self.assertEqual("01 33 1234 5678", phonenumbers.format_number(MX_NUMBER1, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+52 33 1234 5678", phonenumbers.format_number(MX_NUMBER1, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+523312345678", phonenumbers.format_number(MX_NUMBER1, PhoneNumberFormat.E164))

        self.assertEqual("01 821 123 4567", phonenumbers.format_number(MX_NUMBER2, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+52 821 123 4567", phonenumbers.format_number(MX_NUMBER2, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+528211234567", phonenumbers.format_number(MX_NUMBER2, PhoneNumberFormat.E164))

    def testFormatOutOfCountryCallingNumber(self):
        self.assertEqual("00 1 900 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_PREMIUM, "DE"))
        self.assertEqual("1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "BS"))
        self.assertEqual("00 1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "PL"))
        self.assertEqual("011 44 7912 345 678",
                         phonenumbers.format_out_of_country_calling_number(GB_MOBILE, "US"))
        self.assertEqual("00 49 1234",
                         phonenumbers.format_out_of_country_calling_number(DE_SHORT_NUMBER, "GB"))
        # Note this number is correctly formatted without national
        # prefix. Most of the numbers that are treated as invalid numbers by
        # the library are short numbers, and they are usually not dialed with
        # national prefix.
        self.assertEqual("1234", phonenumbers.format_out_of_country_calling_number(DE_SHORT_NUMBER, "DE"))
        self.assertEqual("011 39 02 3661 8300",
                         phonenumbers.format_out_of_country_calling_number(IT_NUMBER, "US"))
        self.assertEqual("02 3661 8300",
                         phonenumbers.format_out_of_country_calling_number(IT_NUMBER, "IT"))
        self.assertEqual("+39 02 3661 8300",
                         phonenumbers.format_out_of_country_calling_number(IT_NUMBER, "SG"))
        self.assertEqual("6521 8000",
                         phonenumbers.format_out_of_country_calling_number(SG_NUMBER, "SG"))
        self.assertEqual("011 54 9 11 8765 4321",
                         phonenumbers.format_out_of_country_calling_number(AR_MOBILE, "US"))
        self.assertEqual("011 800 1234 5678",
                         phonenumbers.format_out_of_country_calling_number(INTERNATIONAL_TOLL_FREE, "US"))

        arNumberWithExtn = PhoneNumber()
        arNumberWithExtn.merge_from(AR_MOBILE)
        arNumberWithExtn.extension = "1234"
        self.assertEqual("011 54 9 11 8765 4321 ext. 1234",
                         phonenumbers.format_out_of_country_calling_number(arNumberWithExtn, "US"))
        self.assertEqual("0011 54 9 11 8765 4321 ext. 1234",
                         phonenumbers.format_out_of_country_calling_number(arNumberWithExtn, "AU"))
        self.assertEqual("011 15 8765-4321 ext. 1234",
                         phonenumbers.format_out_of_country_calling_number(arNumberWithExtn, "AR"))
        # Python version extra tests
        self.assertEqual("1234567890",
                         phonenumbers.format_out_of_country_calling_number(XY_NUMBER, "AR"))
        self.assertEqual("1234567890",
                         phonenumbers.format_out_of_country_calling_number(XY_NUMBER, "XX"))

    def testFormatOutOfCountryWithInvalidRegion(self):
        # AQ/Antarctica isn't a valid region code for phone number formatting,
        # so this falls back to intl formatting.
        self.assertEqual("+1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "AQ"))
        # For region code 001, the out-of-country format always turns into the
        # international format.
        self.assertEqual("+1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "001"))

    def testFormatOutOfCountryWithPreferredIntlPrefix(self):
        # This should use 0011, since that is the preferred international
        # prefix (both 0011 and 0012 are accepted as possible international
        # prefixes in our test metadta.)
        self.assertEqual("0011 39 02 3661 8300",
                         phonenumbers.format_out_of_country_calling_number(IT_NUMBER, "AU"))
        # For region code 001, the out-of-country format always turns into the international format.
        self.assertEqual("+1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "001"))

    def testFormatOutOfCountryKeepingAlphaChars(self):
        alphaNumericNumber = PhoneNumber(country_code=1, national_number=8007493524L)
        alphaNumericNumber.raw_input = "1800 six-flag"
        self.assertEqual("0011 1 800 SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.raw_input = "1-800-SIX-flag"
        self.assertEqual("0011 1 800-SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.raw_input = "Call us from UK: 00 1 800 SIX-flag"
        self.assertEqual("0011 1 800 SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.raw_input = "800 SIX-flag"
        self.assertEqual("0011 1 800 SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        # Formatting from within the NANPA region.
        self.assertEqual("1 800 SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "US"))

        self.assertEqual("1 800 SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "BS"))

        # Testing that if the raw input doesn't exist, it is formatted using
        # formatOutOfCountryCallingNumber.
        alphaNumericNumber.raw_input = None
        self.assertEqual("00 1 800 749 3524",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "DE"))

        # Testing AU alpha number formatted from Australia.
        alphaNumericNumber.country_code = 61
        alphaNumericNumber.national_number = 827493524L
        alphaNumericNumber.raw_input = "+61 82749-FLAG"
        # This number should have the national prefix fixed.
        self.assertEqual("082749-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.raw_input = "082749-FLAG"
        self.assertEqual("082749-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.national_number = 18007493524L
        alphaNumericNumber.raw_input = "1-800-SIX-flag"
        # This number should not have the national prefix prefixed, in
        # accordance with the override for this specific formatting rule.
        self.assertEqual("1-800-SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        # The metadata should not be permanently changed, since we copied it
        # before modifying patterns.  Here we check this.
        alphaNumericNumber.national_number = 1800749352L
        self.assertEqual("1800 749 352",
                         phonenumbers.format_out_of_country_calling_number(alphaNumericNumber, "AU"))

        # Testing a region with multiple international prefixes.
        self.assertEqual("+61 1-800-SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "SG"))
        # Testing the case of calling from a non-supported region.
        self.assertEqual("+61 1-800-SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AQ"))

        # Testing the case with an invalid country calling code.
        alphaNumericNumber.country_code = 0
        alphaNumericNumber.national_number = 18007493524L
        alphaNumericNumber.raw_input = "1-800-SIX-flag"
        # Uses the raw input only.
        self.assertEqual("1-800-SIX-flag",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "DE"))

        # Testing the case of an invalid alpha number.
        alphaNumericNumber.country_code = 1
        alphaNumericNumber.national_number = 80749L
        alphaNumericNumber.raw_input = "180-SIX"
        # No country-code stripping can be done.
        self.assertEqual("00 1 180-SIX",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "DE"))

        # Testing the case of calling from a non-supported region.
        alphaNumericNumber.country_code = 1
        alphaNumericNumber.national_number = 80749L
        alphaNumericNumber.raw_input = "180-SIX"
        # No country-code stripping can be done since the number is invalid.
        self.assertEqual("+1 180-SIX",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AQ"))

    def testFormatWithCarrierCode(self):
        # We only support this for AR in our test metadata, and only for mobile numbers starting with
        # certain values.
        arMobile = PhoneNumber(country_code=54, national_number=92234654321L)
        self.assertEqual("02234 65-4321", phonenumbers.format_number(arMobile, PhoneNumberFormat.NATIONAL))
        # Here we force 14 as the carrier code.
        self.assertEqual("02234 14 65-4321",
                         phonenumbers.format_national_number_with_carrier_code(arMobile, "14"))
        # Here we force the number to be shown with no carrier code.
        self.assertEqual("02234 65-4321",
                         phonenumbers.format_national_number_with_carrier_code(arMobile, ""))
        # Here the international rule is used, so no carrier code should be present.
        self.assertEqual("+5492234654321", phonenumbers.format_number(arMobile, PhoneNumberFormat.E164))
        # We don't support this for the US so there should be no change.
        self.assertEqual("650 253 0000", phonenumbers.format_national_number_with_carrier_code(US_NUMBER, "15"))
        # Python version extra test
        self.assertEqual("1234567890",
                         phonenumbers.format_national_number_with_carrier_code(XY_NUMBER, "123"))

    def testFormatWithPreferredCarrierCode(self):
        # We only support this for AR in our test metadata.
        arNumber = PhoneNumber()
        arNumber.country_code = 54
        arNumber.national_number = 91234125678L
        # Test formatting with no preferred carrier code stored in the number itself.
        self.assertEqual("01234 15 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, "15"))
        self.assertEqual("01234 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, ""))
        # Test formatting with preferred carrier code present.
        arNumber.preferred_domestic_carrier_code = "19"
        self.assertEqual("01234 12-5678", phonenumbers.format_number(arNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("01234 19 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, "15"))
        self.assertEqual("01234 19 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, ""))
        # Python version extra test: check string conversion with preferred carrier code
        self.assertEqual('Country Code: 54 National Number: 91234125678 '
                         'Leading Zero: False Preferred Domestic Carrier Code: 19',
                          str(arNumber))
        self.assertEqual("PhoneNumber(country_code=54, national_number=91234125678%s, extension=None, "
                         "italian_leading_zero=False, country_code_source=None, preferred_domestic_carrier_code='19')" % _LS,
                         repr(arNumber))
        # When the preferred_domestic_carrier_code is present (even when it
        # contains an empty string), use it instead of the default carrier
        # code passed in.
        arNumber.preferred_domestic_carrier_code = ""
        self.assertEqual("01234 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, "15"))
        # We don't support this for the US so there should be no change.
        usNumber = PhoneNumber(country_code=1, national_number=4241231234L, preferred_domestic_carrier_code="99")
        self.assertEqual("424 123 1234", phonenumbers.format_number(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("424 123 1234",
                         phonenumbers.format_national_number_with_preferred_carrier_code(usNumber, "15"))

    def testFormatNumberForMobileDialing(self):
        # US toll free numbers are marked as noInternationalDialling in the
        # test metadata for testing purposes.
        self.assertEqual("800 253 0000",
                         phonenumbers.format_number_for_mobile_dialing(US_TOLLFREE, "US",
                                                                       True))  # Keep formatting
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(US_TOLLFREE, "CN", True))
        self.assertEqual("+1 650 253 0000",
                         phonenumbers.format_number_for_mobile_dialing(US_NUMBER, "US", True))
        usNumberWithExtn = PhoneNumber()
        usNumberWithExtn.merge_from(US_NUMBER)
        usNumberWithExtn.extension = "1234"
        self.assertEqual("+1 650 253 0000",
                         phonenumbers.format_number_for_mobile_dialing(usNumberWithExtn, "US", True))
        self.assertEqual("8002530000",
                         phonenumbers.format_number_for_mobile_dialing(US_TOLLFREE, "US",
                                                                       False))  # Remove formatting
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(US_TOLLFREE, "CN", False))
        self.assertEqual("+16502530000",
                         phonenumbers.format_number_for_mobile_dialing(US_NUMBER, "US", False))
        self.assertEqual("+16502530000",
                         phonenumbers.format_number_for_mobile_dialing(usNumberWithExtn, "US", False))

        # An invalid US number, which is one digit too long.
        self.assertEqual("+165025300001",
                         phonenumbers.format_number_for_mobile_dialing(US_LONG_NUMBER, "US", False))
        self.assertEqual("+1 65025300001",
                         phonenumbers.format_number_for_mobile_dialing(US_LONG_NUMBER, "US", True))

        # Star numbers. In real life they appear in Israel, but we have them
        # in JP in our test metadata.
        self.assertEqual("*2345",
                         phonenumbers.format_number_for_mobile_dialing(JP_STAR_NUMBER, "JP", False))
        self.assertEqual("*2345",
                         phonenumbers.format_number_for_mobile_dialing(JP_STAR_NUMBER, "JP", True))

        # Python version extra tests
        number = PhoneNumber()
        number.merge_from(XY_NUMBER)
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(number, "US", False))
        number.raw_input = " 123-456-7890"
        self.assertEqual(" 123-456-7890", phonenumbers.format_number_for_mobile_dialing(number, "US", False))
        self.assertEqual("+80012345678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "JP", False))
        self.assertEqual("+800 1234 5678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "JP", True))

    def testFormatByPattern(self):
        newNumFormat = NumberFormat(pattern="(\\d{3})(\\d{3})(\\d{4})", format="(\\1) \\2-\\3")
        newNumberFormats = [newNumFormat]

        self.assertEqual("(650) 253-0000", phonenumbers.format_by_pattern(US_NUMBER, PhoneNumberFormat.NATIONAL,
                                                                          newNumberFormats))
        self.assertEqual("+1 (650) 253-0000", phonenumbers.format_by_pattern(US_NUMBER,
                                                                             PhoneNumberFormat.INTERNATIONAL,
                                                                             newNumberFormats))
        self.assertEqual("+1-650-253-0000", phonenumbers.format_by_pattern(US_NUMBER,
                                                                           PhoneNumberFormat.RFC3966,
                                                                           newNumberFormats))

        # $NP is set to '1' for the US. Here we check that for other NANPA
        # countries the US rules are followed.
        newNumFormat.national_prefix_formatting_rule = "$NP ($FG)"
        newNumFormat.format = "\\1 \\2-\\3"
        self.assertEqual("1 (242) 365-1234",
                         phonenumbers.format_by_pattern(BS_NUMBER, PhoneNumberFormat.NATIONAL,
                                                        newNumberFormats))
        self.assertEqual("+1 242 365-1234",
                         phonenumbers.format_by_pattern(BS_NUMBER, PhoneNumberFormat.INTERNATIONAL,
                                                        newNumberFormats))

        newNumFormat.pattern = "(\\d{2})(\\d{5})(\\d{3})"
        newNumFormat.format = "\\1-\\2 \\3"
        newNumberFormats[0] = newNumFormat

        self.assertEqual("02-36618 300",
                         phonenumbers.format_by_pattern(IT_NUMBER, PhoneNumberFormat.NATIONAL,
                                                        newNumberFormats))
        self.assertEqual("+39 02-36618 300",
                         phonenumbers.format_by_pattern(IT_NUMBER, PhoneNumberFormat.INTERNATIONAL,
                                                        newNumberFormats))

        newNumFormat.national_prefix_formatting_rule = "$NP$FG"
        newNumFormat.pattern = "(\\d{2})(\\d{4})(\\d{4})"
        newNumFormat.format = "\\1 \\2 \\3"
        newNumberFormats[0] = newNumFormat
        self.assertEqual("020 7031 3000",
                         phonenumbers.format_by_pattern(GB_NUMBER, PhoneNumberFormat.NATIONAL,
                                                        newNumberFormats))

        newNumFormat.national_prefix_formatting_rule = "($NP$FG)"
        self.assertEqual("(020) 7031 3000",
                         phonenumbers.format_by_pattern(GB_NUMBER, PhoneNumberFormat.NATIONAL,
                                                        newNumberFormats))

        newNumFormat.national_prefix_formatting_rule = ""
        self.assertEqual("20 7031 3000",
                         phonenumbers.format_by_pattern(GB_NUMBER, PhoneNumberFormat.NATIONAL,
                                                        newNumberFormats))

        self.assertEqual("+44 20 7031 3000",
                         phonenumbers.format_by_pattern(GB_NUMBER, PhoneNumberFormat.INTERNATIONAL,
                                                        newNumberFormats))
        # Python version extra tests
        self.assertEqual("1234567890",
                         phonenumbers.format_by_pattern(XY_NUMBER, PhoneNumberFormat.E164,
                                                        newNumberFormats))
        # None of the patterns in the list match (because it's an empty list)
        self.assertEqual("6502530000", phonenumbers.format_by_pattern(US_NUMBER, PhoneNumberFormat.NATIONAL, []))

    def testFormatE164Number(self):
        self.assertEqual("+16502530000", phonenumbers.format_number(US_NUMBER, PhoneNumberFormat.E164))
        self.assertEqual("+4930123456", phonenumbers.format_number(DE_NUMBER, PhoneNumberFormat.E164))
        self.assertEqual("+80012345678", phonenumbers.format_number(INTERNATIONAL_TOLL_FREE, PhoneNumberFormat.E164))

    def testFormatNumberWithExtension(self):
        nzNumber = PhoneNumber()
        nzNumber.merge_from(NZ_NUMBER)
        nzNumber.extension = "1234"
        # Uses default extension prefix:
        self.assertEqual("03-331 6005 ext. 1234", phonenumbers.format_number(nzNumber, PhoneNumberFormat.NATIONAL))
        # Uses RFC 3966 syntax.
        self.assertEqual("+64-3-331-6005;ext=1234", phonenumbers.format_number(nzNumber, PhoneNumberFormat.RFC3966))
        # Extension prefix overridden in the territory information for the US:
        usNumberWithExtension = PhoneNumber()
        usNumberWithExtension.merge_from(US_NUMBER)
        usNumberWithExtension.extension = "4567"
        self.assertEqual("650 253 0000 extn. 4567", phonenumbers.format_number(usNumberWithExtension,
                                                                               PhoneNumberFormat.NATIONAL))

    def testFormatInOriginalFormat(self):
        number1 = phonenumbers.parse("+442087654321", "GB", keep_raw_input=True)
        self.assertEqual("+44 20 8765 4321", phonenumbers.format_in_original_format(number1, "GB"))

        number2 = phonenumbers.parse("02087654321", "GB", keep_raw_input=True)
        self.assertEqual("(020) 8765 4321", phonenumbers.format_in_original_format(number2, "GB"))

        number3 = phonenumbers.parse("011442087654321", "US", keep_raw_input=True)
        self.assertEqual("011 44 20 8765 4321", phonenumbers.format_in_original_format(number3, "US"))

        number4 = phonenumbers.parse("442087654321", "GB", keep_raw_input=True)
        self.assertEqual("44 20 8765 4321", phonenumbers.format_in_original_format(number4, "GB"))

        number5 = phonenumbers.parse("+442087654321", "GB")
        self.assertEqual("(020) 8765 4321", phonenumbers.format_in_original_format(number5, "GB"))

        # Invalid numbers that we have a formatting pattern for should be
        # formatted properly. Note area codes starting with 7 are
        # intentionally excluded in the test metadata for testing purposes.
        number6 = phonenumbers.parse("7345678901", "US", keep_raw_input=True)
        self.assertEqual("734 567 8901", phonenumbers.format_in_original_format(number6, "US"))

        # US is not a leading zero country, and the presence of the leading zero leads us to format the
        # number using raw_input.
        number7 = phonenumbers.parse("0734567 8901", "US", keep_raw_input=True)
        self.assertEqual("0734567 8901", phonenumbers.format_in_original_format(number7, "US"))

        # This number is valid, but we don't have a formatting pattern for
        # it. Fall back to the raw input.
        number8 = phonenumbers.parse("02-4567-8900", "KR", keep_raw_input=True)
        self.assertEqual("02-4567-8900", phonenumbers.format_in_original_format(number8, "KR"))

        number9 = phonenumbers.parse("01180012345678", "US", keep_raw_input=True)
        self.assertEqual("011 800 1234 5678", phonenumbers.format_in_original_format(number9, "US"))

        number10 = phonenumbers.parse("+80012345678", "KR", keep_raw_input=True)
        self.assertEqual("+800 1234 5678", phonenumbers.format_in_original_format(number10, "KR"))

        # US local numbers are formatted correctly, as we have formatting patterns for them.
        localNumberUS = phonenumbers.parse("2530000", "US", keep_raw_input=True)
        self.assertEqual("253 0000", phonenumbers.format_in_original_format(localNumberUS, "US"))

        numberWithNationalPrefixUS = phonenumbers.parse("18003456789", "US", keep_raw_input=True)
        self.assertEqual("1 800 345 6789",
                         phonenumbers.format_in_original_format(numberWithNationalPrefixUS, "US"))

        numberWithoutNationalPrefixGB = phonenumbers.parse("2087654321", "GB", keep_raw_input=True)
        self.assertEqual("20 8765 4321",
                         phonenumbers.format_in_original_format(numberWithoutNationalPrefixGB, "GB"))
        # Make sure no metadata is modified as a result of the previous function call.
        self.assertEqual("(020) 8765 4321", phonenumbers.format_in_original_format(number5, "GB"))

        numberWithNationalPrefixMX = phonenumbers.parse("013312345678", "MX", keep_raw_input=True)
        self.assertEqual("01 33 1234 5678",
                         phonenumbers.format_in_original_format(numberWithNationalPrefixMX, "MX"))

        numberWithoutNationalPrefixMX = phonenumbers.parse("3312345678", "MX", keep_raw_input=True)
        self.assertEqual("33 1234 5678",
                         phonenumbers.format_in_original_format(numberWithoutNationalPrefixMX, "MX"))

        italianFixedLineNumber = phonenumbers.parse("0212345678", "IT", keep_raw_input=True)
        self.assertEqual("02 1234 5678",
                         phonenumbers.format_in_original_format(italianFixedLineNumber, "IT"))

        numberWithNationalPrefixJP = phonenumbers.parse("00777012", "JP", keep_raw_input=True)
        self.assertEqual("0077-7012",
                         phonenumbers.format_in_original_format(numberWithNationalPrefixJP, "JP"))

        numberWithoutNationalPrefixJP = phonenumbers.parse("0777012", "JP", keep_raw_input=True)
        self.assertEqual("0777012",
                         phonenumbers.format_in_original_format(numberWithoutNationalPrefixJP, "JP"))

        numberWithCarrierCodeBR = phonenumbers.parse("012 3121286979", "BR", keep_raw_input=True)
        self.assertEqual("012 3121286979",
                         phonenumbers.format_in_original_format(numberWithCarrierCodeBR, "BR"))

        # The default national prefix used in this case is 045. When a number
        # with national prefix 044 is entered, we return the raw input as we
        # don't want to change the number entered.
        numberWithNationalPrefixMX1 = phonenumbers.parse("044(33)1234-5678", "MX", keep_raw_input=True)
        self.assertEqual("044(33)1234-5678",
                         phonenumbers.format_in_original_format(numberWithNationalPrefixMX1, "MX"))

        numberWithNationalPrefixMX2 = phonenumbers.parse("045(33)1234-5678", "MX", keep_raw_input=True)
        self.assertEqual("045 33 1234 5678",
                         phonenumbers.format_in_original_format(numberWithNationalPrefixMX2, "MX"))

        # The default international prefix used in this case is 0011. When a
        # number with international prefix 0012 is entered, we return the raw
        # input as we don't want to change the number entered.
        outOfCountryNumberFromAU1 = phonenumbers.parse("0012 16502530000", "AU", keep_raw_input=True)
        self.assertEqual("0012 16502530000",
                         phonenumbers.format_in_original_format(outOfCountryNumberFromAU1, "AU"))

        outOfCountryNumberFromAU2 = phonenumbers.parse("0011 16502530000", "AU", keep_raw_input=True)
        self.assertEqual("0011 1 650 253 0000",
                         phonenumbers.format_in_original_format(outOfCountryNumberFromAU2, "AU"))

        # Python version extra tests
        number101 = phonenumbers.parse("87654321", None, keep_raw_input=True, _check_region=False)
        self.assertEqual("87654321", phonenumbers.format_in_original_format(number101, "US"))

    def testIsPremiumRate(self):
        self.assertEqual(PhoneNumberType.PREMIUM_RATE, phonenumbers.number_type(US_PREMIUM))

        premiumRateNumber = PhoneNumber(country_code=39, national_number=892123L)
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 44
        premiumRateNumber.national_number = 9187654321L
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 49
        premiumRateNumber.national_number = 9001654321L
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 49
        premiumRateNumber.national_number = 90091234567L
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

    def testIsTollFree(self):
        tollFreeNumber = PhoneNumber(country_code=1, national_number=8881234567L)
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 39
        tollFreeNumber.national_number = 803123L
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 44
        tollFreeNumber.national_number = 8012345678L
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 49
        tollFreeNumber.national_number = 8001234567L
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(INTERNATIONAL_TOLL_FREE))

    def testIsMobile(self):
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(BS_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(GB_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(IT_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(AR_MOBILE))

        mobileNumber = PhoneNumber(country_code=49, national_number=15123456789L)
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(mobileNumber))

    def testIsFixedLine(self):
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(BS_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(IT_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(GB_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(DE_NUMBER))

    def testIsFixedLineAndMobile(self):
        self.assertEqual(PhoneNumberType.FIXED_LINE_OR_MOBILE,
                         phonenumbers.number_type(US_NUMBER))

        fixedLineAndMobileNumber = PhoneNumber(country_code=54, national_number=1987654321L)
        self.assertEqual(PhoneNumberType.FIXED_LINE_OR_MOBILE,
                         phonenumbers.number_type(fixedLineAndMobileNumber))

    def testIsSharedCost(self):
        gbNumber = PhoneNumber(country_code=44, national_number=8431231234L)
        self.assertEqual(PhoneNumberType.SHARED_COST, phonenumbers.number_type(gbNumber))

    def testIsVoip(self):
        gbNumber = PhoneNumber(country_code=44, national_number=5631231234L)
        self.assertEqual(PhoneNumberType.VOIP, phonenumbers.number_type(gbNumber))

    def testIsPersonalNumber(self):
        gbNumber = PhoneNumber(country_code=44, national_number=7031231234L)
        self.assertEqual(PhoneNumberType.PERSONAL_NUMBER,
                         phonenumbers.number_type(gbNumber))

    def testIsUnknown(self):
        # Invalid numbers should be of type UNKNOWN.
        self.assertEqual(PhoneNumberType.UNKNOWN, phonenumbers.number_type(US_LOCAL_NUMBER))

    def testIsValidNumber(self):
        self.assertTrue(phonenumbers.is_valid_number(US_NUMBER))
        self.assertTrue(phonenumbers.is_valid_number(IT_NUMBER))
        self.assertTrue(phonenumbers.is_valid_number(GB_MOBILE))
        self.assertTrue(phonenumbers.is_valid_number(INTERNATIONAL_TOLL_FREE))

        nzNumber = PhoneNumber(country_code=64, national_number=21387835L)
        self.assertTrue(phonenumbers.is_valid_number(nzNumber))

    def testIsValidForRegion(self):
        # This number is valid for the Bahamas, but is not a valid US number.
        self.assertTrue(phonenumbers.is_valid_number(BS_NUMBER))
        self.assertTrue(phonenumbers.is_valid_number_for_region(BS_NUMBER, "BS"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(BS_NUMBER, "US"))
        bsInvalidNumber = PhoneNumber(country_code=1, national_number=2421232345L)
        # This number is no longer valid.
        self.assertFalse(phonenumbers.is_valid_number(bsInvalidNumber))

        # La Mayotte and Reunion use 'leadingDigits' to differentiate them.
        reNumber = PhoneNumber(country_code=262, national_number=262123456L)
        self.assertTrue(phonenumbers.is_valid_number(reNumber))
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        # Now change the number to be a number for La Mayotte.
        reNumber.national_number = 269601234L
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        # This number is no longer valid for La Reunion.
        reNumber.national_number = 269123456L
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertFalse(phonenumbers.is_valid_number(reNumber))
        # However, it should be recognised as from La Mayotte, since it is valid for this region.
        self.assertEqual("YT", phonenumbers.region_code_for_number(reNumber))
        # This number is valid in both places.
        reNumber.national_number = 800123456L
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertTrue(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "001"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "US"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "ZZ"))

        invalidNumber = PhoneNumber()
        # Invalid country calling codes.
        invalidNumber.country_code = 3923
        invalidNumber.national_number = 2366L
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "ZZ"))
        invalidNumber.country_code = 3923
        invalidNumber.national_number = 2366L
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "001"))
        invalidNumber.country_code = 0
        invalidNumber.national_number = 2366L
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "001"))
        invalidNumber.country_code = 0
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "ZZ"))

        # Python version extra test
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "US"))

    def testIsNotValidNumber(self):
        self.assertFalse(phonenumbers.is_valid_number(US_LOCAL_NUMBER))

        invalidNumber = PhoneNumber(country_code=39, national_number=23661830000L, italian_leading_zero=True)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 44
        invalidNumber.national_number = 791234567L
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 49
        invalidNumber.national_number = 1234L
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 64
        invalidNumber.national_number = 3316005L
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        # Invalid country calling codes.
        invalidNumber.country_code = 3923
        invalidNumber.national_number = 2366L
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))
        invalidNumber.country_code = 0
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        self.assertFalse(phonenumbers.is_valid_number(INTERNATIONAL_TOLL_FREE_TOO_LONG))

    def testGetRegionCodeForCountryCode(self):
        self.assertEqual("US", phonenumbers.region_code_for_country_code(1))
        self.assertEqual("GB", phonenumbers.region_code_for_country_code(44))
        self.assertEqual("DE", phonenumbers.region_code_for_country_code(49))
        self.assertEqual("001", phonenumbers.region_code_for_country_code(800))

    def testGetRegionCodeForNumber(self):
        self.assertEqual("BS", phonenumbers.region_code_for_number(BS_NUMBER))
        self.assertEqual("US", phonenumbers.region_code_for_number(US_NUMBER))
        self.assertEqual("GB", phonenumbers.region_code_for_number(GB_MOBILE))
        self.assertEqual("001", phonenumbers.region_code_for_number(INTERNATIONAL_TOLL_FREE))

    def testGetCountryCodeForRegion(self):
        self.assertEqual(1, phonenumbers.country_code_for_region("US"))
        self.assertEqual(64, phonenumbers.country_code_for_region("NZ"))
        self.assertEqual(0, phonenumbers.country_code_for_region(None))
        self.assertEqual(0, phonenumbers.country_code_for_region("ZZ"))
        self.assertEqual(0, phonenumbers.country_code_for_region("001"))
        # CS is already deprecated so the library doesn't support it.
        self.assertEqual(0, phonenumbers.country_code_for_region("CS"))

    def testGetNationalDiallingPrefixForRegion(self):
        self.assertEqual("1", phonenumbers.ndd_prefix_for_region("US", False))
        # Test non-main country to see it gets the national dialling prefix
        # for the main country with that country calling code.
        self.assertEqual("1", phonenumbers.ndd_prefix_for_region("BS", False))
        self.assertEqual("0", phonenumbers.ndd_prefix_for_region("NZ", False))
        # Test case with non digit in the national prefix.
        self.assertEqual("0~0", phonenumbers.ndd_prefix_for_region("AO", False))
        self.assertEqual("00", phonenumbers.ndd_prefix_for_region("AO", True))
        # Test cases with invalid regions.
        self.assertEqual(None, phonenumbers.ndd_prefix_for_region(None, False))
        self.assertEqual(None, phonenumbers.ndd_prefix_for_region("ZZ", False))
        self.assertEqual(None, phonenumbers.ndd_prefix_for_region("001", False))
        # CS is already deprecated so the library doesn't support it.
        self.assertEqual(None, phonenumbers.ndd_prefix_for_region("CS", False))
        # Python version extra test
        # IT has no national prefix
        self.assertTrue(phonenumbers.ndd_prefix_for_region("IT", False) is None)

    def testIsNANPACountry(self):
        self.assertTrue(phonenumbers.is_nanpa_country("US"))
        self.assertTrue(phonenumbers.is_nanpa_country("BS"))
        self.assertFalse(phonenumbers.is_nanpa_country("DE"))
        self.assertFalse(phonenumbers.is_nanpa_country("ZZ"))
        self.assertFalse(phonenumbers.is_nanpa_country("001"))
        self.assertFalse(phonenumbers.is_nanpa_country(None))

    def testIsPossibleNumber(self):
        self.assertTrue(phonenumbers.is_possible_number(US_NUMBER))
        self.assertTrue(phonenumbers.is_possible_number(US_LOCAL_NUMBER))
        self.assertTrue(phonenumbers.is_possible_number(GB_NUMBER))
        self.assertTrue(phonenumbers.is_possible_number(INTERNATIONAL_TOLL_FREE))

        self.assertTrue(phonenumbers.is_possible_number_string("+1 650 253 0000", "US"))
        self.assertTrue(phonenumbers.is_possible_number_string("+1 650 GOO OGLE", "US"))
        self.assertTrue(phonenumbers.is_possible_number_string("(650) 253-0000", "US"))
        self.assertTrue(phonenumbers.is_possible_number_string("253-0000", "US"))
        self.assertTrue(phonenumbers.is_possible_number_string("+1 650 253 0000", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("+44 20 7031 3000", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("(020) 7031 3000", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("7031 3000", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("3331 6005", "NZ"))
        self.assertTrue(phonenumbers.is_possible_number_string("+800 1234 5678", "001"))

    def testIsPossibleNumberWithReason(self):
        # National numbers for country calling code +1 that are within 7 to 10 digits are possible.
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(US_NUMBER))

        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(US_LOCAL_NUMBER))

        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_with_reason(US_LONG_NUMBER))

        number = PhoneNumber(country_code=0, national_number=2530000L)
        self.assertEqual(ValidationResult.INVALID_COUNTRY_CODE,
                         phonenumbers.is_possible_number_with_reason(number))

        number.clear()
        number.country_code = 1
        number.national_number = 253000L
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_with_reason(number))

        number.clear()
        number.country_code = 65
        number.national_number = 1234567890L
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(number))

        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_with_reason(INTERNATIONAL_TOLL_FREE_TOO_LONG))

        # Try with number that we don't have metadata for.
        adNumber = PhoneNumber(country_code=376, national_number=12345L)
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(adNumber))
        adNumber.country_code = 376
        adNumber.national_number = 13L
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_with_reason(adNumber))
        adNumber.country_code = 376
        adNumber.national_number = 12345678901234567L
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_with_reason(adNumber))

    def testIsNotPossibleNumber(self):
        self.assertFalse(phonenumbers.is_possible_number(US_LONG_NUMBER))
        self.assertFalse(phonenumbers.is_possible_number(INTERNATIONAL_TOLL_FREE_TOO_LONG))

        number = PhoneNumber(country_code=1, national_number=253000L)
        self.assertFalse(phonenumbers.is_possible_number(number))

        number.clear()
        number.country_code = 44
        number.national_number = 300L
        self.assertFalse(phonenumbers.is_possible_number(number))
        self.assertFalse(phonenumbers.is_possible_number_string("+1 650 253 00000", "US"))
        self.assertFalse(phonenumbers.is_possible_number_string("(650) 253-00000", "US"))
        self.assertFalse(phonenumbers.is_possible_number_string("I want a Pizza", "US"))
        self.assertFalse(phonenumbers.is_possible_number_string("253-000", "US"))
        self.assertFalse(phonenumbers.is_possible_number_string("1 3000", "GB"))
        self.assertFalse(phonenumbers.is_possible_number_string("+44 300", "GB"))
        self.assertFalse(phonenumbers.is_possible_number_string("+800 1234 5678 9", "001"))

    def testTruncateTooLongNumber(self):
        # GB number 080 1234 5678, but entered with 4 extra digits at the end.
        tooLongNumber = PhoneNumber(country_code=44, national_number=80123456780123L)
        validNumber = PhoneNumber(country_code=44, national_number=8012345678L)
        self.assertTrue(phonenumbers.truncate_too_long_number(tooLongNumber))
        self.assertEqual(validNumber, tooLongNumber)

        # IT number 022 3456 7890, but entered with 3 extra digits at the end.
        tooLongNumber.clear()
        tooLongNumber.country_code = 39
        tooLongNumber.national_number = 2234567890123L
        tooLongNumber.italian_leading_zero = True
        validNumber.clear()
        validNumber.country_code = 39
        validNumber.national_number = 2234567890L
        validNumber.italian_leading_zero = True
        self.assertTrue(phonenumbers.truncate_too_long_number(tooLongNumber))
        self.assertEqual(validNumber, tooLongNumber)

        # US number 650-253-0000, but entered with one additional digit at the end.
        tooLongNumber.clear()
        tooLongNumber.merge_from(US_LONG_NUMBER)
        self.assertTrue(phonenumbers.truncate_too_long_number(tooLongNumber))
        self.assertEqual(US_NUMBER, tooLongNumber)

        tooLongNumber.clear()
        tooLongNumber.merge_from(INTERNATIONAL_TOLL_FREE_TOO_LONG)
        self.assertTrue(phonenumbers.truncate_too_long_number(tooLongNumber))
        self.assertEqual(INTERNATIONAL_TOLL_FREE, tooLongNumber)

        # Tests what happens when a valid number is passed in.
        validNumberCopy = PhoneNumber()
        validNumberCopy.merge_from(validNumber)
        self.assertTrue(phonenumbers.truncate_too_long_number(validNumber))
        # Tests the number is not modified.
        self.assertEqual(validNumberCopy, validNumber)

        # Tests what happens when a number with invalid prefix is passed in.
        # The test metadata says US numbers cannot have prefix 240.
        numberWithInvalidPrefix = PhoneNumber(country_code=1, national_number=2401234567L)
        invalidNumberCopy = PhoneNumber()
        invalidNumberCopy.merge_from(numberWithInvalidPrefix)
        self.assertFalse(phonenumbers.truncate_too_long_number(numberWithInvalidPrefix))
        # Tests the number is not modified.
        self.assertEqual(invalidNumberCopy, numberWithInvalidPrefix)

        # Tests what happens when a too short number is passed in.
        tooShortNumber = PhoneNumber(country_code=1, national_number=1234L)
        tooShortNumberCopy = PhoneNumber()
        tooShortNumberCopy.merge_from(tooShortNumber)
        self.assertFalse(phonenumbers.truncate_too_long_number(tooShortNumber))
        # Tests the number is not modified.
        self.assertEqual(tooShortNumberCopy, tooShortNumber)

    def testIsViablePhoneNumber(self):
        # Only one or two digits before strange non-possible punctuation.
        self.assertFalse(phonenumberutil._is_viable_phone_number("12. March"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("1+1+1"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("80+0"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("00"))
        # Three digits is viable.
        self.assertTrue(phonenumberutil._is_viable_phone_number("111"))
        # Alpha numbers.
        self.assertTrue(phonenumberutil._is_viable_phone_number("0800-4-pizza"))
        self.assertTrue(phonenumberutil._is_viable_phone_number("0800-4-PIZZA"))

    def testIsViablePhoneNumberNonAscii(self):
        # Only one or two digits before possible punctuation followed by more digits.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u"1\u300034"))
        self.assertFalse(phonenumberutil._is_viable_phone_number(u"1\u30003+4"))
        # Unicode variants of possible starting character and other allowed punctuation/digits.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u"\uFF081\uFF09\u30003456789"))
        # Testing a leading + is okay.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u"+1\uFF09\u30003456789"))

    def testExtractPossibleNumber(self):
        # Removes preceding funky punctuation and letters but leaves the rest untouched.
        self.assertEqual("0800-345-600", phonenumberutil._extract_possible_number("Tel:0800-345-600"))
        self.assertEqual("0800 FOR PIZZA", phonenumberutil._extract_possible_number("Tel:0800 FOR PIZZA"))
        # Should not remove plus sign
        self.assertEqual("+800-345-600", phonenumberutil._extract_possible_number("Tel:+800-345-600"))
        # Should recognise wide digits as possible start values.
        self.assertEqual(u"\uFF10\uFF12\uFF13",
                         phonenumberutil._extract_possible_number(u"\uFF10\uFF12\uFF13"))
        # Dashes are not possible start values and should be removed.
        self.assertEqual(u"\uFF11\uFF12\uFF13",
                         phonenumberutil._extract_possible_number(u"Num-\uFF11\uFF12\uFF13"))
        # If not possible number present, return empty string.
        self.assertEqual("", phonenumberutil._extract_possible_number("Num-...."))
        # Leading brackets are stripped - these are not used when parsing.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000"))

        # Trailing non-alpha-numeric characters should be removed.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000..- .."))
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000."))
        # This case has a trailing RTL char.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number(u"(650) 253-0000\u200F"))

    def testMaybeStripNationalPrefix(self):
        metadata = PhoneMetadata(id="Test", national_prefix_for_parsing="34", register=False)
        metadata.general_desc = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        numberToStrip = "34356778"
        strippedNumber = "356778"
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertTrue(rc)
        self.assertEqual(strippedNumber, numberToStrip,
                         msg="Should have had national prefix stripped.")
        # Retry stripping - now the number should not start with the national prefix, so no more
        # stripping should occur.
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertFalse(rc)
        self.assertEqual(strippedNumber, numberToStrip,
                         msg="Should have had no change - no national prefix present.")
        # Some countries have no national prefix. Repeat test with none specified.
        metadata.national_prefix_for_parsing = ""
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertFalse(rc)
        self.assertEqual(strippedNumber, numberToStrip,
                         msg="Should not strip anything with empty national prefix.")
        # If the resultant number doesn't match the national rule, it shouldn't be stripped.
        metadata.national_prefix_for_parsing = "3"
        numberToStrip = "3123"
        strippedNumber = "3123"
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertFalse(rc)
        self.assertEqual(strippedNumber, numberToStrip,
                         msg="Should have had no change - after stripping, it wouldn't have matched the national rule.")
        # Test extracting carrier selection code.
        metadata.national_prefix_for_parsing = "0(81)?"
        numberToStrip = "08122123456"
        strippedNumber = "22123456"
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertTrue(rc)
        self.assertEqual("81", cc)
        self.assertEqual(strippedNumber, numberToStrip,
                         msg="Should have had national prefix and carrier code stripped.")
        # If there was a transform rule, check it was applied.
        metadata.national_prefix_transform_rule = "5\\g<1>5"
        # Note that a capturing group is present here.
        metadata.national_prefix_for_parsing = "0(\\d{2})"
        numberToStrip = "031123"
        transformedNumber = "5315123"
        cc, numberToStrip, rc = phonenumberutil._maybe_strip_national_prefix_carrier_code(numberToStrip, metadata)
        self.assertTrue(rc)
        self.assertEqual(transformedNumber, numberToStrip,
                         msg="Should transform the 031 to a 5315.")

    def testMaybeStripInternationalPrefix(self):
        internationalPrefix = "00[39]"
        numberToStrip = "0034567700-3898003"
        # Note the dash is removed as part of the normalization.
        strippedNumber = "45677003898003"
        self.assertEqual((CountryCodeSource.FROM_NUMBER_WITH_IDD, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix),
                         msg="The number supplied was not stripped of its international prefix.")
        # Now the number no longer starts with an IDD prefix, so it should now
        # report FROM_DEFAULT_COUNTRY.
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(strippedNumber, internationalPrefix))

        numberToStrip = "00945677003898003"
        self.assertEqual((CountryCodeSource.FROM_NUMBER_WITH_IDD, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix),
                         msg="The number supplied was not stripped of its international prefix.")

        # Test it works when the international prefix is broken up by spaces.
        numberToStrip = "00 9 45677003898003"
        self.assertEqual((CountryCodeSource.FROM_NUMBER_WITH_IDD, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix),
                         msg="The number supplied was not stripped of its international prefix.")

        # Now the number no longer starts with an IDD prefix, so it should now report
        # FROM_DEFAULT_COUNTRY.
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(strippedNumber, internationalPrefix))

        # Test the + symbol is also recognised and stripped.
        numberToStrip = "+45677003898003"
        strippedNumber = "45677003898003"
        self.assertEqual((CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix),
                         msg="The number supplied was not stripped of the plus symbol.")

        # If the number afterwards is a zero, we should not strip this - no country calling code begins
        # with 0.
        numberToStrip = "0090112-3123"
        strippedNumber = "00901123123"
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix),
                         msg="The number supplied had a 0 after the match so shouldn't be stripped.")
        # Here the 0 is separated by a space from the IDD.
        numberToStrip = "009 0-112-3123"
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, strippedNumber),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize(numberToStrip, internationalPrefix))

    def testMaybeExtractCountryCode(self):
        number = PhoneNumber()
        metadata = PhoneMetadata.region_metadata["US"]
        # Note that for the US, the IDD is 011.
        try:
            phoneNumber = "011112-3456789"
            strippedNumber = "123456789"
            countryCallingCode = 1
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Did not extract country calling code %s correctly." % countryCallingCode)

            self.assertEqual(CountryCodeSource.FROM_NUMBER_WITH_IDD, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
            # Should strip and normalize national significant number.
            self.assertEqual(strippedNumber, numberToFill,
                             msg="Did not strip off the country calling code correctly.")
            # Python version extra test covering string conversion with country_code_source present
            self.assertEqual("Country Code: 1 National Number: None Leading Zero: False Country Code Source: 5",
                             str(number))
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "+6423456789"
            countryCallingCode = 64
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Did not extract country calling code %s correctly." % countryCallingCode)
            self.assertEqual(CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "+80012345678"
            countryCallingCode = 800
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Did not extract country calling code %s correctly." % countryCallingCode)
            self.assertEqual(CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "2345-6789"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(0, ccc,
                             msg="Should not have extracted a country calling code - no international prefix present.")
            self.assertEqual(CountryCodeSource.FROM_DEFAULT_COUNTRY, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "0119991123456789"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.fail("Should have thrown an exception, no valid country calling code present.")
        except NumberParseException, e:
            # Expected.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
            self.assertEqual("(0) Country calling code supplied was not recognised.",
                             str(e))

        number.clear()
        try:
            phoneNumber = "(1 610) 619 4466"
            countryCallingCode = 1
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Should have extracted the country calling code of the region passed in")
            self.assertEqual(CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN,
                             number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "(1 610) 619 4466"
            countryCallingCode = 1
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, False, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Should have extracted the country calling code of the region passed in")
            self.assertFalse(number.country_code_source is not None,
                             msg="Should not contain CountryCodeSource.")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "(1 610) 619 446"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, False, number)
            self.assertEqual(0, ccc,
                             msg=("Should not have extracted a country calling code - invalid number after " +
                                  "extraction of uncertain country calling code."))
            self.assertFalse(number.country_code_source is not None,
                             msg="Should not contain CountryCodeSource.")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "(1 610) 619"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(0, ccc,
                             msg=("Should not have extracted a country calling code - too short number both " +
                                  "before and after extraction of uncertain country calling code."))
            self.assertEqual(CountryCodeSource.FROM_DEFAULT_COUNTRY, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException, e:
            self.fail("Should not have thrown an exception: %s" % e)

    def testParseNationalNumber(self):
        # National prefix attached.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("033316005", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("33316005", "NZ"))
        # National prefix attached and some formatting present.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("03-331 6005", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("03 331 6005", "NZ"))

        # Testing international prefixes.
        # Should strip country calling code.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("0064 3 331 6005", "NZ"))
        # Try again, but this time we have an international number with Region Code US. It should
        # recognise the country calling code and parse accordingly.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("01164 3 331 6005", "US"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+64 3 331 6005", "US"))
        # We should ignore the leading plus here, since it is not followed by
        # a valid country code but instead is followed by the IDD for the US.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+01164 3 331 6005", "US"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+0064 3 331 6005", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+ 00 64 3 331 6005", "NZ"))

        nzNumber = PhoneNumber(country_code=64, national_number=64123456L)
        self.assertEqual(nzNumber, phonenumbers.parse("64(0)64123456", "NZ"))
        # Check that using a "/" is fine in a phone number.
        self.assertEqual(DE_NUMBER, phonenumbers.parse("301/23456", "DE"))

        # Check it doesn't use the '1' as a country calling code when parsing if the phone number was
        # already possible.
        usNumber = PhoneNumber(country_code=1, national_number=1234567890L)
        self.assertEqual(usNumber, phonenumbers.parse("123-456-7890", "US"))

        # Test star numbers. Although this is not strictly valid, we would
        # like to make sure we can parse the output we produce when formatting
        # the number.
        self.assertEqual(JP_STAR_NUMBER, phonenumbers.parse("+81 *2345", "JP"))

    def testParseNumberWithAlphaCharacters(self):
        # Test case with alpha characters.
        tollfreeNumber = PhoneNumber(country_code=64, national_number=800332005L)
        self.assertEqual(tollfreeNumber, phonenumbers.parse("0800 DDA 005", "NZ"))
        premiumNumber = PhoneNumber(country_code=64, national_number=9003326005L)
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 DDA 6005", "NZ"))
        # Not enough alpha characters for them to be considered intentional, so they are stripped.
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 6005a", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 600a5", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 600A5", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 a332 600A5", "NZ"))

    def testParseWithInternationalPrefixes(self):
        self.assertEqual(US_NUMBER, phonenumbers.parse("+1 (650) 253-0000", "NZ"))
        self.assertEqual(INTERNATIONAL_TOLL_FREE, phonenumbers.parse("011 800 1234 5678", "US"))
        self.assertEqual(US_NUMBER, phonenumbers.parse("1-650-253-0000", "US"))
        # Calling the US number from Singapore by using different service providers
        # 1st test: calling using SingTel IDD service (IDD is 001)
        self.assertEqual(US_NUMBER, phonenumbers.parse("0011-650-253-0000", "SG"))
        # 2nd test: calling using StarHub IDD service (IDD is 008)
        self.assertEqual(US_NUMBER, phonenumbers.parse("0081-650-253-0000", "SG"))
        # 3rd test: calling using SingTel V019 service (IDD is 019)
        self.assertEqual(US_NUMBER, phonenumbers.parse("0191-650-253-0000", "SG"))
        # Calling the US number from Poland
        self.assertEqual(US_NUMBER, phonenumbers.parse("0~01-650-253-0000", "PL"))
        # Using "++" at the start.
        self.assertEqual(US_NUMBER, phonenumbers.parse("++1 (650) 253-0000", "PL"))

    def testParseNonAscii(self):
        # Using a full-width plus sign.
        self.assertEqual(US_NUMBER, phonenumbers.parse(u"\uFF0B1 (650) 253-0000", "SG"))
        # The whole number, including punctuation, is here represented in full-width form.
        self.assertEqual(US_NUMBER, phonenumbers.parse(u"\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09" +
                                                       u"\u3000\uFF12\uFF15\uFF13\uFF0D\uFF10\uFF10\uFF10" +
                                                       u"\uFF10",
                                                       "SG"))
        # Using U+30FC dash instead.
        self.assertEqual(US_NUMBER, phonenumbers.parse(u"\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09" +
                                                       u"\u3000\uFF12\uFF15\uFF13\u30FC\uFF10\uFF10\uFF10" +
                                                       u"\uFF10",
                                                       "SG"))
        # Using a very strange decimal digit range (Mongolian digits).
        self.assertEqual(US_NUMBER, phonenumbers.parse(u"\u1811 \u1816\u1815\u1810 " +
                                                       u"\u1812\u1815\u1813 \u1810\u1810\u1810\u1810",
                                                       "US"))

    def testParseWithLeadingZero(self):
        self.assertEqual(IT_NUMBER, phonenumbers.parse("+39 02-36618 300", "NZ"))
        self.assertEqual(IT_NUMBER, phonenumbers.parse("02-36618 300", "IT"))

        self.assertEqual(IT_MOBILE, phonenumbers.parse("345 678 901", "IT"))

    def testParseNationalNumberArgentina(self):
        # Test parsing mobile numbers of Argentina.
        arNumber = PhoneNumber(country_code=54, national_number=93435551212L)
        self.assertEqual(arNumber, phonenumbers.parse("+54 9 343 555 1212", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("0343 15 555 1212", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = 93715654320L
        self.assertEqual(arNumber, phonenumbers.parse("+54 9 3715 65 4320", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("03715 15 65 4320", "AR"))
        self.assertEqual(AR_MOBILE, phonenumbers.parse("911 876 54321", "AR"))

        # Test parsing fixed-line numbers of Argentina.
        self.assertEqual(AR_NUMBER, phonenumbers.parse("+54 11 8765 4321", "AR"))
        self.assertEqual(AR_NUMBER, phonenumbers.parse("011 8765 4321", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = 3715654321L
        self.assertEqual(arNumber, phonenumbers.parse("+54 3715 65 4321", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("03715 65 4321", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = 2312340000L
        self.assertEqual(arNumber, phonenumbers.parse("+54 23 1234 0000", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("023 1234 0000", "AR"))

        # Python version extra test
        arIncompleteNumber = phonenumbers.parse("03715 15 65", "AR")
        self.assertEqual("9371565",
                         phonenumbers.format_number(arIncompleteNumber, PhoneNumberFormat.NATIONAL))

    def testParseWithXInNumber(self):
        # Test that having an 'x' in the phone number at the start is ok and that it just gets removed.
        self.assertEqual(AR_NUMBER, phonenumbers.parse("01187654321", "AR"))
        self.assertEqual(AR_NUMBER, phonenumbers.parse("(0) 1187654321", "AR"))
        self.assertEqual(AR_NUMBER, phonenumbers.parse("0 1187654321", "AR"))
        self.assertEqual(AR_NUMBER, phonenumbers.parse("(0xx) 1187654321", "AR"))
        arFromUs = PhoneNumber(country_code=54, national_number=81429712L)
        # This test is intentionally constructed such that the number of digit
        # after xx is larger than 7, so that the number won't be mistakenly
        # treated as an extension, as we allow extensions up to 7 digits. This
        # assumption is okay for now as all the countries where a carrier
        # selection code is written in the form of xx have a national
        # significant number of length larger than 7.
        self.assertEqual(arFromUs, phonenumbers.parse("011xx5481429712", "US"))

    def testParseNumbersMexico(self):
        # Test parsing fixed-line numbers of Mexico.
        mxNumber = PhoneNumber(country_code=52, national_number=4499780001L)
        self.assertEqual(mxNumber, phonenumbers.parse("+52 (449)978-0001", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("01 (449)978-0001", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("(449)978-0001", "MX"))

        # Test parsing mobile numbers of Mexico.
        mxNumber.clear()
        mxNumber.country_code = 52
        mxNumber.national_number = 13312345678L
        self.assertEqual(mxNumber, phonenumbers.parse("+52 1 33 1234-5678", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("044 (33) 1234-5678", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("045 33 1234-5678", "MX"))

    def testFailedParseOnInvalidNumbers(self):
        try:
            sentencePhoneNumber = "This is not a phone number"
            phonenumbers.parse(sentencePhoneNumber, "NZ")
            self.fail("This should not parse without throwing an exception " + sentencePhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            tooLongPhoneNumber = "01495 72553301873 810104"
            phonenumbers.parse(tooLongPhoneNumber, "GB")
            self.fail("This should not parse without throwing an exception " + tooLongPhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_LONG,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusMinusPhoneNumber = "+---"
            phonenumbers.parse(plusMinusPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusStar = "+***"
            phonenumbers.parse(plusStar, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusStarPhoneNumber = "+*******91"
            phonenumbers.parse(plusStarPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            tooShortPhoneNumber = "+49 0"
            phonenumbers.parse(tooShortPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + tooShortPhoneNumber)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_SHORT_NSN,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            invalidCountryCode = "+210 3456 56789"
            phonenumbers.parse(invalidCountryCode, "NZ")
            self.fail("This is not a recognised region code: should fail: " + invalidCountryCode)
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusAndIddAndInvalidCountryCode = "+ 00 210 3 331 6005"
            phonenumbers.parse(plusAndIddAndInvalidCountryCode, "NZ")
            self.fail("This should not parse without throwing an exception.")
        except NumberParseException, e:
            # Expected this exception. 00 is a correct IDD, but 210 is not a valid country code.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, "ZZ")
            self.fail("'Unknown' region code not allowed: should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, "CS")
            self.fail("Deprecated region code not allowed: should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, None)
            self.fail("Null region code not allowed: should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0044------"
            phonenumbers.parse(someNumber, "GB")
            self.fail("No number provided, only region code: should fail")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0044"
            phonenumbers.parse(someNumber, "GB")
            self.fail("No number provided, only region code: should fail")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "011"
            phonenumbers.parse(someNumber, "US")
            self.fail("Only IDD provided - should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0119"
            phonenumbers.parse(someNumber, "US")
            self.fail("Only IDD provided and then 9 - should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            emptyNumber = ""
            # Invalid region.
            phonenumbers.parse(emptyNumber, "ZZ")
            self.fail("Empty string - should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            nullNumber = None
            # Invalid region.
            phonenumbers.parse(nullNumber, "ZZ")
            self.fail("Null string - should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        except Exception:
            self.fail("None string - but should not throw an exception.")

        try:
            nullNumber = None
            phonenumbers.parse(nullNumber, "US")
            self.fail("Null string - should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        except Exception:
            self.fail("None string - but should not throw an exception.")

    def testParseNumbersWithPlusWithNoRegion(self):
        # "ZZ" is allowed only if the number starts with a '+' - then the country calling code
        # can be calculated.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+64 3 331 6005", "ZZ"))
        # Test with full-width plus.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse(u"\uFF0B64 3 331 6005", "ZZ"))
        # Test with normal plus but leading characters that need to be stripped.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("Tel: +64 3 331 6005", "ZZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+64 3 331 6005", None))
        self.assertEqual(INTERNATIONAL_TOLL_FREE, phonenumbers.parse("+800 1234 5678", None))

        # It is important that we set the carrier code to an empty string, since we used
        # parse_number(leep_raw_input = True) and no carrier code was found.
        nzNumberWithRawInput = PhoneNumber()
        nzNumberWithRawInput.merge_from(NZ_NUMBER)
        nzNumberWithRawInput.raw_input = "+64 3 331 6005"
        nzNumberWithRawInput.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        nzNumberWithRawInput.preferred_domestic_carrier_code = ""
        self.assertEqual(nzNumberWithRawInput, phonenumbers.parse("+64 3 331 6005", "ZZ", keep_raw_input=True))
        # Null is also allowed for the region code in these cases.
        self.assertEqual(nzNumberWithRawInput, phonenumbers.parse("+64 3 331 6005", None, keep_raw_input=True))

    def testParseExtensions(self):
        nzNumber = PhoneNumber(country_code=64, national_number=33316005L, extension="3456")
        self.assertEqual(nzNumber, phonenumbers.parse("03 331 6005 ext 3456", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03-3316005x3456", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03-3316005 int.3456", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 #3456", "NZ"))
        # Test the following do not extract extensions:
        self.assertEqual(ALPHA_NUMERIC_NUMBER, phonenumbers.parse("1800 six-flags", "US"))
        self.assertEqual(ALPHA_NUMERIC_NUMBER, phonenumbers.parse("1800 SIX FLAGS", "US"))
        self.assertEqual(ALPHA_NUMERIC_NUMBER, phonenumbers.parse("0~0 1800 7493 5247", "PL"))
        self.assertEqual(ALPHA_NUMERIC_NUMBER, phonenumbers.parse("(1800) 7493.5247", "US"))
        # Check that the last instance of an extension token is matched.
        extnNumber = PhoneNumber()
        extnNumber.merge_from(ALPHA_NUMERIC_NUMBER)
        extnNumber.extension = "1234"
        self.assertEqual(extnNumber, phonenumbers.parse("0~0 1800 7493 5247 ~1234", "PL"))
        # Verifying bug-fix where the last digit of a number was previously omitted if it was a 0 when
        # extracting the extension. Also verifying a few different cases of extensions.
        ukNumber = PhoneNumber(country_code=44, national_number=2034567890L, extension="456")
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890x456", "NZ"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890x456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 x456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X 456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X    456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 x 456    ", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890    X 456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44-2034567890;ext=456", "GB"))
        # Full-width extension, "extn" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u"+442034567890\uFF45\uFF58\uFF54\uFF4E456", "GB"))
        # "xtn" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u"+442034567890\uFF58\uFF54\uFF4E456", "GB"))
        # "xt" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u"+442034567890\uFF58\uFF54456", "GB"))

        usWithExtension = PhoneNumber(country_code=1, national_number=8009013355L, extension="7246433")
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 x 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 , ext 7246433", "US"))
        self.assertEqual(usWithExtension,
                         phonenumbers.parse("(800) 901-3355 ,extension 7246433", "US"))
        self.assertEqual(usWithExtension,
                         phonenumbers.parse(u"(800) 901-3355 ,extensi\u00F3n 7246433", "US"))
        # Repeat with the small letter o with acute accent created by combining characters.
        self.assertEqual(usWithExtension,
                         phonenumbers.parse(u"(800) 901-3355 ,extensio\u0301n 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 , 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 ext: 7246433", "US"))

        # Test that if a number has two extensions specified, we ignore the second.
        usWithTwoExtensionsNumber = PhoneNumber(country_code=1, national_number=2121231234L, extension="508")
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508/x1234", "US"))
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508/ x1234", "US"))
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508\\x1234", "US"))

        # Test parsing numbers in the form (645) 123-1234-910# works, where the last 3 digits before
        # the # are an extension.
        usWithExtension.clear()
        usWithExtension.country_code = 1
        usWithExtension.national_number = 6451231234L
        usWithExtension.extension = "910"
        self.assertEqual(usWithExtension, phonenumbers.parse("+1 (645) 123 1234-910#", "US"))
        # Retry with the same number in a slightly different format.
        self.assertEqual(usWithExtension, phonenumbers.parse("+1 (645) 123 1234 ext. 910#", "US"))

    def testParseAndKeepRaw(self):
        alphaNumericNumber = PhoneNumber()
        alphaNumericNumber.merge_from(ALPHA_NUMERIC_NUMBER)
        alphaNumericNumber.raw_input = "800 six-flags"
        alphaNumericNumber.country_code_source = CountryCodeSource.FROM_DEFAULT_COUNTRY
        alphaNumericNumber.preferred_domestic_carrier_code = ""
        self.assertEqual(alphaNumericNumber,
                         phonenumbers.parse("800 six-flags", "US", keep_raw_input=True))

        shorterAlphaNumber = PhoneNumber(country_code=1, national_number=8007493524L,
                                         raw_input="1800 six-flag",
                                         country_code_source=CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN,
                                         preferred_domestic_carrier_code="")
        self.assertEqual(shorterAlphaNumber,
                          phonenumbers.parse("1800 six-flag", "US", keep_raw_input=True))

        shorterAlphaNumber.raw_input = "+1800 six-flag"
        shorterAlphaNumber.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertEqual(shorterAlphaNumber,
                          phonenumbers.parse("+1800 six-flag", "NZ", keep_raw_input=True))

        shorterAlphaNumber.raw_input = "001800 six-flag"
        shorterAlphaNumber.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_IDD
        self.assertEqual(shorterAlphaNumber,
                         phonenumbers.parse("001800 six-flag", "NZ", keep_raw_input=True))

        # Invalid region code supplied.
        try:
            phonenumbers.parse("123 456 7890", "CS", keep_raw_input=True)
            self.fail("Deprecated region code not allowed: should fail.")
        except NumberParseException, e:
            # Expected this exception.
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        koreanNumber = PhoneNumber(country_code=82, national_number=22123456, raw_input="08122123456",
                                   country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY,
                                   preferred_domestic_carrier_code="81")
        self.assertEqual(koreanNumber, phonenumbers.parse("08122123456", "KR", keep_raw_input=True))

    def testCountryWithNoNumberDesc(self):
        # Andorra is a country where we don't have PhoneNumberDesc info in the metadata.
        adNumber = PhoneNumber(country_code=376, national_number=12345L)
        self.assertEqual("+376 12345", phonenumbers.format_number(adNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+37612345", phonenumbers.format_number(adNumber, PhoneNumberFormat.E164))
        self.assertEqual("12345", phonenumbers.format_number(adNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual(PhoneNumberType.UNKNOWN, phonenumbers.number_type(adNumber))
        self.assertTrue(phonenumbers.is_valid_number(adNumber))

        # Test dialing a US number from within Andorra.
        self.assertEqual("00 1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "AD"))

    def testUnknownCountryCallingCodeForValidation(self):
        invalidNumber = PhoneNumber(country_code=0, national_number=1234L)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

    def testIsNumberMatchMatches(self):
        # Test simple matches where formatting is different, or leading zeroes, or country calling code
        # has been specified.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331 6005", "+64 03 331 6005"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 03 331-6005", "+64 03331 6005"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+800 1234 5678", "+80012345678"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+643 331-6005", "+64033316005"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+643 331-6005", "+6433316005"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "+6433316005"))
        # Test alpha numbers.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+1800 siX-Flags", "+1 800 7493 5247"))
        # Test numbers with extensions.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 extn 1234", "+6433316005#1234"))
        # Test proto buffers.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(NZ_NUMBER, "+6403 331 6005"))

        nzNumber = PhoneNumber()
        nzNumber.merge_from(NZ_NUMBER)
        nzNumber.extension = "3456"
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumber, "+643 331 6005 ext 3456"))
        # Check empty extensions are ignored.
        nzNumber.extension = ""
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumber, "+6403 331 6005"))
        # Check variant with two proto buffers.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumber, NZ_NUMBER),
                         msg="Number " + str(nzNumber) + " did not match " + str(NZ_NUMBER))

        # Check raw_input, country_code_source and preferred_domestic_carrier_code are ignored.
        brNumberOne = PhoneNumber(country_code=55, national_number=3121286979L,
                                  country_code_source=CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN,
                                  preferred_domestic_carrier_code="12", raw_input="012 3121286979")
        brNumberTwo = PhoneNumber(country_code=55, national_number=3121286979L,
                                  country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY,
                                  preferred_domestic_carrier_code="14", raw_input="143121286979")
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                          phonenumbers.is_number_match(brNumberOne, brNumberTwo))

        # Python version extra tests
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+9991234567", "+99943211234"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match(brNumberOne, "+9991235467"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+9991235467", brNumberOne))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("asdfasdf", brNumberOne))
        self.assertFalse(phonenumberutil._is_number_matching_desc(1234, None))

    def testIsNumberMatchNonMatches(self):
        # Non-matches.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("03 331 6005", "03 331 6006"))
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+800 1234 5678", "+1 800 1234 5678"))
        # Different country calling code, partial number match.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "+16433316005"))
        # Different country calling code, same number.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "+6133316005"))
        # Extension different, all else the same.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 extn 1234", "0116433316005#1235"))
        # NSN matches, but extension is different - not the same number.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 ext.1235", "3 331 6005#1234"))

        # Invalid numbers that can't be parsed.
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("43", "3 331 6043"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+43", "+64 3 331 6005"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+43", "64 3 331 6005"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("Dog", "64 3 331 6005"))

    def testIsNumberMatchNsnMatches(self):
        # NSN matches.
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "03 331 6005"))
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match(NZ_NUMBER, "03 331 6005"))
        # Here the second number possibly starts with the country calling code for Zealand,
        # although we are unsure.
        unchangedNzNumber = PhoneNumber()
        unchangedNzNumber.merge_from(NZ_NUMBER)
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match(unchangedNzNumber, "(64-3) 331 6005"))
        # Check the phone number proto was not edited during the method call.
        self.assertEqual(NZ_NUMBER, unchangedNzNumber)

        # Here, the 1 might be a national prefix, if we compare it to the US number, so the resultant
        # match is an NSN match.
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match(US_NUMBER, "1-650-253-0000"))
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match(US_NUMBER, "6502530000"))
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match("+1 650-253 0000", "1 650 253 0000"))
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match("1 650-253 0000", "1 650 253 0000"))
        self.assertEqual(phonenumbers.MatchType.NSN_MATCH,
                         phonenumbers.is_number_match("1 650-253 0000", "+1 650 253 0000"))
        # For this case, the match will be a short NSN match, because we cannot assume that the 1 might
        # be a national prefix, so don't remove it when parsing.
        randomNumber = PhoneNumber(country_code=41, national_number=6502530000L)
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(randomNumber, "1-650-253-0000"))

    def testIsNumberMatchShortNsnMatches(self):
        # Short NSN matches with the country not specified for either one or both numbers.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "331 6005"))
        # We did not know that the "0" was a national prefix since neither
        # number has a country code, so this is considered a SHORT_NSN_MATCH.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "03 331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "+64 331 6005"))
        # Short NSN match with the country specified.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("03 331-6005", "331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("1 234 345 6789", "345 6789"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+1 (234) 345 6789", "345 6789"))
        # NSN matches, country calling code omitted for one number, extension missing for one.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "3 331 6005#1234"))
        # One has Italian leading zero, one does not.
        italianNumberOne = PhoneNumber(country_code=39, national_number=1234L, italian_leading_zero=True)
        italianNumberTwo = PhoneNumber(country_code=39, national_number=1234L)
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(italianNumberOne, italianNumberTwo))
        # One has an extension, the other has an extension of "".
        italianNumberOne.extension = "1234"
        italianNumberOne.italian_leading_zero = None
        italianNumberTwo.extension = ""
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(italianNumberOne, italianNumberTwo))

    def testCanBeInternationallyDialled(self):
        # We have no-international-dialling rules for the US in our test metadata that say that
        # toll-free numbers cannot be dialled internationally.
        self.assertFalse(phonenumberutil._can_be_internationally_dialled(US_TOLLFREE))

        # Normal US numbers can be internationally dialled.
        self.assertTrue(phonenumberutil._can_be_internationally_dialled(US_NUMBER))

        # Invalid number.
        self.assertTrue(phonenumberutil._can_be_internationally_dialled(US_LOCAL_NUMBER))

        # We have no data for NZ - should return True.
        self.assertTrue(phonenumberutil._can_be_internationally_dialled(NZ_NUMBER))
        self.assertTrue(phonenumberutil._can_be_internationally_dialled(INTERNATIONAL_TOLL_FREE))

    def testIsAlphaNumber(self):
        self.assertTrue(phonenumbers.is_alpha_number("1800 six-flags"))
        self.assertTrue(phonenumbers.is_alpha_number("1800 six-flags ext. 1234"))
        self.assertTrue(phonenumbers.is_alpha_number("+800 six-flags"))
        self.assertFalse(phonenumbers.is_alpha_number("1800 123-1234"))
        self.assertFalse(phonenumbers.is_alpha_number("1800 123-1234 extension: 1234"))
        self.assertFalse(phonenumbers.is_alpha_number("+800 1234-1234"))
        # Python version extra test
        self.assertFalse(phonenumbers.is_alpha_number(""))

    def testMetadataEquality(self):
        # Python version extra tests for equality against other types
        desc1 = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        desc2 = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        desc3 = PhoneNumberDesc(national_number_pattern="\\d{4,7}",
                                possible_number_pattern="\\d{7}",
                                example_number="1234567")
        self.assertNotEqual(desc1, None)
        self.assertNotEqual(desc1, "")
        self.assertEqual(desc1, desc2)
        self.assertNotEqual(desc1, desc3)
        self.assertTrue(desc1 != desc3)
        desc1.merge_from(desc3)
        self.assertEqual(desc1, desc3)
        self.assertEqual(r"PhoneNumberDesc(national_number_pattern='\\d{4,7}', " +
                         r"possible_number_pattern='\\d{7}', example_number='1234567')",
                         str(desc3))
        nf1 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['1'])
        nf2 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['1'])
        nf3 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['2'],
                           national_prefix_formatting_rule='$NP',
                           domestic_carrier_code_formatting_rule='$NP')
        self.assertEqual(nf1, nf2)
        self.assertNotEqual(nf1, nf3)
        self.assertNotEqual(nf1, None)
        self.assertNotEqual(nf1, "")
        self.assertNotEqual(nf1, 123)
        self.assertTrue(nf1 != nf3)
        nf1.merge_from(nf3)
        # Still not equal because the leading digits are combined not overwritten
        self.assertNotEqual(nf1, nf3)

        metadata1 = PhoneMetadata("XY", preferred_international_prefix=u'9123', register=False)
        metadata2 = PhoneMetadata("XY", preferred_international_prefix=u'9123', register=False)
        metadata3 = PhoneMetadata("XY", preferred_international_prefix=u'9100', register=False)
        self.assertEqual(metadata1, metadata2)
        self.assertNotEqual(metadata1, metadata3)
        self.assertTrue(metadata1 != metadata3)
        self.assertNotEqual(metadata1, None)
        self.assertNotEqual(metadata1, "")
        self.assertNotEqual(metadata1, 123)

    def testMetadataAsString(self):
        # Python version extra tests for string conversions
        metadata = PhoneMetadata.region_metadata["AU"]
        self.assertEqual('\\' + 'd',
                         metadata.number_format[0].pattern[1:3])
        self.assertEqual(r"""NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format=%(u)s'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=%(u)s'\\1')""" % {'u': _UP},
                         str(metadata.number_format[0]))
        self.assertEqual(repr(metadata.number_format[0]),
                         str(metadata.number_format[0]))
        self.assertEqual(r"""PhoneNumberDesc(national_number_pattern='[1-578]\\d{4,14}', possible_number_pattern='\\d{5,15}')""",
                         str(metadata.general_desc))
        self.assertEqual(repr(metadata.general_desc), str(metadata.general_desc))

        # Create some metadata, including an invalid example number
        metadataXX = PhoneMetadata("XX",
                                   personal_number=PhoneNumberDesc(example_number='12'),
                                   preferred_international_prefix='9123',
                                   national_prefix='1',
                                   preferred_extn_prefix='2',
                                   national_prefix_for_parsing='1',
                                   national_prefix_transform_rule='',
                                   number_format=[NumberFormat()],
                                   intl_number_format=[NumberFormat()],
                                   leading_digits='123',
                                   leading_zero_possible=True,
                                   register=False)
        self.assertEqual("""PhoneMetadata(id='XX', country_code=-1, international_prefix=None,
    general_desc=None,
    fixed_line=None,
    mobile=None,
    toll_free=None,
    premium_rate=None,
    shared_cost=None,
    personal_number=PhoneNumberDesc(example_number='12'),
    voip=None,
    pager=None,
    uan=None,
    emergency=None,
    voicemail=None,
    no_international_dialling=None,
    preferred_international_prefix='9123',
    national_prefix='1',
    preferred_extn_prefix='2',
    national_prefix_for_parsing='1',
    national_prefix_transform_rule='',
    number_format=[NumberFormat(pattern=None, format=None)],
    intl_number_format=[NumberFormat(pattern=None, format=None)],
    leading_digits='123',
    leading_zero_possible=True)""",
                          str(metadataXX))

        # Coverage test: invalid example number for region
        PhoneMetadata.region_metadata['XX'] = metadataXX
        phonenumberutil.SUPPORTED_REGIONS.add("XX")
        self.assertTrue(phonenumbers.example_number_for_type("XX", PhoneNumberType.PERSONAL_NUMBER) is None)
        phonenumberutil.SUPPORTED_REGIONS.remove('XX')
        del PhoneMetadata.region_metadata['XX']

        # And now the grand finale: check a real metadata example
        self.assertEqual(r"""PhoneMetadata(id='AU', country_code=61, international_prefix='001[12]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-578]\\d{4,14}', possible_number_pattern='\\d{5,15}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2378]\\d{8}', possible_number_pattern='\\d{9}'),
    mobile=PhoneNumberDesc(national_number_pattern='4\\d{8}', possible_number_pattern='\\d{9}'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0126]\\d{6}', possible_number_pattern='\\d{10}'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format=%(u)s'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=%(u)s'\\1'),
        NumberFormat(pattern='(\\d{1})(\\d{4})(\\d{4})', format=%(u)s'\\1 \\2 \\3', leading_digits_pattern=['[2-478]'], national_prefix_formatting_rule=%(u)s'0\\1')])""" % {'u': _UP},
                          str(metadata))

    def testMetadataEval(self):
        # Python version extra tests for string conversions
        metadata = PhoneMetadata.region_metadata["AU"]
        new_number_format = eval(repr(metadata.number_format[0]))
        self.assertEqual(new_number_format, metadata.number_format[0])
        new_general_desc = eval(repr(metadata.general_desc))
        self.assertEqual(new_general_desc, metadata.general_desc)
        new_metadata = eval(repr(metadata))
        self.assertEqual(new_metadata, metadata)

        PhoneMetadata("XY",
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   possible_number_pattern='\\d{4,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      possible_number_pattern='\\d{4,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u'9123',
                      register=True)
        self.assertRaises(Exception, PhoneMetadata, *("XY",),
                          **{'preferred_international_prefix': '9999',
                             'register': True})
        self.assertTrue(phonenumbers.example_number_for_type('XY', PhoneNumberType.PERSONAL_NUMBER) is None)

    def testCoverage(self):
        # Python version extra tests
        self.assertTrue(phonenumberutil._region_code_for_number_from_list(GB_NUMBER, ("XX",)) is None)
        self.assertEqual((0, "abcdef"),
                          phonenumberutil._extract_country_code("abcdef"))
        metadata = PhoneMetadata.region_metadata["AU"]
        number = PhoneNumber()
        self.assertEqual((0, u""),
                         phonenumberutil._maybe_extract_country_code("",
                                                                     metadata,
                                                                     False,
                                                                     number))
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, ""),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize("", "011"))
        self.assertFalse(phonenumberutil._check_region_for_parsing("", "cs"))

        metadataXY = PhoneMetadata("XY",
                                   general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                                possible_number_pattern='\\d{4,10}'),
                                   national_prefix_for_parsing=u'0(1|2|3)(4|5|6)',
                                   national_prefix_transform_rule=u'\\2',
                                   register=False)
        self.assertEqual(('1', '41234567', True),
                         phonenumberutil._maybe_strip_national_prefix_carrier_code("0141234567",
                                                                                   metadataXY))
        self.assertEqual(('', '01412345', False),
                         phonenumberutil._maybe_strip_national_prefix_carrier_code("01412345",
                                                                                   metadataXY))

        # Temporarily insert invalid example number
        metadata800 = PhoneMetadata.country_code_metadata[800]
        saved_example = metadata800.general_desc.example_number
        metadata800.general_desc.example_number = '01'
        self.assertTrue(phonenumbers.example_number_for_non_geo_entity(800) is None)
        metadata800.general_desc.example_number = saved_example

        self.assertFalse(phonenumbers.phonenumberutil._raw_input_contains_national_prefix("077", "0", "JP"))

        # Temporarily change formatting rule
        metadataGB = PhoneMetadata.region_metadata["GB"]
        saved_rule = metadataGB.number_format[0].national_prefix_formatting_rule
        metadataGB.number_format[0].national_prefix_formatting_rule = u'(\\1)'
        numberWithoutNationalPrefixGB = phonenumbers.parse("2087654321", "GB", keep_raw_input=True)
        self.assertEqual("(20) 8765 4321",
                         phonenumbers.format_in_original_format(numberWithoutNationalPrefixGB, "GB"))
        metadataGB.number_format[0].national_prefix_formatting_rule = saved_rule
