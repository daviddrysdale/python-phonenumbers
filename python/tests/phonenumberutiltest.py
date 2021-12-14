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
import pickle

import phonenumbers
from phonenumbers import PhoneNumber, PhoneMetadata
from phonenumbers import FrozenPhoneNumber, PhoneNumberDesc
from phonenumbers import PhoneNumberType, PhoneNumberFormat, NumberParseException
from phonenumbers import ValidationResult, NumberFormat, CountryCodeSource
from phonenumbers import region_code_for_country_code, MatchType
# Access internal functions of phonenumberutil.py
from phonenumbers import phonenumberutil, shortnumberinfo
from phonenumbers.phonenumberutil import NumberParseException
from phonenumbers.util import u, to_long
from .testmetadatatest import TestMetadataTestCase


# Set up some test numbers to re-use.
ALPHA_NUMERIC_NUMBER = FrozenPhoneNumber(country_code=1, national_number=80074935247)
AE_UAN = FrozenPhoneNumber(country_code=971, national_number=600123456)
AR_MOBILE = FrozenPhoneNumber(country_code=54, national_number=91187654321)
AR_NUMBER = FrozenPhoneNumber(country_code=54, national_number=1187654321)
AU_NUMBER = FrozenPhoneNumber(country_code=61, national_number=236618300)
BS_MOBILE = FrozenPhoneNumber(country_code=1, national_number=2423570000)
BS_NUMBER = FrozenPhoneNumber(country_code=1, national_number=2423651234)
# Note that this is the same as the example number for DE in the metadata.
DE_NUMBER = FrozenPhoneNumber(country_code=49, national_number=30123456)
DE_SHORT_NUMBER = FrozenPhoneNumber(country_code=49, national_number=1234)
GB_MOBILE = FrozenPhoneNumber(country_code=44, national_number=7912345678)
GB_NUMBER = FrozenPhoneNumber(country_code=44, national_number=2070313000)
IT_MOBILE = FrozenPhoneNumber(country_code=39, national_number=345678901)
IT_NUMBER = FrozenPhoneNumber(country_code=39, national_number=236618300, italian_leading_zero=True)
JP_STAR_NUMBER = FrozenPhoneNumber(country_code=81, national_number=2345)
# Numbers to test the formatting rules from Mexico.
MX_MOBILE1 = FrozenPhoneNumber(country_code=52, national_number=12345678900)
MX_MOBILE2 = FrozenPhoneNumber(country_code=52, national_number=15512345678)
MX_NUMBER1 = FrozenPhoneNumber(country_code=52, national_number=3312345678)
MX_NUMBER2 = FrozenPhoneNumber(country_code=52, national_number=8211234567)
NZ_NUMBER = FrozenPhoneNumber(country_code=64, national_number=33316005)
SG_NUMBER = FrozenPhoneNumber(country_code=65, national_number=65218000)
# A too-long and hence invalid US number.
US_LONG_NUMBER = FrozenPhoneNumber(country_code=1, national_number=65025300001)
US_NUMBER = FrozenPhoneNumber(country_code=1, national_number=6502530000)
US_PREMIUM = FrozenPhoneNumber(country_code=1, national_number=9002530000)
# Too short, but still possible US numbers.
US_LOCAL_NUMBER = FrozenPhoneNumber(country_code=1, national_number=2530000)
US_SHORT_BY_ONE_NUMBER = FrozenPhoneNumber(country_code=1, national_number=650253000)
US_TOLLFREE = FrozenPhoneNumber(country_code=1, national_number=8002530000)
US_SPOOF = FrozenPhoneNumber(country_code=1, national_number=0)
US_SPOOF_WITH_RAW_INPUT = FrozenPhoneNumber(country_code=1, national_number=0, raw_input="000-000-0000")
UZ_FIXED_LINE = FrozenPhoneNumber(country_code=998, national_number=612201234)
UZ_MOBILE = FrozenPhoneNumber(country_code=998, national_number=950123456)
INTERNATIONAL_TOLL_FREE = FrozenPhoneNumber(country_code=800, national_number=12345678)
# We set this to be the same length as numbers for the other non-geographical
# country prefix that we have in our test metadata. However, this is not
# considered valid because they differ in their country calling code.
INTERNATIONAL_TOLL_FREE_TOO_LONG = FrozenPhoneNumber(country_code=800, national_number=123456789)
UNIVERSAL_PREMIUM_RATE = FrozenPhoneNumber(country_code=979, national_number=123456789)
UNKNOWN_COUNTRY_CODE_NO_RAW_INPUT = FrozenPhoneNumber(country_code=2, national_number=12345)
# A number with an invalid region code
XY_NUMBER = FrozenPhoneNumber(country_code=999, national_number=1234567890)


class PhoneNumberUtilTest(TestMetadataTestCase):
    """Unit tests for phonenumbers/__init__.py

    Note that these tests use the test metadata, not the normal metadata file,
    so should not be used for regression test purposes - these tests are
    illustrative only and test functionality.
    """
    def testSupportedRegions(self):
        self.assertTrue(len(phonenumbers.SUPPORTED_REGIONS) > 0)
        # Python version extra test
        # Check the pseudo-code for non-geographic entities is not supported
        self.assertFalse("001" in phonenumbers.SUPPORTED_REGIONS)
        # Check a non-US NANPA country is correctly listed as supported
        self.assertTrue("BS" in phonenumbers.SUPPORTED_REGIONS)

    def testGetSupportedGlobalNetworkCallingCodes(self):
        globalNetworkCallingCodes = phonenumbers.COUNTRY_CODES_FOR_NON_GEO_REGIONS
        self.assertTrue(len(globalNetworkCallingCodes) > 0)
        for callingCode in globalNetworkCallingCodes:
            self.assertTrue(callingCode > 0)
            self.assertEqual("001", region_code_for_country_code(callingCode))

    def testGetSupportedCallingCodes(self):
        callingCodes = phonenumbers.supported_calling_codes()
        self.assertTrue(len(callingCodes) > 0)
        for callingCode in callingCodes:
            self.assertTrue(callingCode > 0)
            self.assertTrue(region_code_for_country_code(callingCode) != "ZZ")
        # There should be more than just the global network calling codes in this set.
        self.assertTrue(len(callingCodes) > len(phonenumbers.COUNTRY_CODES_FOR_NON_GEO_REGIONS))
        # But they should be included. Testing one of them.
        self.assertTrue(979 in callingCodes)

    def testGetSupportedTypesForRegion(self):
        self.assertTrue(PhoneNumberType.FIXED_LINE in phonenumbers.supported_types_for_region("BR"))
        # Our test data has no mobile numbers for Brazil.
        self.assertFalse(PhoneNumberType.MOBILE in phonenumbers.supported_types_for_region("BR"))
        # UNKNOWN should never be returned.
        self.assertFalse(PhoneNumberType.UNKNOWN in phonenumbers.supported_types_for_region("BR"))
        # In the US, many numbers are classified as FIXED_LINE_OR_MOBILE; but we don't want to expose
        # this as a supported type, instead we say FIXED_LINE and MOBILE are both present.
        self.assertTrue(PhoneNumberType.FIXED_LINE in phonenumbers.supported_types_for_region("US"))
        self.assertTrue(PhoneNumberType.MOBILE in phonenumbers.supported_types_for_region("US"))
        self.assertFalse(PhoneNumberType.FIXED_LINE_OR_MOBILE in phonenumbers.supported_types_for_region("US"))

        # Test the invalid region code.
        self.assertEqual(0, len(phonenumbers.supported_types_for_region("ZZ")))

    def testGetSupportedTypesForNonGeoEntity(self):
        # No data exists for 999 at all, no types should be returned.
        self.assertEqual(0, len(phonenumbers.supported_types_for_non_geo_entity(999)))
        typesFor979 = phonenumbers.supported_types_for_non_geo_entity(979)
        self.assertTrue(PhoneNumberType.PREMIUM_RATE in typesFor979)
        self.assertFalse(PhoneNumberType.MOBILE in typesFor979)
        self.assertFalse(PhoneNumberType.UNKNOWN in typesFor979)

    def testGetInstanceLoadUSMetadata(self):
        metadata = PhoneMetadata.metadata_for_region("US")
        self.assertEqual("US", metadata.id)
        self.assertEqual(1, metadata.country_code)
        self.assertEqual("011", metadata.international_prefix)
        self.assertTrue(metadata.national_prefix is not None)
        self.assertEqual(2, len(metadata.number_format))
        self.assertEqual("(\\d{3})(\\d{3})(\\d{4})", metadata.number_format[1].pattern)
        self.assertEqual("\\1 \\2 \\3", metadata.number_format[1].format)
        self.assertEqual("[13-689]\\d{9}|2[0-35-9]\\d{8}",
                         metadata.general_desc.national_number_pattern)
        self.assertEqual("[13-689]\\d{9}|2[0-35-9]\\d{8}", metadata.fixed_line.national_number_pattern)
        self.assertEqual(1, len(metadata.general_desc.possible_length))
        self.assertEqual(10, metadata.general_desc.possible_length[0])
        # Python version: each number type description has its own possible_length value,
        # rather than inheriting from the general_desc (like the Java code does).
        self.assertEqual(1, len(metadata.toll_free.possible_length))
        self.assertEqual(10, metadata.toll_free.possible_length[0])
        self.assertEqual("900\\d{7}", metadata.premium_rate.national_number_pattern)
        # No shared-cost data is available, so it should be initialised to None.
        self.assertEqual(None, metadata.shared_cost)

    def testGetInstanceLoadDEMetadata(self):
        metadata = PhoneMetadata.metadata_for_region("DE")
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
        self.assertEqual(2, len(metadata.general_desc.possible_length_local_only))
        self.assertEqual(8, len(metadata.general_desc.possible_length))
        # Python version: each number type description has its own possible_length value,
        # rather than inheriting from the general_desc (like the Java code does).
        self.assertEqual(8, len(metadata.fixed_line.possible_length))
        self.assertEqual(2, len(metadata.mobile.possible_length))
        self.assertEqual("(?:[24-6]\\d{2}|3[03-9]\\d|[789](?:0[2-9]|[1-9]\\d))\\d{1,8}",
                         metadata.fixed_line.national_number_pattern)
        self.assertEqual("30123456", metadata.fixed_line.example_number)
        self.assertEqual(10, metadata.toll_free.possible_length[0])
        self.assertEqual("900([135]\\d{6}|9\\d{7})", metadata.premium_rate.national_number_pattern)

    def testGetInstanceLoadARMetadata(self):
        metadata = PhoneMetadata.metadata_for_region("AR")
        self.assertEqual("AR", metadata.id)
        self.assertEqual(54, metadata.country_code)
        self.assertEqual("00", metadata.international_prefix)
        self.assertEqual("0", metadata.national_prefix)
        self.assertEqual("0(?:(11|343|3715)15)?", metadata.national_prefix_for_parsing)
        self.assertEqual("9\\1", metadata.national_prefix_transform_rule)
        self.assertEqual("\\2 15 \\3-\\4", metadata.number_format[2].format)
        self.assertEqual("(\\d)(\\d{4})(\\d{2})(\\d{4})",
                         metadata.number_format[3].pattern)
        self.assertEqual("(\\d)(\\d{4})(\\d{2})(\\d{4})",
                         metadata.intl_number_format[3].pattern)
        self.assertEqual("\\1 \\2 \\3 \\4", metadata.intl_number_format[3].format)

    def testGetInstanceLoadInternationalTollFreeMetadata(self):
        metadata = PhoneMetadata.metadata_for_nongeo_region(800)
        self.assertEqual("001", metadata.id)
        self.assertEqual(800, metadata.country_code)
        self.assertEqual("\\1 \\2", metadata.number_format[0].format)
        self.assertEqual("(\\d{4})(\\d{4})", metadata.number_format[0].pattern)
        self.assertEqual(0, len(metadata.general_desc.possible_length_local_only))
        self.assertEqual(1, len(metadata.general_desc.possible_length))
        self.assertEqual("12345678", metadata.toll_free.example_number)

    def testIsNumberGeographical(self):
        self.assertFalse(phonenumberutil.is_number_geographical(BS_MOBILE))  # Bahamas, mobile phone number.
        self.assertTrue(phonenumberutil.is_number_geographical(AU_NUMBER))  # Australian fixed line number.
        self.assertFalse(phonenumberutil.is_number_geographical(INTERNATIONAL_TOLL_FREE))  # International toll free number

        # We test that mobile phone numbers in relevant regions are indeed
        # considered geographical.
        self.assertTrue(phonenumberutil.is_number_geographical(AR_MOBILE))  # Argentina, mobile phone number.
        self.assertTrue(phonenumberutil.is_number_geographical(MX_MOBILE1))  # Mexico, mobile phone number.
        self.assertTrue(phonenumberutil.is_number_geographical(MX_MOBILE2))  # Mexico, another mobile phone number.

    def testGetLengthOfGeographicalAreaCode(self):
        # Google MTV, which has area code "650".
        self.assertEqual(3, phonenumbers.length_of_geographical_area_code(US_NUMBER))
        # A North America toll-free number, which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(US_TOLLFREE))
        # Google London, which has area code "20".
        self.assertEqual(2, phonenumbers.length_of_geographical_area_code(GB_NUMBER))
        # A mobile number in the UK does not have an area code (by default,
        # mobile numbers do not, unless they have been added to our list of
        # exceptions).
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(GB_MOBILE))
        # Google Buenos Aires, which has area code "11".
        self.assertEqual(2, phonenumbers.length_of_geographical_area_code(AR_NUMBER))
        # A mobile number in Argentina also has an area code.
        self.assertEqual(3, phonenumbers.length_of_geographical_area_code(AR_MOBILE))
        # Google Sydney, which has area code "2".
        self.assertEqual(1, phonenumbers.length_of_geographical_area_code(AU_NUMBER))
        # Italian numbers - there is no national prefix, but it still has an area code.
        self.assertEqual(2, phonenumbers.length_of_geographical_area_code(IT_NUMBER))
        # Google Singapore. Singapore has no area code and no national prefix.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(SG_NUMBER))
        # An invalid US number (1 digit shorter), which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(US_SHORT_BY_ONE_NUMBER))
        # An international toll free number, which has no area code.
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(INTERNATIONAL_TOLL_FREE))
        # A mobile number from China is geographical, but does not have an area code.
        cnMobile = PhoneNumber(country_code=86, national_number=18912341234)
        self.assertEqual(0, phonenumbers.length_of_geographical_area_code(cnMobile))

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
        number = PhoneNumber(country_code=123, national_number=6502530000)
        self.assertEqual(0, phonenumbers.length_of_national_destination_code(number))

        # An international toll free number, which has NDC "1234".
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(INTERNATIONAL_TOLL_FREE))

        # A mobile number from China is geographical, but does not have an area
        # code: however it still can be considered to have a national
        # destination code.
        cnMobile = PhoneNumber(country_code=86, national_number=18912341234)
        self.assertEqual(3, phonenumbers.length_of_national_destination_code(cnMobile))

        # Python version extra test
        # A number with an extension; still has NDC "7912"
        number2 = PhoneNumber()
        number2.merge_from(GB_MOBILE)
        number2.extension = "1234"
        self.assertEqual(4, phonenumbers.length_of_national_destination_code(number2))

    def testGetCountryMobileToken(self):
        self.assertEqual("9", phonenumbers.country_mobile_token(phonenumbers.country_code_for_region("AR")))
        # Country calling code for Sweden, which has no mobile token.
        # Python version change: Use GB instead, which exists in the test metadata
        self.assertEqual("", phonenumbers.country_mobile_token(phonenumbers.country_code_for_region("GB")))

    def testGetNationalSignificantNumber(self):
        self.assertEqual("6502530000", phonenumbers.national_significant_number(US_NUMBER))
        # An Italian mobile number.
        self.assertEqual("345678901", phonenumbers.national_significant_number(IT_MOBILE))

        # An Italian fixed line number.
        self.assertEqual("0236618300", phonenumbers.national_significant_number(IT_NUMBER))

        self.assertEqual("12345678", phonenumbers.national_significant_number(INTERNATIONAL_TOLL_FREE))

    def testGetNationalSignificantNumber_ManyLeadingZeros(self):
        number = PhoneNumber(country_code=1, national_number=650, italian_leading_zero=True, number_of_leading_zeros=2)
        self.assertEqual("00650", phonenumbers.national_significant_number(number))

        # Set a bad value; we shouldn't crash, we shouldn't output any leading zeros at all.
        number.number_of_leading_zeros = -3
        self.assertEqual("650", phonenumbers.national_significant_number(number))

    def testGetExampleNumber(self):
        self.assertEqual(DE_NUMBER, phonenumbers.example_number("DE"))

        self.assertEqual(DE_NUMBER, phonenumbers.example_number_for_type("DE", PhoneNumberType.FIXED_LINE))
        # Should return the same response if asked for FIXED_LINE_OR_MOBILE too.
        self.assertEqual(DE_NUMBER,
                         phonenumbers.example_number_for_type("DE", PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.FIXED_LINE) is not None)
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.MOBILE) is not None)
        # We have data for the US, but no data for VOICEMAIL, so return null.
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.VOICEMAIL) is None)
        # CS is an invalid region, so we have no data for it.
        self.assertTrue(phonenumbers.example_number_for_type("CS", PhoneNumberType.MOBILE) is None)
        # Python version extra test
        self.assertTrue(phonenumbers.example_number_for_type("US", PhoneNumberType.UNKNOWN) is None)

        # RegionCode 001 is reserved for supporting non-geographical country
        # calling code. We don't support getting an example number for it with
        # this method.
        self.assertTrue(phonenumbers.example_number("001") is None)

    def testGetInvalidExampleNumber(self):
        # RegionCode 001 is reserved for supporting non-geographical country
        # calling codes. We don't support getting an invalid example number
        # for it with invalid_example_number.
        self.assertTrue(phonenumbers.invalid_example_number("001") is None)
        self.assertTrue(phonenumbers.invalid_example_number("CS") is None)
        usInvalidNumber = phonenumbers.invalid_example_number("US")
        self.assertEqual(1, usInvalidNumber.country_code)
        self.assertFalse(usInvalidNumber.national_number == 0)

    def testGetExampleNumberForNonGeoEntity(self):
        self.assertEqual(INTERNATIONAL_TOLL_FREE, phonenumbers.example_number_for_non_geo_entity(800))
        self.assertEqual(UNIVERSAL_PREMIUM_RATE, phonenumbers.example_number_for_non_geo_entity(979))
        # Python version extra test
        self.assertTrue(phonenumbers.example_number_for_non_geo_entity(666) is None)

    def testGetExampleNumberWithoutRegion(self):
        # In our test metadata we don't cover all types: in our real metadata, we do.
        self.assertTrue(phonenumbers.example_number_for_type(None, PhoneNumberType.FIXED_LINE) is not None)
        self.assertTrue(phonenumbers.example_number_for_type(None, PhoneNumberType.MOBILE) is not None)
        self.assertTrue(phonenumbers.example_number_for_type(None, PhoneNumberType.PREMIUM_RATE) is not None)
        # Python version extra test: temporarily drop SUPPORTED_REGIONS to check
        # that example_number_for_type() falls back to non-geo numbers.
        saved = phonenumberutil.SUPPORTED_REGIONS
        phonenumberutil.SUPPORTED_REGIONS = set()
        self.assertTrue(phonenumbers.example_number_for_type(None, PhoneNumberType.TOLL_FREE) is not None)
        phonenumberutil.SUPPORTED_REGIONS = saved

    def testConvertAlphaCharactersInNumber(self):
        input = "1800-ABC-DEF"
        # Alpha chars are converted to digits; everything else is left untouched.
        expectedOutput = "1800-222-333"
        self.assertEqual(expectedOutput, phonenumberutil.convert_alpha_characters_in_number(input))

    def testNormaliseRemovePunctuation(self):
        inputNumber = u("034-56&+#2\u00AD34")
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
        inputNumber = u("\uFF125\u0665")
        expectedOutput = "255"
        self.assertEqual(expectedOutput,
                         phonenumberutil._normalize(inputNumber),
                         msg="Conversion did not correctly replace non-latin digits")
        # Eastern-Arabic digits.
        inputNumber = u("\u06F52\u06F0")
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

    def testNormaliseStripNonDiallableCharacters(self):
        inputNumber = "03*4-56&+1a#234"
        expectedOutput = "03*456+1#234"
        self.assertEqual(expectedOutput,
                         phonenumberutil.normalize_diallable_chars_only(inputNumber),
                         msg="Conversion did not correctly remove non-diallable characters")

    def testFormatUSNumber(self):
        self.assertEqual("650 253 0000", phonenumbers.format_number(US_NUMBER, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 650 253 0000", phonenumbers.format_number(US_NUMBER, PhoneNumberFormat.INTERNATIONAL))

        self.assertEqual("800 253 0000", phonenumbers.format_number(US_TOLLFREE, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 800 253 0000", phonenumbers.format_number(US_TOLLFREE, PhoneNumberFormat.INTERNATIONAL))

        self.assertEqual("900 253 0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+1 900 253 0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("tel:+1-900-253-0000", phonenumbers.format_number(US_PREMIUM, PhoneNumberFormat.RFC3966))
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
        deNumber = PhoneNumber(country_code=49, national_number=301234)
        self.assertEqual("030/1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 30/1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("tel:+49-30-1234", phonenumbers.format_number(deNumber, PhoneNumberFormat.RFC3966))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = to_long(291123)
        self.assertEqual("0291 123", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 291 123", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = to_long(29112345678)
        self.assertEqual("0291 12345678", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 291 12345678", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))

        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = to_long(912312345)
        self.assertEqual("09123 12345", phonenumbers.format_number(deNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("+49 9123 12345", phonenumbers.format_number(deNumber, PhoneNumberFormat.INTERNATIONAL))
        deNumber.clear()
        deNumber.country_code = 49
        deNumber.national_number = to_long(80212345)
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

        auNumber = PhoneNumber(country_code=61, national_number=1800123456)
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

        # Testing preferred international prefixes with ~ are supported (designates waiting).
        self.assertEqual("8~10 39 02 3661 8300",
                         phonenumbers.format_out_of_country_calling_number(IT_NUMBER, "UZ"))

    def testFormatOutOfCountryKeepingAlphaChars(self):
        alphaNumericNumber = PhoneNumber(country_code=1, national_number=8007493524)
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
        alphaNumericNumber.national_number = to_long(827493524)
        alphaNumericNumber.raw_input = "+61 82749-FLAG"
        # This number should have the national prefix fixed.
        self.assertEqual("082749-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.raw_input = "082749-FLAG"
        self.assertEqual("082749-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        alphaNumericNumber.national_number = to_long(18007493524)
        alphaNumericNumber.raw_input = "1-800-SIX-flag"
        # This number should not have the national prefix prefixed, in
        # accordance with the override for this specific formatting rule.
        self.assertEqual("1-800-SIX-FLAG",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AU"))

        # The metadata should not be permanently changed, since we copied it
        # before modifying patterns.  Here we check this.
        alphaNumericNumber.national_number = to_long(1800749352)
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
        alphaNumericNumber.national_number = to_long(18007493524)
        alphaNumericNumber.raw_input = "1-800-SIX-flag"
        # Uses the raw input only.
        self.assertEqual("1-800-SIX-flag",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "DE"))

        # Testing the case of an invalid alpha number.
        alphaNumericNumber.country_code = 1
        alphaNumericNumber.national_number = to_long(80749)
        alphaNumericNumber.raw_input = "180-SIX"
        # No country-code stripping can be done.
        self.assertEqual("00 1 180-SIX",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "DE"))

        # Testing the case of calling from a non-supported region.
        alphaNumericNumber.country_code = 1
        alphaNumericNumber.national_number = to_long(80749)
        alphaNumericNumber.raw_input = "180-SIX"
        # No country-code stripping can be done since the number is invalid.
        self.assertEqual("+1 180-SIX",
                         phonenumbers.format_out_of_country_keeping_alpha_chars(alphaNumericNumber, "AQ"))

    def testFormatWithCarrierCode(self):
        # We only support this for AR in our test metadata, and only for mobile numbers starting with
        # certain values.
        arMobile = PhoneNumber(country_code=54, national_number=92234654321)
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
        # Invalid country code should just get the NSN.
        self.assertEqual("12345",
                         phonenumbers.format_national_number_with_carrier_code(UNKNOWN_COUNTRY_CODE_NO_RAW_INPUT, "89"))
        # Python version extra test
        self.assertEqual("1234567890",
                         phonenumbers.format_national_number_with_carrier_code(XY_NUMBER, "123"))

    def testFormatWithPreferredCarrierCode(self):
        # We only support this for AR in our test metadata.
        arNumber = PhoneNumber()
        arNumber.country_code = 54
        arNumber.national_number = to_long(91234125678)
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
                         'Preferred Domestic Carrier Code: 19',
                         str(arNumber))
        self.assertEqual("PhoneNumber(country_code=54, national_number=91234125678, extension=None, "
                         "italian_leading_zero=None, number_of_leading_zeros=None, "
                         "country_code_source=0, preferred_domestic_carrier_code='19')",
                         repr(arNumber))
        # When the preferred_domestic_carrier_code is present (even when it is
        # just a space), use it instead of the default carrier code passed in.
        arNumber.preferred_domestic_carrier_code = " "
        self.assertEqual("01234   12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, "15"))
        # When the preferred_domestic_carrier_code is present but empty, treat
        # it as unset and use instead the default carrier code passed in.
        arNumber.preferred_domestic_carrier_code = ""
        self.assertEqual("01234 15 12-5678",
                         phonenumbers.format_national_number_with_preferred_carrier_code(arNumber, "15"))
        # We don't support this for the US so there should be no change.
        usNumber = PhoneNumber(country_code=1, national_number=4241231234, preferred_domestic_carrier_code="99")
        self.assertEqual("424 123 1234", phonenumbers.format_number(usNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual("424 123 1234",
                         phonenumbers.format_national_number_with_preferred_carrier_code(usNumber, "15"))

    def testFormatNumberForMobileDialing(self):
        # Numbers are normally dialed in national format in-country, and
        # international format from outside the country.
        self.assertEqual("030123456",
                         phonenumbers.format_number_for_mobile_dialing(DE_NUMBER, "DE", False))
        self.assertEqual("+4930123456",
                         phonenumbers.format_number_for_mobile_dialing(DE_NUMBER, "CH", False))
        deNumberWithExtn = PhoneNumber()
        deNumberWithExtn.merge_from(DE_NUMBER)
        deNumberWithExtn.extension = "1234"
        self.assertEqual("030123456",
                         phonenumbers.format_number_for_mobile_dialing(deNumberWithExtn, "DE", False))
        self.assertEqual("+4930123456",
                         phonenumbers.format_number_for_mobile_dialing(deNumberWithExtn, "CH", False))

        # US toll free numbers are marked as noInternationalDialling in the
        # test metadata for testing purposes.For such numbers, we expect
        # nothing to be returned when the region code is not the same one.
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

        self.assertEqual("+80012345678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "JP", False))
        self.assertEqual("+800 1234 5678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "JP", True))

        # UAE numbers beginning with 600 (classified as UAN) need to be dialled without +971 locally.
        self.assertEqual("+971600123456",
                         phonenumbers.format_number_for_mobile_dialing(AE_UAN, "JP", False))
        self.assertEqual("600123456",
                         phonenumbers.format_number_for_mobile_dialing(AE_UAN, "AE", False))

        self.assertEqual("+523312345678",
                         phonenumbers.format_number_for_mobile_dialing(MX_NUMBER1, "MX", False))
        self.assertEqual("+523312345678",
                         phonenumbers.format_number_for_mobile_dialing(MX_NUMBER1, "US", False))

        # Test whether Uzbek phone numbers are returned in international format even when dialled from
        # same region or other regions.
        self.assertEqual("+998612201234",
                         phonenumbers.format_number_for_mobile_dialing(UZ_FIXED_LINE, "UZ", False))
        self.assertEqual("+998950123456",
                         phonenumbers.format_number_for_mobile_dialing(UZ_MOBILE, "UZ", False))
        self.assertEqual("+998950123456",
                         phonenumbers.format_number_for_mobile_dialing(UZ_MOBILE, "US", False))

        # Non-geographical numbers should always be dialed in international format.
        self.assertEqual("+80012345678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "US", False))
        self.assertEqual("+80012345678",
                         phonenumbers.format_number_for_mobile_dialing(INTERNATIONAL_TOLL_FREE, "001", False))

        # Test that a short number is formatted correctly for mobile dialing
        # within the region, and is not diallable from outside the region.
        deShortNumber = PhoneNumber(country_code=49, national_number=123)
        self.assertEqual("123", phonenumbers.format_number_for_mobile_dialing(deShortNumber, "DE", False))
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(deShortNumber, "IT", False))

        # Test the special logic for NANPA countries, for which regular length phone numbers are always
        # output in international format, but short numbers are in national format.
        self.assertEqual("+16502530000", phonenumbers.format_number_for_mobile_dialing(US_NUMBER, "US", False))
        self.assertEqual("+16502530000", phonenumbers.format_number_for_mobile_dialing(US_NUMBER, "CA", False))
        self.assertEqual("+16502530000", phonenumbers.format_number_for_mobile_dialing(US_NUMBER, "BR", False))
        usShortNumber = PhoneNumber(country_code=1, national_number=911)
        self.assertEqual("911", phonenumbers.format_number_for_mobile_dialing(usShortNumber, "US", False))
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(usShortNumber, "CA", False))
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(usShortNumber, "BR", False))

        # Test that the Australian emergency number 000 is formatted correctly.
        auNumber = PhoneNumber(country_code=61, national_number=0, italian_leading_zero=True, number_of_leading_zeros=2)
        self.assertEqual("000", phonenumbers.format_number_for_mobile_dialing(auNumber, "AU", False))
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(auNumber, "NZ", False))

        # Python version extra tests
        self.assertNotEqual(-1, str(auNumber).find("Number of leading zeros"))
        number = PhoneNumber()
        number.merge_from(XY_NUMBER)
        self.assertEqual("", phonenumbers.format_number_for_mobile_dialing(number, "US", False))
        number.raw_input = " 123-456-7890"
        self.assertEqual(" 123-456-7890", phonenumbers.format_number_for_mobile_dialing(number, "US", False))

    def testFormatByPattern(self):
        newNumFormat = NumberFormat(pattern="(\\d{3})(\\d{3})(\\d{4})", format="(\\1) \\2-\\3")
        newNumFormat._mutable = True
        newNumberFormats = [newNumFormat]

        self.assertEqual("(650) 253-0000", phonenumbers.format_by_pattern(US_NUMBER, PhoneNumberFormat.NATIONAL,
                                                                          newNumberFormats))
        self.assertEqual("+1 (650) 253-0000", phonenumbers.format_by_pattern(US_NUMBER,
                                                                             PhoneNumberFormat.INTERNATIONAL,
                                                                             newNumberFormats))
        self.assertEqual("tel:+1-650-253-0000", phonenumbers.format_by_pattern(US_NUMBER,
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
        self.assertEqual("tel:+64-3-331-6005;ext=1234", phonenumbers.format_number(nzNumber, PhoneNumberFormat.RFC3966))
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

        # Test the star sign is not removed from or added to the original input by this method.
        starNumber = phonenumbers.parse("*1234", "JP", keep_raw_input=True)
        self.assertEqual("*1234", phonenumbers.format_in_original_format(starNumber, "JP"))
        numberWithoutStar = phonenumbers.parse("1234", "JP", keep_raw_input=True)
        self.assertEqual("1234", phonenumbers.format_in_original_format(numberWithoutStar, "JP"))

        # Test an invalid national number without raw input is just formatted as the national number.
        self.assertEqual("650253000",
                         phonenumbers.format_in_original_format(US_SHORT_BY_ONE_NUMBER, "US"))
        # Python version extra tests
        number101 = phonenumbers.parse("87654321", None, keep_raw_input=True, _check_region=False)
        self.assertEqual("87654321", phonenumbers.format_in_original_format(number101, "US"))
        number102 = PhoneNumber(country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY,
                                country_code=44, national_number=999999999)
        self.assertEqual("999999999",
                         phonenumbers.format_in_original_format(number102, "GB"))

    def testIsPremiumRate(self):
        self.assertEqual(PhoneNumberType.PREMIUM_RATE, phonenumbers.number_type(US_PREMIUM))

        premiumRateNumber = PhoneNumber(country_code=39, national_number=892123)
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 44
        premiumRateNumber.national_number = to_long(9187654321)
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 49
        premiumRateNumber.national_number = to_long(9001654321)
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        premiumRateNumber.clear()
        premiumRateNumber.country_code = 49
        premiumRateNumber.national_number = to_long(90091234567)
        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(premiumRateNumber))

        self.assertEqual(PhoneNumberType.PREMIUM_RATE,
                         phonenumbers.number_type(UNIVERSAL_PREMIUM_RATE))

    def testIsTollFree(self):
        tollFreeNumber = PhoneNumber(country_code=1, national_number=8881234567)
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 39
        tollFreeNumber.national_number = to_long(803123)
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 44
        tollFreeNumber.national_number = to_long(8012345678)
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        tollFreeNumber.clear()
        tollFreeNumber.country_code = 49
        tollFreeNumber.national_number = to_long(8001234567)
        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(tollFreeNumber))

        self.assertEqual(PhoneNumberType.TOLL_FREE,
                         phonenumbers.number_type(INTERNATIONAL_TOLL_FREE))

    def testIsMobile(self):
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(BS_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(GB_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(IT_MOBILE))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(AR_MOBILE))

        mobileNumber = PhoneNumber(country_code=49, national_number=15123456789)
        self.assertEqual(PhoneNumberType.MOBILE, phonenumbers.number_type(mobileNumber))

    def testIsFixedLine(self):
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(BS_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(IT_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(GB_NUMBER))
        self.assertEqual(PhoneNumberType.FIXED_LINE, phonenumbers.number_type(DE_NUMBER))

    def testIsFixedLineAndMobile(self):
        self.assertEqual(PhoneNumberType.FIXED_LINE_OR_MOBILE,
                         phonenumbers.number_type(US_NUMBER))

        fixedLineAndMobileNumber = PhoneNumber(country_code=54, national_number=1987654321)
        self.assertEqual(PhoneNumberType.FIXED_LINE_OR_MOBILE,
                         phonenumbers.number_type(fixedLineAndMobileNumber))

    def testIsSharedCost(self):
        gbNumber = PhoneNumber(country_code=44, national_number=8431231234)
        self.assertEqual(PhoneNumberType.SHARED_COST, phonenumbers.number_type(gbNumber))

    def testIsVoip(self):
        gbNumber = PhoneNumber(country_code=44, national_number=5631231234)
        self.assertEqual(PhoneNumberType.VOIP, phonenumbers.number_type(gbNumber))

    def testIsPersonalNumber(self):
        gbNumber = PhoneNumber(country_code=44, national_number=7031231234)
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
        self.assertTrue(phonenumbers.is_valid_number(UNIVERSAL_PREMIUM_RATE))

        nzNumber = PhoneNumber(country_code=64, national_number=21387835)
        self.assertTrue(phonenumbers.is_valid_number(nzNumber))

    def testIsValidForRegion(self):
        # This number is valid for the Bahamas, but is not a valid US number.
        self.assertTrue(phonenumbers.is_valid_number(BS_NUMBER))
        self.assertTrue(phonenumbers.is_valid_number_for_region(BS_NUMBER, "BS"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(BS_NUMBER, "US"))
        bsInvalidNumber = PhoneNumber(country_code=1, national_number=2421232345)
        # This number is no longer valid.
        self.assertFalse(phonenumbers.is_valid_number(bsInvalidNumber))

        # La Mayotte and Reunion use 'leadingDigits' to differentiate them.
        reNumber = PhoneNumber(country_code=262, national_number=262123456)
        self.assertTrue(phonenumbers.is_valid_number(reNumber))
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        # Now change the number to be a number for La Mayotte.
        reNumber.national_number = to_long(269601234)
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        # This number is no longer valid for La Reunion.
        reNumber.national_number = to_long(269123456)
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertFalse(phonenumbers.is_valid_number(reNumber))
        # However, it should be recognised as from La Mayotte, since it is valid for this region.
        self.assertEqual("YT", phonenumbers.region_code_for_number(reNumber))
        # This number is valid in both places.
        reNumber.national_number = to_long(800123456)
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "YT"))
        self.assertTrue(phonenumbers.is_valid_number_for_region(reNumber, "RE"))
        self.assertTrue(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "001"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "US"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(INTERNATIONAL_TOLL_FREE, "ZZ"))

        invalidNumber = PhoneNumber()
        # Invalid country calling codes.
        invalidNumber.country_code = 3923
        invalidNumber.national_number = to_long(2366)
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "ZZ"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "001"))
        invalidNumber.country_code = 0
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "001"))
        self.assertFalse(phonenumbers.is_valid_number_for_region(invalidNumber, "ZZ"))

        # Python version extra test
        self.assertFalse(phonenumbers.is_valid_number_for_region(reNumber, "US"))

    def testIsNotValidNumber(self):
        self.assertFalse(phonenumbers.is_valid_number(US_LOCAL_NUMBER))

        invalidNumber = PhoneNumber(country_code=39, national_number=23661830000, italian_leading_zero=True)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 44
        invalidNumber.national_number = to_long(791234567)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 49
        invalidNumber.national_number = to_long(1234)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        invalidNumber.country_code = 64
        invalidNumber.national_number = to_long(3316005)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        invalidNumber.clear()
        # Invalid country calling codes.
        invalidNumber.country_code = 3923
        invalidNumber.national_number = to_long(2366)
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))
        invalidNumber.country_code = 0
        self.assertFalse(phonenumbers.is_valid_number(invalidNumber))

        self.assertFalse(phonenumbers.is_valid_number(INTERNATIONAL_TOLL_FREE_TOO_LONG))

    def testGetRegionCodeForCountryCode(self):
        self.assertEqual("US", phonenumbers.region_code_for_country_code(1))
        self.assertEqual("GB", phonenumbers.region_code_for_country_code(44))
        self.assertEqual("DE", phonenumbers.region_code_for_country_code(49))
        self.assertEqual("001", phonenumbers.region_code_for_country_code(800))
        self.assertEqual("001", phonenumbers.region_code_for_country_code(979))

    def testGetRegionCodeForNumber(self):
        self.assertEqual("BS", phonenumbers.region_code_for_number(BS_NUMBER))
        self.assertEqual("US", phonenumbers.region_code_for_number(US_NUMBER))
        self.assertEqual("GB", phonenumbers.region_code_for_number(GB_MOBILE))
        self.assertEqual("001", phonenumbers.region_code_for_number(INTERNATIONAL_TOLL_FREE))
        self.assertEqual("001", phonenumbers.region_code_for_number(UNIVERSAL_PREMIUM_RATE))

    def testGetRegionCodesForCountryCode(self):
        regionCodesForNANPA = phonenumbers.region_codes_for_country_code(1)
        self.assertTrue("US" in regionCodesForNANPA)
        self.assertTrue("BS" in regionCodesForNANPA)
        self.assertTrue("GB" in phonenumbers.region_codes_for_country_code(44))
        self.assertTrue("DE" in phonenumbers.region_codes_for_country_code(49))
        self.assertTrue("001" in phonenumbers.region_codes_for_country_code(800))
        # Test with invalid country calling code.
        self.assertEqual(0, len(phonenumbers.region_codes_for_country_code(-1)))

    def testGetCountryCodeForRegion(self):
        self.assertEqual(1, phonenumbers.country_code_for_region("US"))
        self.assertEqual(64, phonenumbers.country_code_for_region("NZ"))
        self.assertEqual(0, phonenumbers.country_code_for_region(None))
        self.assertEqual(0, phonenumbers.country_code_for_region("ZZ"))
        self.assertEqual(0, phonenumbers.country_code_for_region("001"))
        # CS is already deprecated so the library doesn't support it.
        self.assertEqual(0, phonenumbers.country_code_for_region("CS"))
        # Python version extra test
        self.assertRaises(Exception, phonenumbers.country_code_for_valid_region, *("XY",))

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
        self.assertTrue(phonenumbers.is_possible_number_string("(020) 7031 300", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("7031 3000", "GB"))
        self.assertTrue(phonenumbers.is_possible_number_string("3331 6005", "NZ"))
        self.assertTrue(phonenumbers.is_possible_number_string("+800 1234 5678", "001"))

    def testIsPossibleNumberForType_DifferentTypeLengths(self):
        # We use Argentinian numbers since they have different possible lengths for different types.
        number = PhoneNumber(country_code=54, national_number=12345)
        # Too short for any Argentinian number, including fixed-line.
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))

        # 6-digit numbers are okay for fixed-line.
        number.national_number = 123456
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        # But too short for mobile.
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        # And too short for toll-free.
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.TOLL_FREE))

        # The same applies to 9-digit numbers.
        number.national_number = 123456789
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.TOLL_FREE))

        # 10-digit numbers are universally possible.
        number.national_number = 1234567890
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.TOLL_FREE))

        # 11-digit numbers are only possible for mobile numbers. Note we don't require the leading 9,
        # which all mobile numbers start with, and would be required for a valid mobile number.
        number.national_number = 12345678901
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.TOLL_FREE))

        # Python version extra test:
        # AM numbers have both mobile and fixed-line data, both have local-only lengths
        am_number = PhoneNumber(country_code=374, national_number=12345678)
        self.assertTrue(phonenumbers.is_possible_number_for_type(am_number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        am_number = PhoneNumber(country_code=374, national_number=12345)
        self.assertTrue(phonenumbers.is_possible_number_for_type(am_number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

    def testIsPossibleNumberForType_LocalOnly(self):
        # Here we test a number length which matches a local-only length.
        number = PhoneNumber(country_code=49, national_number=12)
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        # Mobile numbers must be 10 or 11 digits, and there are no local-only lengths.
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))

    def testIsPossibleNumberForType_DataMissingForSizeReasons(self):
        # Here we test something where the possible lengths match the possible lengths of the country
        # as a whole, and hence aren't present in the binary for size reasons - this should still work.
        # Local-only number.
        number = PhoneNumber(country_code=55, national_number=12345678)
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))

        number.national_number = 1234567890
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.UNKNOWN))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))

    def testIsPossibleNumberForType_NumberTypeNotSupportedForRegion(self):
        # There are *no* mobile numbers for this region at all, so we return false.
        number = PhoneNumber(country_code=55, national_number=12345678)
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        # This matches a fixed-line length though.
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

        # There are *no* fixed-line OR mobile numbers for this country calling code at all, so we
        # return false for these.
        number.country_code = 979
        number.national_number = 123456789
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.MOBILE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE))
        self.assertFalse(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self.assertTrue(phonenumbers.is_possible_number_for_type(number, PhoneNumberType.PREMIUM_RATE))

    def testIsPossibleNumberWithReason(self):
        # National numbers for country calling code +1 that are within 7 to 10 digits are possible.
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(US_NUMBER))

        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_with_reason(US_LOCAL_NUMBER))

        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_with_reason(US_LONG_NUMBER))

        number = PhoneNumber(country_code=0, national_number=2530000)
        self.assertEqual(ValidationResult.INVALID_COUNTRY_CODE,
                         phonenumbers.is_possible_number_with_reason(number))

        number.clear()
        number.country_code = 1
        number.national_number = to_long(253000)
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_with_reason(number))

        number.clear()
        number.country_code = 65
        number.national_number = to_long(1234567890)
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_with_reason(number))

        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_with_reason(INTERNATIONAL_TOLL_FREE_TOO_LONG))

    def testIsPossibleNumberForTypeWithReason_DifferentTypeLengths(self):
        # We use Argentinian numbers since they have different possible lengths for different types.
        number = PhoneNumber(country_code=54, national_number=12345)
        # Too short for any Argentinian number.
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))

        # 6-digit numbers are okay for fixed-line.
        number.national_number = 123456
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        # But too short for mobile.
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        # And too short for toll-free.
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.TOLL_FREE))

        # The same applies to 9-digit numbers.
        number.national_number = 123456789
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.TOLL_FREE))

        # 10-digit numbers are universally possible.
        number.national_number = 1234567890
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.TOLL_FREE))

        # 11-digit numbers are only possible for mobile numbers. Note we don't require the leading 9,
        # which all mobile numbers start with, and would be required for a valid mobile number.
        number.national_number = 12345678901
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.TOLL_FREE))

    def testIsPossibleNumberForTypeWithReason_LocalOnly(self):
        # Here we test a number length which matches a local-only length.
        number = PhoneNumber(country_code=49, national_number=12)
        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        # Mobile numbers must be 10 or 11 digits, and there are no local-only lengths.
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))

    def testIsPossibleNumberForTypeWithReason_DataMissingForSizeReasons(self):
        # Here we test something where the possible lengths match the possible lengths of the country
        # as a whole, and hence aren't present in the binary for size reasons - this should still work.
        # Local-only number.
        number = PhoneNumber(country_code=55, national_number=12345678)
        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))

        # Normal-length number.
        number.national_number = 1234567890
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.UNKNOWN))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))

    def testIsPossibleNumberForTypeWithReason_NumberTypeNotSupportedForRegion(self):
        # There are *no* mobile numbers for this region at all, so we return INVALID_LENGTH.
        number = PhoneNumber(country_code=55, national_number=12345678)
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        # This matches a fixed-line length though.
        self.assertEqual(ValidationResult.IS_POSSIBLE_LOCAL_ONLY,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        # This is too short for fixed-line, and no mobile numbers exist.
        number.country_code = 55
        number.national_number = 1234567
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))

        # This is too short for mobile, and no fixed-line numbers exist.
        number.country_code = 882
        number.national_number = 1234567
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))

        # There are *no* fixed-line OR mobile numbers for this country calling code at all, so we
        # return INVALID_LENGTH.
        number.country_code = 979
        number.national_number = 123456789
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.PREMIUM_RATE))

    def testIsPossibleNumberForTypeWithReason_FixedLineOrMobile(self):
        # For FIXED_LINE_OR_MOBILE, a number should be considered valid if it matches the possible
        # lengths for mobile *or* fixed-line numbers.
        number = PhoneNumber(country_code=290, national_number=1234)
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

        number.national_number = 12345
        self.assertEqual(ValidationResult.TOO_SHORT,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.INVALID_LENGTH,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

        number.national_number = 123456
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

        number.national_number = 1234567
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.MOBILE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

        # 8-digit numbers are possible for toll-free and premium-rate numbers only.
        number.national_number = 12345678
        self.assertEqual(ValidationResult.IS_POSSIBLE,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.TOLL_FREE))
        self.assertEqual(ValidationResult.TOO_LONG,
                         phonenumbers.is_possible_number_for_type_with_reason(number, PhoneNumberType.FIXED_LINE_OR_MOBILE))

    def testIsNotPossibleNumber(self):
        self.assertFalse(phonenumbers.is_possible_number(US_LONG_NUMBER))
        self.assertFalse(phonenumbers.is_possible_number(INTERNATIONAL_TOLL_FREE_TOO_LONG))

        number = PhoneNumber(country_code=1, national_number=253000)
        self.assertFalse(phonenumbers.is_possible_number(number))

        number.clear()
        number.country_code = 44
        number.national_number = to_long(300)
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
        tooLongNumber = PhoneNumber(country_code=44, national_number=80123456780123)
        validNumber = PhoneNumber(country_code=44, national_number=8012345678)
        self.assertTrue(phonenumbers.truncate_too_long_number(tooLongNumber))
        self.assertEqual(validNumber, tooLongNumber)

        # IT number 022 3456 7890, but entered with 3 extra digits at the end.
        tooLongNumber.clear()
        tooLongNumber.country_code = 39
        tooLongNumber.national_number = to_long(2234567890123)
        tooLongNumber.italian_leading_zero = True
        validNumber.clear()
        validNumber.country_code = 39
        validNumber.national_number = to_long(2234567890)
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
        numberWithInvalidPrefix = PhoneNumber(country_code=1, national_number=2401234567)
        invalidNumberCopy = PhoneNumber()
        invalidNumberCopy.merge_from(numberWithInvalidPrefix)
        self.assertFalse(phonenumbers.truncate_too_long_number(numberWithInvalidPrefix))
        # Tests the number is not modified.
        self.assertEqual(invalidNumberCopy, numberWithInvalidPrefix)

        # Tests what happens when a too short number is passed in.
        tooShortNumber = PhoneNumber(country_code=1, national_number=1234)
        tooShortNumberCopy = PhoneNumber()
        tooShortNumberCopy.merge_from(tooShortNumber)
        self.assertFalse(phonenumbers.truncate_too_long_number(tooShortNumber))
        # Tests the number is not modified.
        self.assertEqual(tooShortNumberCopy, tooShortNumber)

    def testIsViablePhoneNumber(self):
        self.assertFalse(phonenumberutil._is_viable_phone_number("1"))
        # Only one or two digits before strange non-possible punctuation.
        self.assertFalse(phonenumberutil._is_viable_phone_number("1+1+1"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("80+0"))
        # Two digits is viable.
        self.assertTrue(phonenumberutil._is_viable_phone_number("00"))
        self.assertTrue(phonenumberutil._is_viable_phone_number("111"))
        # Alpha numbers.
        self.assertTrue(phonenumberutil._is_viable_phone_number("0800-4-pizza"))
        self.assertTrue(phonenumberutil._is_viable_phone_number("0800-4-PIZZA"))
        # We need at least three digits before any alpha characters.
        self.assertFalse(phonenumberutil._is_viable_phone_number("08-PIZZA"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("8-PIZZA"))
        self.assertFalse(phonenumberutil._is_viable_phone_number("12. March"))

    def testIsViablePhoneNumberNonAscii(self):
        # Only one or two digits before possible punctuation followed by more digits.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u("1\u300034")))
        self.assertFalse(phonenumberutil._is_viable_phone_number(u("1\u30003+4")))
        # Unicode variants of possible starting character and other allowed punctuation/digits.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u("\uFF081\uFF09\u30003456789")))
        # Testing a leading + is okay.
        self.assertTrue(phonenumberutil._is_viable_phone_number(u("+1\uFF09\u30003456789")))

    def testExtractPossibleNumber(self):
        # Removes preceding funky punctuation and letters but leaves the rest untouched.
        self.assertEqual("0800-345-600", phonenumberutil._extract_possible_number("Tel:0800-345-600"))
        self.assertEqual("0800 FOR PIZZA", phonenumberutil._extract_possible_number("Tel:0800 FOR PIZZA"))
        # Should not remove plus sign
        self.assertEqual("+800-345-600", phonenumberutil._extract_possible_number("Tel:+800-345-600"))
        # Should recognise wide digits as possible start values.
        self.assertEqual(u("\uFF10\uFF12\uFF13"),
                         phonenumberutil._extract_possible_number(u("\uFF10\uFF12\uFF13")))
        # Dashes are not possible start values and should be removed.
        self.assertEqual(u("\uFF11\uFF12\uFF13"),
                         phonenumberutil._extract_possible_number(u("Num-\uFF11\uFF12\uFF13")))
        # If not possible number present, return empty string.
        self.assertEqual("", phonenumberutil._extract_possible_number("Num-...."))
        # Leading brackets are stripped - these are not used when parsing.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000"))

        # Trailing non-alpha-numeric characters should be removed.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000..- .."))
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number("(650) 253-0000."))
        # This case has a trailing RTL char.
        self.assertEqual("650) 253-0000", phonenumberutil._extract_possible_number(u("(650) 253-0000\u200F")))

    def testMaybeStripNationalPrefix(self):
        metadata = PhoneMetadata(id="Test", national_prefix_for_parsing="34", register=False)
        metadata._mutable = True
        metadata.general_desc = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        metadata.general_desc._mutable = True
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
        metadata = PhoneMetadata.metadata_for_region("US")
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
            self.assertEqual("Country Code: 1 National Number: None Country Code Source: 5",
                             str(number))
        except NumberParseException:
            e = sys.exc_info()[1]
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
        except NumberParseException:
            e = sys.exc_info()[1]
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
        except NumberParseException:
            e = sys.exc_info()[1]
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "2345-6789"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.assertEqual(0, ccc,
                             msg="Should not have extracted a country calling code - no international prefix present.")
            self.assertEqual(CountryCodeSource.FROM_DEFAULT_COUNTRY, number.country_code_source,
                             msg="Did not figure out CountryCodeSource correctly")
        except NumberParseException:
            e = sys.exc_info()[1]
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "0119991123456789"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, True, number)
            self.fail("Should have thrown an exception, no valid country calling code present.")
        except NumberParseException:
            # Expected.
            e = sys.exc_info()[1]
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
        except NumberParseException:
            e = sys.exc_info()[1]
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "(1 610) 619 4466"
            countryCallingCode = 1
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, False, number)
            self.assertEqual(countryCallingCode, ccc,
                             msg="Should have extracted the country calling code of the region passed in")
            self.assertEqual(CountryCodeSource.UNSPECIFIED, number.country_code_source)
        except NumberParseException:
            e = sys.exc_info()[1]
            self.fail("Should not have thrown an exception: %s" % e)

        number.clear()
        try:
            phoneNumber = "(1 610) 619 446"
            ccc, numberToFill = phonenumberutil._maybe_extract_country_code(phoneNumber, metadata, False, number)
            self.assertEqual(0, ccc,
                             msg=("Should not have extracted a country calling code - invalid number after " +
                                  "extraction of uncertain country calling code."))
            self.assertEqual(CountryCodeSource.UNSPECIFIED, number.country_code_source)
        except NumberParseException:
            e = sys.exc_info()[1]
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
        except NumberParseException:
            e = sys.exc_info()[1]
            self.fail("Should not have thrown an exception: %s" % e)

    def testParseNationalNumber(self):
        # National prefix attached.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("033316005", "NZ"))
        # Some fields are not filled in by parse when keep_raw_input is not set.
        self.assertEqual(CountryCodeSource.UNSPECIFIED, NZ_NUMBER.country_code_source)

        self.assertEqual(NZ_NUMBER, phonenumbers.parse("33316005", "NZ"))
        # National prefix attached and some formatting present.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("03-331 6005", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("03 331 6005", "NZ"))
        # Test parsing RFC3966 format with a phone context.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:03-331-6005;phone-context=+64", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:331-6005;phone-context=+64-3", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:331-6005;phone-context=+64-3", "US"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("My number is tel:03-331-6005;phone-context=+64", "NZ"))
        # Test parsing RFC3966 format with optional user-defined
        # parameters. The parameters will appear after the context if present.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:03-331-6005;phone-context=+64;a=%A1", "NZ"))
        # Test parsing RFC3966 with an ISDN subaddress.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:03-331-6005;isub=12345;phone-context=+64", "NZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:+64-3-331-6005;isub=12345", "NZ"))
        # Test parsing RFC3966 with "tel:" missing.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("03-331-6005;phone-context=+64", "NZ"))
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

        self.assertEqual(US_LOCAL_NUMBER,
                         phonenumbers.parse("tel:253-0000;phone-context=www.google.com", "US"))
        self.assertEqual(US_LOCAL_NUMBER,
                         phonenumbers.parse("tel:253-0000;isub=12345;phone-context=www.google.com", "US"))
        # This is invalid because no "+" sign is present as part of
        # phone-context. The phone context is simply ignored in this case just
        # as if it contains a domain.
        self.assertEqual(US_LOCAL_NUMBER,
                         phonenumbers.parse("tel:2530000;isub=12345;phone-context=1-650", "US"))
        self.assertEqual(US_LOCAL_NUMBER,
                         phonenumbers.parse("tel:2530000;isub=12345;phone-context=1234.com", "US"))

        nzNumber = PhoneNumber(country_code=64, national_number=64123456)
        self.assertEqual(nzNumber, phonenumbers.parse("64(0)64123456", "NZ"))
        # Check that using a "/" is fine in a phone number.
        self.assertEqual(DE_NUMBER, phonenumbers.parse("301/23456", "DE"))

        # Check it doesn't use the '1' as a country calling code when parsing if the phone number was
        # already possible.
        usNumber = PhoneNumber(country_code=1, national_number=1234567890)
        self.assertEqual(usNumber, phonenumbers.parse("123-456-7890", "US"))

        # Test star numbers. Although this is not strictly valid, we would
        # like to make sure we can parse the output we produce when formatting
        # the number.
        self.assertEqual(JP_STAR_NUMBER, phonenumbers.parse("+81 *2345", "JP"))

        shortNumber = PhoneNumber(country_code=64, national_number=12)
        self.assertEqual(shortNumber, phonenumbers.parse("12", "NZ"))

        # Test for short-code with leading zero for a country which has 0 as national prefix. Ensure
        # it's not interpreted as national prefix if the remaining number length is local-only in
        # terms of length. Example: In GB, length 6-7 are only possible local-only.
        shortNumber.country_code = 44
        shortNumber.national_number = 123456
        shortNumber.italian_leading_zero = True
        self.assertEqual(shortNumber, phonenumbers.parse("0123456", "GB"))

    def testParseNumberWithAlphaCharacters(self):
        # Test case with alpha characters.
        tollfreeNumber = PhoneNumber(country_code=64, national_number=800332005)
        self.assertEqual(tollfreeNumber, phonenumbers.parse("0800 DDA 005", "NZ"))
        premiumNumber = PhoneNumber(country_code=64, national_number=9003326005)
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 DDA 6005", "NZ"))
        # Not enough alpha characters for them to be considered intentional, so they are stripped.
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 6005a", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 600a5", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 332 600A5", "NZ"))
        self.assertEqual(premiumNumber, phonenumbers.parse("0900 a332 600A5", "NZ"))

    def testParseMaliciousInput(self):
        # Lots of leading + signs before the possible number.
        maliciousNumber = '+' * 6000 + "12222-33-244 extensioB 343+"
        try:
            phonenumbers.parse(maliciousNumber, "US")
            self.fail("This should not parse without throwing an exception %s" % maliciousNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(e.error_type,
                             NumberParseException.TOO_LONG,
                             msg="Wrong error type stored in exception.")

        maliciousNumberWithAlmostExt = "200" * 350 + " extensiOB 345"
        try:
            phonenumbers.parse(maliciousNumberWithAlmostExt, "US")
            self.fail("This should not parse without throwing an exception %s" % maliciousNumberWithAlmostExt)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(e.error_type,
                             NumberParseException.TOO_LONG,
                             msg="Wrong error type stored in exception.")

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
        self.assertEqual(US_NUMBER, phonenumbers.parse(u("\uFF0B1 (650) 253-0000"), "SG"))
        # Using a soft hyphen U+00AD
        self.assertEqual(US_NUMBER, phonenumbers.parse(u("1 (650) 253\u00AD0000"), "US"))
        # The whole number, including punctuation, is here represented in full-width form.
        self.assertEqual(US_NUMBER, phonenumbers.parse(u("\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09") +
                                                       u("\u3000\uFF12\uFF15\uFF13\uFF0D\uFF10\uFF10\uFF10") +
                                                       u("\uFF10"),
                                                       "SG"))
        # Using U+30FC dash instead.
        self.assertEqual(US_NUMBER, phonenumbers.parse(u("\uFF0B\uFF11\u3000\uFF08\uFF16\uFF15\uFF10\uFF09") +
                                                       u("\u3000\uFF12\uFF15\uFF13\u30FC\uFF10\uFF10\uFF10") +
                                                       u("\uFF10"),
                                                       "SG"))
        # Using a very strange decimal digit range (Mongolian digits).
        self.assertEqual(US_NUMBER, phonenumbers.parse(u("\u1811 \u1816\u1815\u1810 ") +
                                                       u("\u1812\u1815\u1813 \u1810\u1810\u1810\u1810"),
                                                       "US"))

    def testParseWithLeadingZero(self):
        self.assertEqual(IT_NUMBER, phonenumbers.parse("+39 02-36618 300", "NZ"))
        self.assertEqual(IT_NUMBER, phonenumbers.parse("02-36618 300", "IT"))

        self.assertEqual(IT_MOBILE, phonenumbers.parse("345 678 901", "IT"))

    def testParseNationalNumberArgentina(self):
        # Test parsing mobile numbers of Argentina.
        arNumber = PhoneNumber(country_code=54, national_number=93435551212)
        self.assertEqual(arNumber, phonenumbers.parse("+54 9 343 555 1212", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("0343 15 555 1212", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = to_long(93715654320)
        self.assertEqual(arNumber, phonenumbers.parse("+54 9 3715 65 4320", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("03715 15 65 4320", "AR"))
        self.assertEqual(AR_MOBILE, phonenumbers.parse("911 876 54321", "AR"))

        # Test parsing fixed-line numbers of Argentina.
        self.assertEqual(AR_NUMBER, phonenumbers.parse("+54 11 8765 4321", "AR"))
        self.assertEqual(AR_NUMBER, phonenumbers.parse("011 8765 4321", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = to_long(3715654321)
        self.assertEqual(arNumber, phonenumbers.parse("+54 3715 65 4321", "AR"))
        self.assertEqual(arNumber, phonenumbers.parse("03715 65 4321", "AR"))

        arNumber.clear()
        arNumber.country_code = 54
        arNumber.national_number = to_long(2312340000)
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
        arFromUs = PhoneNumber(country_code=54, national_number=81429712)
        # This test is intentionally constructed such that the number of digit
        # after xx is larger than 7, so that the number won't be mistakenly
        # treated as an extension, as we allow extensions up to 7 digits. This
        # assumption is okay for now as all the countries where a carrier
        # selection code is written in the form of xx have a national
        # significant number of length larger than 7.
        self.assertEqual(arFromUs, phonenumbers.parse("011xx5481429712", "US"))

    def testParseNumbersMexico(self):
        # Test parsing fixed-line numbers of Mexico.
        mxNumber = PhoneNumber(country_code=52, national_number=4499780001)
        self.assertEqual(mxNumber, phonenumbers.parse("+52 (449)978-0001", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("01 (449)978-0001", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("(449)978-0001", "MX"))

        # Test parsing mobile numbers of Mexico.
        mxNumber.clear()
        mxNumber.country_code = 52
        mxNumber.national_number = to_long(13312345678)
        self.assertEqual(mxNumber, phonenumbers.parse("+52 1 33 1234-5678", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("044 (33) 1234-5678", "MX"))
        self.assertEqual(mxNumber, phonenumbers.parse("045 33 1234-5678", "MX"))

    def testFailedParseOnInvalidNumbers(self):
        try:
            sentencePhoneNumber = "This is not a phone number"
            phonenumbers.parse(sentencePhoneNumber, "NZ")
            self.fail("This should not parse without throwing an exception " + sentencePhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        try:
            sentencePhoneNumber = "1 Still not a number"
            phonenumbers.parse(sentencePhoneNumber, "NZ")
            self.fail("This should not parse without throwing an exception " + sentencePhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        try:
            sentencePhoneNumber = "1 MICROSOFT"
            phonenumbers.parse(sentencePhoneNumber, "NZ")
            self.fail("This should not parse without throwing an exception " + sentencePhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        try:
            sentencePhoneNumber = "12 MICROSOFT"
            phonenumbers.parse(sentencePhoneNumber, "NZ")
            self.fail("This should not parse without throwing an exception " + sentencePhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            tooLongPhoneNumber = "01495 72553301873 810104"
            phonenumbers.parse(tooLongPhoneNumber, "GB")
            self.fail("This should not parse without throwing an exception " + tooLongPhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_LONG,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusMinusPhoneNumber = "+---"
            phonenumbers.parse(plusMinusPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusStar = "+***"
            phonenumbers.parse(plusStar, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusStarPhoneNumber = "+*******91"
            phonenumbers.parse(plusStarPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + plusMinusPhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            tooShortPhoneNumber = "+49 0"
            phonenumbers.parse(tooShortPhoneNumber, "DE")
            self.fail("This should not parse without throwing an exception " + tooShortPhoneNumber)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_SHORT_NSN,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            invalidCountryCode = "+210 3456 56789"
            phonenumbers.parse(invalidCountryCode, "NZ")
            self.fail("This is not a recognised region code: should fail: " + invalidCountryCode)
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            plusAndIddAndInvalidCountryCode = "+ 00 210 3 331 6005"
            phonenumbers.parse(plusAndIddAndInvalidCountryCode, "NZ")
            self.fail("This should not parse without throwing an exception.")
        except NumberParseException:
            # Expected this exception. 00 is a correct IDD, but 210 is not a valid country code.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, "ZZ")
            self.fail("'Unknown' region code not allowed: should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, "CS")
            self.fail("Deprecated region code not allowed: should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "123 456 7890"
            phonenumbers.parse(someNumber, None)
            self.fail("Null region code not allowed: should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0044------"
            phonenumbers.parse(someNumber, "GB")
            self.fail("No number provided, only region code: should fail")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0044"
            phonenumbers.parse(someNumber, "GB")
            self.fail("No number provided, only region code: should fail")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "011"
            phonenumbers.parse(someNumber, "US")
            self.fail("Only IDD provided - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            someNumber = "0119"
            phonenumbers.parse(someNumber, "US")
            self.fail("Only IDD provided and then 9 - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_SHORT_AFTER_IDD,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            emptyNumber = ""
            # Invalid region.
            phonenumbers.parse(emptyNumber, "ZZ")
            self.fail("Empty string - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            nullNumber = None
            # Invalid region.
            phonenumbers.parse(nullNumber, "ZZ")
            self.fail("Null string - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        except Exception:
            self.fail("None string - but should not throw an exception.")

        try:
            nullNumber = None
            phonenumbers.parse(nullNumber, "US")
            self.fail("Null string - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")
        except Exception:
            self.fail("None string - but should not throw an exception.")

        try:
            domainRfcPhoneContext = "tel:555-1234;phone-context=www.google.com"
            phonenumbers.parse(domainRfcPhoneContext, "ZZ")
            self.fail("'Unknown' region code not allowed - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            # This is invalid because no "+" sign is present as part of phone-context. This should not
            # succeed in being parsed.
            invalidRfcPhoneContext = "tel:555-1234;phone-context=1-331"
            phonenumbers.parse(invalidRfcPhoneContext, "ZZ")
            self.fail("'Unknown' region code not allowed - should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        try:
            # Only the phone-context symbol is present, but no data.
            invalidRfcPhoneContext = ";phone-context="
            phonenumbers.parse(invalidRfcPhoneContext, "ZZ")
            self.fail("No number is present: should fail.")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

    def testParseNumbersWithPlusWithNoRegion(self):
        # "ZZ" is allowed only if the number starts with a '+' - then the country calling code
        # can be calculated.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+64 3 331 6005", "ZZ"))
        # Test with full-width plus.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse(u("\uFF0B64 3 331 6005"), "ZZ"))
        # Test with normal plus but leading characters that need to be stripped.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("Tel: +64 3 331 6005", "ZZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("+64 3 331 6005", None))
        self.assertEqual(INTERNATIONAL_TOLL_FREE, phonenumbers.parse("+800 1234 5678", None))
        self.assertEqual(UNIVERSAL_PREMIUM_RATE, phonenumbers.parse("+979 123 456 789", None))

        # Test parsing RFC3966 format with a phone context.
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:03-331-6005;phone-context=+64", "ZZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("  tel:03-331-6005;phone-context=+64", "ZZ"))
        self.assertEqual(NZ_NUMBER, phonenumbers.parse("tel:03-331-6005;isub=12345;phone-context=+64", "ZZ"))

        nzNumberWithRawInput = PhoneNumber()
        nzNumberWithRawInput.merge_from(NZ_NUMBER)
        nzNumberWithRawInput.raw_input = "+64 3 331 6005"
        nzNumberWithRawInput.country_code_source = CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN
        self.assertEqual(nzNumberWithRawInput, phonenumbers.parse("+64 3 331 6005", "ZZ", keep_raw_input=True))
        # Null is also allowed for the region code in these cases.
        self.assertEqual(nzNumberWithRawInput, phonenumbers.parse("+64 3 331 6005", None, keep_raw_input=True))

    def testParseNumberTooShortIfNationalPrefixStripped(self):
        # Test that a number whose first digits happen to coincide with the national prefix does not
        # get them stripped if doing so would result in a number too short to be a possible (regular
        # length) phone number for that region.
        byNumber = PhoneNumber(country_code=375, national_number=8123)
        self.assertEqual(byNumber, phonenumbers.parse("8123", "BY"))
        byNumber.national_number = 81234
        self.assertEqual(byNumber, phonenumbers.parse("81234", "BY"))

        # The prefix doesn't get stripped, since the input is a viable 6-digit number, whereas the
        # result of stripping is only 5 digits.
        byNumber.national_number = 812345
        self.assertEqual(byNumber, phonenumbers.parse("812345", "BY"))

        # The prefix gets stripped, since only 6-digit numbers are possible.
        byNumber.national_number = 123456
        self.assertEqual(byNumber, phonenumbers.parse("8123456", "BY"))

    def testParseExtensions(self):
        nzNumber = PhoneNumber(country_code=64, national_number=33316005, extension="3456")
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
        ukNumber = PhoneNumber(country_code=44, national_number=2034567890, extension="456")
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890x456", "NZ"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890x456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 x456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X 456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 X    456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890 x 456    ", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44 2034567890    X 456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("+44-2034567890;ext=456", "GB"))
        self.assertEqual(ukNumber, phonenumbers.parse("tel:2034567890;ext=456;phone-context=+44", "ZZ"))
        # Full-width extension, "extn" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u("+442034567890\uFF45\uFF58\uFF54\uFF4E456"), "GB"))
        # "xtn" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u("+442034567890\uFF58\uFF54\uFF4E456"), "GB"))
        # "xt" only.
        self.assertEqual(ukNumber, phonenumbers.parse(u("+442034567890\uFF58\uFF54456"), "GB"))

        usWithExtension = PhoneNumber(country_code=1, national_number=8009013355, extension="7246433")
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 x 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 , ext 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 ; 7246433", "US"))
        # To test an extension character without surrounding spaces.
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355;7246433", "US"))
        self.assertEqual(usWithExtension,
                         phonenumbers.parse("(800) 901-3355 ,extension 7246433", "US"))
        self.assertEqual(usWithExtension,
                         phonenumbers.parse(u("(800) 901-3355 ,extensi\u00F3n 7246433"), "US"))
        # Repeat with the small letter o with acute accent created by combining characters.
        self.assertEqual(usWithExtension,
                         phonenumbers.parse(u("(800) 901-3355 ,extensio\u0301n 7246433"), "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 , 7246433", "US"))
        self.assertEqual(usWithExtension, phonenumbers.parse("(800) 901-3355 ext: 7246433", "US"))
        # Testing Russian extension \u0434\u043E\u0431 with variants found online.
        ruWithExtension = PhoneNumber(country_code=7, national_number=4232022511, extension="100")
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11, \u0434\u043E\u0431. 100"), "RU"))
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11 \u0434\u043E\u0431. 100"), "RU"))
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11, \u0434\u043E\u0431 100"), "RU"))
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11 \u0434\u043E\u0431 100"), "RU"))
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11\u0434\u043E\u0431100"), "RU"))
        # In upper case
        self.assertEqual(ruWithExtension, phonenumbers.parse(u("8 (423) 202-25-11, \u0414\u041E\u0411. 100"), "RU"))

        # Test that if a number has two extensions specified, we ignore the second.
        usWithTwoExtensionsNumber = PhoneNumber(country_code=1, national_number=2121231234, extension="508")
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508/x1234", "US"))
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508/ x1234", "US"))
        self.assertEqual(usWithTwoExtensionsNumber, phonenumbers.parse("(212)123-1234 x508\\x1234", "US"))

        # Test parsing numbers in the form (645) 123-1234-910# works, where the last 3 digits before
        # the # are an extension.
        usWithExtension.clear()
        usWithExtension.country_code = 1
        usWithExtension.national_number = to_long(6451231234)
        usWithExtension.extension = "910"
        self.assertEqual(usWithExtension, phonenumbers.parse("+1 (645) 123 1234-910#", "US"))
        # Retry with the same number in a slightly different format.
        self.assertEqual(usWithExtension, phonenumbers.parse("+1 (645) 123 1234 ext. 910#", "US"))

    def testParseHandlesLongExtensionsWithExplicitLabels(self):
        # Test lower and upper limits of extension lengths for each type of label.
        nzNumber = PhoneNumber(country_code=64, national_number=33316005)

        # Firstly, when in RFC format: PhoneNumberUtil.extLimitAfterExplicitLabel
        nzNumber.extension = "0"
        self.assertEqual(nzNumber, phonenumbers.parse("tel:+6433316005;ext=0", "NZ"))
        nzNumber.extension = "01234567890123456789"
        self.assertEqual(nzNumber, phonenumbers.parse("tel:+6433316005;ext=01234567890123456789", "NZ"))
        # Extension too long.
        try:
            phonenumbers.parse("tel:+6433316005;ext=012345678901234567890", "NZ")
            self.fail("This should not parse as length of extension is higher than allowed: " +
                      "tel:+6433316005;ext=012345678901234567890")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        # Explicit extension label: phonenumberutil.ext_limit_after_explicit_label
        nzNumber.extension = "1"
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005ext:1", "NZ"))
        nzNumber.extension = "12345678901234567890"
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 xtn:12345678901234567890", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 extension\t12345678901234567890", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 xtensio:12345678901234567890", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse(u("03 3316005 xtensi\u00F3n, 12345678901234567890#"), "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005extension.12345678901234567890", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse(u("03 3316005 \u0434\u043E\u0431:12345678901234567890"), "NZ"))
        # Extension too long.
        try:
            phonenumbers.parse("03 3316005 extension 123456789012345678901", "NZ")
            self.fail("This should not parse as length of extension is higher than allowed: " +
                      "03 3316005 extension 123456789012345678901")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_LONG,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

    def testParseHandlesLongExtensionsWithAutoDiallingLabels(self):
        # Secondly, cases of auto-dialling and other standard extension labels,
        # phonenumberutil.ext_limit_after_likely_label
        usNumberUserInput = PhoneNumber(country_code=1, national_number=2679000000, extension="123456789012345")
        self.assertEqual(usNumberUserInput, phonenumbers.parse("+12679000000,,123456789012345#", "US"))
        self.assertEqual(usNumberUserInput, phonenumbers.parse("+12679000000;123456789012345#", "US"))
        ukNumberUserInput = PhoneNumber(country_code=44, national_number=2034000000, extension="123456789")
        self.assertEqual(ukNumberUserInput, phonenumbers.parse("+442034000000,,123456789#", "GB"))
        # Extension too long.
        try:
            phonenumbers.parse("+12679000000,,1234567890123456#", "US")
            self.fail("This should not parse as length of extension is higher than allowed: " +
                      "+12679000000,,1234567890123456#")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

    def testParseHandlesShortExtensionsWithAmbiguousChar(self):
        nzNumber = PhoneNumber(country_code=64, national_number=33316005)

        # Thirdly, for single and non-standard cases:
        # phonenumberutil.ext_limit_after_ambiguous_char
        nzNumber.extension = "123456789"
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 x 123456789", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 x. 123456789", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 #123456789#", "NZ"))
        self.assertEqual(nzNumber, phonenumbers.parse("03 3316005 ~ 123456789", "NZ"))
        # Extension too long.
        try:
            phonenumbers.parse("03 3316005 ~ 1234567890", "NZ")
            self.fail("This should not parse as length of extension is higher than allowed: " +
                      "03 3316005 ~ 1234567890")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.TOO_LONG,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

    def testParseHandlesShortExtensionsWhenNotSureOfLabel(self):
        # Lastly, when no explicit extension label present, but denoted by tailing #:
        # PhoneNumberUtil.extLimitWhenNotSure
        usNumber = PhoneNumber(country_code=1, national_number=1234567890, extension="666666")
        self.assertEqual(usNumber, phonenumbers.parse("+1123-456-7890 666666#", "US"))
        usNumber.extension = "6"
        self.assertEqual(usNumber, phonenumbers.parse("+11234567890-6#", "US"))
        # Extension too long.
        try:
            phonenumbers.parse("+1123-456-7890 7777777#", "US")
            self.fail("This should not parse as length of extension is higher than allowed: " +
                      "+1123-456-7890 7777777#")
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.NOT_A_NUMBER,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

    def testParseAndKeepRaw(self):
        alphaNumericNumber = PhoneNumber()
        alphaNumericNumber.merge_from(ALPHA_NUMERIC_NUMBER)
        alphaNumericNumber.raw_input = "800 six-flags"
        alphaNumericNumber.country_code_source = CountryCodeSource.FROM_DEFAULT_COUNTRY
        self.assertEqual(alphaNumericNumber,
                         phonenumbers.parse("800 six-flags", "US", keep_raw_input=True))

        shorterAlphaNumber = PhoneNumber(country_code=1, national_number=8007493524,
                                         raw_input="1800 six-flag",
                                         country_code_source=CountryCodeSource.FROM_NUMBER_WITHOUT_PLUS_SIGN)
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
        except NumberParseException:
            # Expected this exception.
            e = sys.exc_info()[1]
            self.assertEqual(NumberParseException.INVALID_COUNTRY_CODE,
                             e.error_type,
                             msg="Wrong error type stored in exception.")

        koreanNumber = PhoneNumber(country_code=82, national_number=22123456, raw_input="08122123456",
                                   country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY,
                                   preferred_domestic_carrier_code="81")
        self.assertEqual(koreanNumber, phonenumbers.parse("08122123456", "KR", keep_raw_input=True))

    def testParseItalianLeadingZeros(self):
        # Test the number "011".
        oneZero = PhoneNumber(country_code=61, national_number=11, italian_leading_zero=True)
        self.assertEqual(oneZero, phonenumbers.parse("011", "AU"))

        # Test the number "001".
        twoZeros = PhoneNumber(country_code=61, national_number=1, italian_leading_zero=True, number_of_leading_zeros=2)
        self.assertEqual(twoZeros, phonenumbers.parse("001", "AU"))

        # Test the number "000". This number has 2 leading zeros.
        stillTwoZeros = PhoneNumber(country_code=61, national_number=0, italian_leading_zero=True, number_of_leading_zeros=2)
        self.assertEqual(stillTwoZeros, phonenumbers.parse("000", "AU"))

        # Test the number "0000". This number has 3 leading zeros.
        threeZeros = PhoneNumber(country_code=61, national_number=0, italian_leading_zero=True, number_of_leading_zeros=3)
        self.assertEqual(threeZeros, phonenumbers.parse("0000", "AU"))

    def testCountryWithNoNumberDesc(self):
        # Andorra is a country where we don't have PhoneNumberDesc info in the metadata.
        adNumber = PhoneNumber(country_code=376, national_number=12345)
        self.assertEqual("+376 12345", phonenumbers.format_number(adNumber, PhoneNumberFormat.INTERNATIONAL))
        self.assertEqual("+37612345", phonenumbers.format_number(adNumber, PhoneNumberFormat.E164))
        self.assertEqual("12345", phonenumbers.format_number(adNumber, PhoneNumberFormat.NATIONAL))
        self.assertEqual(PhoneNumberType.UNKNOWN, phonenumbers.number_type(adNumber))
        self.assertFalse(phonenumbers.is_valid_number(adNumber))

        # Test dialing a US number from within Andorra.
        self.assertEqual("00 1 650 253 0000",
                         phonenumbers.format_out_of_country_calling_number(US_NUMBER, "AD"))

    def testUnknownCountryCallingCode(self):
        self.assertFalse(phonenumbers.is_valid_number(UNKNOWN_COUNTRY_CODE_NO_RAW_INPUT))
        # It's not very well defined as to what the E164 representation for a
        # number with an invalid country calling code is, but just prefixing
        # the country code and national number is about the best we can do.
        self.assertEqual("+212345",
                         phonenumbers.format_number(UNKNOWN_COUNTRY_CODE_NO_RAW_INPUT, PhoneNumberFormat.E164))

    def testIsNumberMatchMatches(self):
        # Test simple matches where formatting is different, or leading zeros, or country calling code
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
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "tel:+64-3-331-6005;isub=123"))
        # Test alpha numbers.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+1800 siX-Flags", "+1 800 7493 5247"))
        # Test numbers with extensions.
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 extn 1234", "+6433316005#1234"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 ext. 1234", "+6433316005;1234"))
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match("+7 423 202-25-11 ext 100", u("+7 4232022511 \u0434\u043E\u0431. 100")))
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

        # Python version extra tests
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+9991234567", "+99943211234"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match(nzNumber, "+9991235467"))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("+9991235467", nzNumber))
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("asdfasdf", nzNumber))
        self.assertFalse(phonenumberutil._is_number_matching_desc(1234, None))

    def testIsNumberMatchShortMatchIfDiffNumLeadingZeros(self):
        nzNumberOne = PhoneNumber(country_code=64, national_number=33316005, italian_leading_zero=True)
        nzNumberTwo = PhoneNumber(country_code=64, national_number=33316005, italian_leading_zero=True, number_of_leading_zeros=2)
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(nzNumberOne, nzNumberTwo))

        nzNumberOne.italian_leading_zero = False
        nzNumberOne.number_of_leading_zeros = 1
        nzNumberTwo.italian_leading_zero = True
        nzNumberTwo.number_of_leading_zeros = 1
        # Since one doesn't have the "italian_leading_zero" set to true, we ignore the number of
        # leading zeros present (1 is in any case the default value).
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(nzNumberOne, nzNumberTwo))

    def testIsNumberMatchAcceptsProtoDefaultsAsMatch(self):
        nzNumberOne = PhoneNumber(country_code=64, national_number=33316005, italian_leading_zero=True)
        # The default for number_of_leading_zeros is 1, so it shouldn't normally be set, however if it
        # is it should be considered equivalent.
        nzNumberTwo = PhoneNumber(country_code=64, national_number=33316005, italian_leading_zero=True, number_of_leading_zeros=1)
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumberOne, nzNumberTwo))

    def testIsNumberMatchMatchesDiffLeadingZerosIfItalianLeadingZeroFalse(self):
        nzNumberOne = PhoneNumber(country_code=64, national_number=33316005)
        # The default for number_of_leading_zeros is 1, so it shouldn't normally be set, however if it
        # is it should be considered equivalent.
        nzNumberTwo = PhoneNumber(country_code=64, national_number=33316005, number_of_leading_zeros=1)
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumberOne, nzNumberTwo))

        # Even if it is set to ten, it is still equivalent because in both cases
        # italian_leading_zero is not true.
        nzNumberTwo.number_of_leading_zeros = 10
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(nzNumberOne, nzNumberTwo))

    def testIsNumberMatchIgnoresSomeFields(self):
        # Check raw_input, country_code_source and preferred_domestic_carrier_code are ignored.
        brNumberOne = PhoneNumber(country_code=55, national_number=3121286979,
                                  country_code_source=CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN,
                                  preferred_domestic_carrier_code="12", raw_input="012 3121286979")
        brNumberTwo = PhoneNumber(country_code=55, national_number=3121286979,
                                  country_code_source=CountryCodeSource.FROM_DEFAULT_COUNTRY,
                                  preferred_domestic_carrier_code="14", raw_input="143121286979")
        self.assertEqual(phonenumbers.MatchType.EXACT_MATCH,
                         phonenumbers.is_number_match(brNumberOne, brNumberTwo))

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
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 extn 1234", "tel:+64-3-331-6005;ext=1235"))
        # NSN matches, but extension is different - not the same number.
        self.assertEqual(phonenumbers.MatchType.NO_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005 ext.1235", "3 331 6005#1234"))

        # Invalid numbers that can't be parsed.
        self.assertEqual(phonenumbers.MatchType.NOT_A_NUMBER,
                         phonenumbers.is_number_match("4", "3 331 6043"))
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
                         phonenumbers.is_number_match("+64 3 331-6005", "tel:03-331-6005;isub=1234;phone-context=abc.nz"))
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
        randomNumber = PhoneNumber(country_code=41, national_number=6502530000)
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match(randomNumber, "1-650-253-0000"))

    def testIsNumberMatchShortNsnMatches(self):
        # Short NSN matches with the country not specified for either one or both numbers.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005", "tel:331-6005;phone-context=abc.nz"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005",
                                                      "tel:331-6005;isub=1234;phone-context=abc.nz"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("+64 3 331-6005",
                                                      "tel:331-6005;isub=1234;phone-context=abc.nz;a=%A1"))
        # We did not know that the "0" was a national prefix since neither
        # number has a country code, so this is considered a SHORT_NSN_MATCH.
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "03 331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "331 6005"))
        self.assertEqual(phonenumbers.MatchType.SHORT_NSN_MATCH,
                         phonenumbers.is_number_match("3 331-6005", "tel:331-6005;phone-context=abc.nz"))
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
        italianNumberOne = PhoneNumber(country_code=39, national_number=1234, italian_leading_zero=True)
        italianNumberTwo = PhoneNumber(country_code=39, national_number=1234)
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
        self.assertFalse(phonenumberutil.can_be_internationally_dialled(US_TOLLFREE))

        # Normal US numbers can be internationally dialled.
        self.assertTrue(phonenumberutil.can_be_internationally_dialled(US_NUMBER))

        # Invalid number.
        self.assertTrue(phonenumberutil.can_be_internationally_dialled(US_LOCAL_NUMBER))

        # We have no data for NZ - should return True.
        self.assertTrue(phonenumberutil.can_be_internationally_dialled(NZ_NUMBER))
        self.assertTrue(phonenumberutil.can_be_internationally_dialled(INTERNATIONAL_TOLL_FREE))

    def testIsAlphaNumber(self):
        self.assertTrue(phonenumbers.is_alpha_number("1800 six-flags"))
        self.assertTrue(phonenumbers.is_alpha_number("1800 six-flags ext. 1234"))
        self.assertTrue(phonenumbers.is_alpha_number("+800 six-flags"))
        self.assertTrue(phonenumbers.is_alpha_number("180 six-flags"))
        self.assertFalse(phonenumbers.is_alpha_number("1800 123-1234"))
        self.assertFalse(phonenumbers.is_alpha_number("1 six-flags"))
        self.assertFalse(phonenumbers.is_alpha_number("18 six-flags"))
        self.assertFalse(phonenumbers.is_alpha_number("1800 123-1234 extension: 1234"))
        self.assertFalse(phonenumbers.is_alpha_number("+800 1234-1234"))
        # Python version extra test
        self.assertFalse(phonenumbers.is_alpha_number(""))

    def testIsMobileNumberPortableRegion(self):
        self.assertTrue(phonenumbers.is_mobile_number_portable_region("US"))
        self.assertTrue(phonenumbers.is_mobile_number_portable_region("GB"))
        self.assertFalse(phonenumbers.is_mobile_number_portable_region("AE"))
        self.assertFalse(phonenumbers.is_mobile_number_portable_region("BS"))
        # Python version extra test: check with bogus region
        self.assertFalse(phonenumbers.is_mobile_number_portable_region("XY"))

    def testMetadataEquality(self):
        # Python version extra tests for equality against other types
        desc1 = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        desc1._mutable = True
        desc2 = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        desc2._mutable = True
        desc3 = PhoneNumberDesc(national_number_pattern="\\d{4,7}",
                                example_number="1234567")
        desc3._mutable = True
        self.assertNotEqual(desc1, None)
        self.assertNotEqual(desc1, "")
        self.assertEqual(desc1, desc2)
        self.assertNotEqual(desc1, desc3)
        self.assertTrue(desc1 != desc3)
        desc1.merge_from(desc3)
        self.assertEqual(desc1, desc3)
        self.assertEqual(r"PhoneNumberDesc(national_number_pattern='\\d{4,7}', " +
                         r"example_number='1234567')",
                         str(desc3))
        nf1 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['1'])
        nf1._mutable = True
        nf2 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['1'])
        nf2._mutable = True
        nf3 = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['2'],
                           national_prefix_formatting_rule='$NP',
                           domestic_carrier_code_formatting_rule='$NP',
                           national_prefix_optional_when_formatting=True)
        nf3._mutable = True
        self.assertEqual(nf1, nf2)
        self.assertNotEqual(nf1, nf3)
        self.assertNotEqual(nf1, None)
        self.assertNotEqual(nf1, "")
        self.assertNotEqual(nf1, 123)
        self.assertTrue(nf1 != nf3)
        nf1.merge_from(nf3)
        # Still not equal because the leading digits are combined not overwritten
        self.assertNotEqual(nf1, nf3)

        metadata1 = PhoneMetadata("XY", preferred_international_prefix=u('9123'), register=False)
        metadata1._mutable = True
        metadata2 = PhoneMetadata("XY", preferred_international_prefix=u('9123'), register=False)
        metadata2._mutable = True
        metadata3 = PhoneMetadata("XY", preferred_international_prefix=u('9100'), register=False)
        metadata3._mutable = True
        self.assertEqual(metadata1, metadata2)
        self.assertNotEqual(metadata1, metadata3)
        self.assertTrue(metadata1 != metadata3)
        self.assertNotEqual(metadata1, None)
        self.assertNotEqual(metadata1, "")
        self.assertNotEqual(metadata1, 123)

    def testFrozenPhoneNumberImmutable(self):
        number = PhoneNumber(country_code=39, national_number=236618300, italian_leading_zero=True)
        frozen1 = FrozenPhoneNumber(country_code=39, national_number=236618300, italian_leading_zero=True)
        frozen2 = FrozenPhoneNumber(number)
        self.assertEqual(number, frozen1)
        self.assertEqual(frozen1, frozen2)
        number.country_code = 999
        self.assertNotEqual(number, frozen1)
        try:
            frozen1.country_code = 999
            self.fail("Expected exception on __setattr__")
        except TypeError:
            pass
        try:
            del frozen2.country_code
            self.fail("Expected exception on __delattr__")
        except TypeError:
            pass
        self.assertEqual(repr(frozen1), "FrozenPhoneNumber(country_code=39, national_number=236618300, extension=None, italian_leading_zero=True, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)")

    def testMetadataImmutable(self):
        desc = PhoneNumberDesc(national_number_pattern="\\d{4,8}")
        nf = NumberFormat(pattern=r'\d{3}', format=r'\1', leading_digits_pattern=['1'])
        metadata = PhoneMetadata("XY", preferred_international_prefix='9123', register=False)
        try:
            desc.national_number_pattern = ""
            self.fail("Expected exception on __setattr__")
        except TypeError:
            pass
        try:
            del desc.national_number_pattern
            self.fail("Expected exception on __delattr__")
        except TypeError:
            pass
        try:
            nf.pattern = ""
            self.fail("Expected exception on __setattr__")
        except TypeError:
            pass
        try:
            del nf.pattern
            self.fail("Expected exception on __delattr__")
        except TypeError:
            pass
        try:
            metadata.id = None
            self.fail("Expected exception on __setattr__")
        except TypeError:
            pass
        try:
            del metadata.id
            self.fail("Expected exception on __delattr__")
        except TypeError:
            pass

    def testMetadataAsString(self):
        # Python version extra tests for string conversions
        metadata = PhoneMetadata.metadata_for_region("AU")
        self.assertEqual('\\' + 'd',
                         metadata.number_format[0].pattern[1:3])
        self.assertEqual(r"""NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1')""",
                         str(metadata.number_format[0]))
        self.assertEqual(repr(metadata.number_format[0]),
                         str(metadata.number_format[0]))
        self.assertEqual(r"""PhoneNumberDesc(national_number_pattern='[1-578]\\d{4,14}', possible_length=(9, 10))""",
                         str(metadata.general_desc))
        self.assertEqual(repr(metadata.general_desc), str(metadata.general_desc))

        # Create some metadata, including an invalid example number
        metadataXX = PhoneMetadata("XX",
                                   international_prefix='9123',
                                   general_desc=PhoneNumberDesc(example_number='12'),
                                   personal_number=PhoneNumberDesc(example_number='12'),
                                   short_code=PhoneNumberDesc(national_number_pattern='[123]'),
                                   preferred_international_prefix='9123',
                                   national_prefix='1',
                                   preferred_extn_prefix='2',
                                   national_prefix_for_parsing='1',
                                   national_prefix_transform_rule='',
                                   number_format=[NumberFormat()],
                                   intl_number_format=[NumberFormat()],
                                   leading_digits='123',
                                   leading_zero_possible=True,
                                   short_data=True,
                                   register=False)
        self.assertEqual("""PhoneMetadata(id='XX', country_code=None, international_prefix='9123',
    general_desc=PhoneNumberDesc(example_number='12'),
    personal_number=PhoneNumberDesc(example_number='12'),
    short_code=PhoneNumberDesc(national_number_pattern='[123]'),
    preferred_international_prefix='9123',
    national_prefix='1',
    preferred_extn_prefix='2',
    national_prefix_for_parsing='1',
    national_prefix_transform_rule='',
    number_format=[NumberFormat(pattern=None, format=None)],
    intl_number_format=[NumberFormat(pattern=None, format=None)],
    leading_digits='123',
    leading_zero_possible=True,
    short_data=True)""",
                         str(metadataXX))

        # Coverage test: short_code desc has no example number
        PhoneMetadata._short_region_metadata['XX'] = metadataXX
        self.assertEqual("", shortnumberinfo._example_short_number("XX"))
        del PhoneMetadata._short_region_metadata['XX']

        # And now the grand finale: check a real metadata example
        result = str(metadata)
        self.assertTrue(result.startswith("PhoneMetadata(id='AU', country_code=61, international_prefix='001[12]',"))

    def testMetadataEval(self):
        # Python version extra tests for string conversions
        metadata = PhoneMetadata.metadata_for_region("AU")
        new_number_format = eval(repr(metadata.number_format[0]))
        self.assertEqual(new_number_format, metadata.number_format[0])
        new_general_desc = eval(repr(metadata.general_desc))
        self.assertEqual(new_general_desc, metadata.general_desc)
        new_metadata = eval(repr(metadata))
        self.assertEqual(new_metadata, metadata)

    def testMetadataRegister(self):
        # Python version extra tests for metadata registration.
        PhoneMetadata("XY",
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      register=True)
        # Registering the same data twice is OK
        PhoneMetadata("XY",
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      register=True)
        # Registering different data is not OK
        self.assertRaises(Exception, PhoneMetadata, *("XY",),
                          **{'preferred_international_prefix': u('9999'),
                             'register': True})
        self.assertTrue(phonenumbers.example_number_for_type('XY', PhoneNumberType.PERSONAL_NUMBER) is None)

    def testShortMetadataRegister(self):
        # Python version extra tests for short metadata registration.
        PhoneMetadata("XZ",
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      short_data=True,
                      register=True)
        # Registering the same data twice is OK
        PhoneMetadata("XZ",
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      short_data=True,
                      register=True)
        # Registering different data is not OK
        self.assertRaises(Exception, PhoneMetadata, *("XZ",),
                          **{'preferred_international_prefix': u('9999'),
                             'register': True,
                             'short_data': True})
        self.assertTrue(phonenumbers.example_number_for_type('XZ', PhoneNumberType.PERSONAL_NUMBER) is None)

    def testNonGeoMetadataRegister(self):
        # Python version extra tests for non-geo metadata registration.
        PhoneMetadata("001", country_code=999,
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      register=True)
        # Registering the same data twice is OK
        PhoneMetadata("001", country_code=999,
                      general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                   example_number='123'),
                      personal_number=PhoneNumberDesc(national_number_pattern='\\d{7,10}',
                                                      example_number='123'),
                      preferred_international_prefix=u('9123'),
                      register=True)
        # Registering different data is not OK
        self.assertRaises(Exception, PhoneMetadata, *("001",),
                          **{'country_code': 999,
                             'preferred_international_prefix': u('9999'),
                             'register': True})

    def testPickledException(self):
        err = NumberParseException(NumberParseException.TOO_SHORT_AFTER_IDD, 'hello world')
        pickled = pickle.dumps(err)
        recovered = pickle.loads(pickled)
        self.assertEqual("%r" % err, "%r" % recovered)

    def testEnumString(self):
        # Python version extra test for enum to_string() methods.
        self.assertEqual(PhoneNumberFormat.to_string(PhoneNumberFormat.E164), u("E164"))
        self.assertEqual(PhoneNumberFormat.to_string(PhoneNumberFormat.INTERNATIONAL), u("INTERNATIONAL"))
        self.assertEqual(PhoneNumberFormat.to_string(PhoneNumberFormat.NATIONAL), u("NATIONAL"))
        self.assertEqual(PhoneNumberFormat.to_string(PhoneNumberFormat.RFC3966), u("RFC3966"))
        self.assertEqual(PhoneNumberFormat.to_string(999), u("INVALID (999)"))

        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.FIXED_LINE), u("FIXED_LINE"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.MOBILE), u("MOBILE"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.FIXED_LINE_OR_MOBILE), u("FIXED_LINE_OR_MOBILE"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.TOLL_FREE), u("TOLL_FREE"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.PREMIUM_RATE), u("PREMIUM_RATE"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.SHARED_COST), u("SHARED_COST"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.VOIP), u("VOIP"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.PERSONAL_NUMBER), u("PERSONAL_NUMBER"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.PAGER), u("PAGER"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.UAN), u("UAN"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.VOICEMAIL), u("VOICEMAIL"))
        self.assertEqual(PhoneNumberType.to_string(PhoneNumberType.UNKNOWN), u("UNKNOWN"))
        self.assertEqual(PhoneNumberType.to_string(999), u("INVALID (999)"))

        self.assertEqual(MatchType.to_string(MatchType.NOT_A_NUMBER), u("NOT_A_NUMBER"))
        self.assertEqual(MatchType.to_string(MatchType.NO_MATCH), u("NO_MATCH"))
        self.assertEqual(MatchType.to_string(MatchType.SHORT_NSN_MATCH), u("SHORT_NSN_MATCH"))
        self.assertEqual(MatchType.to_string(MatchType.NSN_MATCH), u("NSN_MATCH"))
        self.assertEqual(MatchType.to_string(MatchType.EXACT_MATCH), u("EXACT_MATCH"))
        self.assertEqual(MatchType.to_string(999), u("INVALID (999)"))

        self.assertEqual(ValidationResult.to_string(ValidationResult.IS_POSSIBLE), u("IS_POSSIBLE"))
        self.assertEqual(ValidationResult.to_string(ValidationResult.IS_POSSIBLE_LOCAL_ONLY), u("IS_POSSIBLE_LOCAL_ONLY"))
        self.assertEqual(ValidationResult.to_string(ValidationResult.INVALID_COUNTRY_CODE), u("INVALID_COUNTRY_CODE"))
        self.assertEqual(ValidationResult.to_string(ValidationResult.TOO_SHORT), u("TOO_SHORT"))
        self.assertEqual(ValidationResult.to_string(ValidationResult.INVALID_LENGTH), u("INVALID_LENGTH"))
        self.assertEqual(ValidationResult.to_string(ValidationResult.TOO_LONG), u("TOO_LONG"))
        self.assertEqual(ValidationResult.to_string(999), u("INVALID (999)"))

    def testCoverage(self):
        # Python version extra tests
        self.assertTrue(phonenumberutil._region_code_for_number_from_list(GB_NUMBER, ("XX",)) is None)
        self.assertEqual((0, "abcdef"),
                         phonenumberutil._extract_country_code("abcdef"))
        metadata = PhoneMetadata.metadata_for_region("AU")
        number = PhoneNumber()
        self.assertEqual((0, u("")),
                         phonenumberutil._maybe_extract_country_code("",
                                                                     metadata,
                                                                     False,
                                                                     number))
        self.assertEqual((CountryCodeSource.FROM_DEFAULT_COUNTRY, ""),
                         phonenumberutil._maybe_strip_i18n_prefix_and_normalize("", "011"))
        self.assertFalse(phonenumberutil._check_region_for_parsing("", "cs"))

        metadataXY = PhoneMetadata("XY",
                                   general_desc=PhoneNumberDesc(national_number_pattern='\\d{7,10}'),
                                   national_prefix_for_parsing=u('0(1|2|3)(4|5|6)'),
                                   national_prefix_transform_rule=u('\\2'),
                                   register=False)
        self.assertEqual(('1', '41234567', True),
                         phonenumberutil._maybe_strip_national_prefix_carrier_code("0141234567",
                                                                                   metadataXY))
        self.assertEqual(('', '01412345', False),
                         phonenumberutil._maybe_strip_national_prefix_carrier_code("01412345",
                                                                                   metadataXY))

        # Temporarily insert invalid example number
        metadata800 = PhoneMetadata.metadata_for_nongeo_region(800)
        saved_mobile = metadata800.mobile
        metadata800._mutable = True
        metadata800.mobile = PhoneNumberDesc(example_number='')
        self.assertTrue(phonenumbers.example_number_for_non_geo_entity(800) is not None)
        metadata800.mobile = saved_mobile
        metadata800._mutable = False

        self.assertFalse(phonenumbers.phonenumberutil._raw_input_contains_national_prefix("07", "0", "JP"))

        # Temporarily change formatting rule
        metadataGB = PhoneMetadata.metadata_for_region("GB")
        saved_rule = metadataGB.number_format[0].national_prefix_formatting_rule
        metadataGB.number_format[0]._mutable = True
        metadataGB.number_format[0].national_prefix_formatting_rule = u('(\\1)')
        numberWithoutNationalPrefixGB = phonenumbers.parse("2087654321", "GB", keep_raw_input=True)
        self.assertEqual("(20) 8765 4321",
                         phonenumbers.format_in_original_format(numberWithoutNationalPrefixGB, "GB"))
        metadataGB.number_format[0].national_prefix_formatting_rule = saved_rule
        metadataGB.number_format[0]._mutable = False
