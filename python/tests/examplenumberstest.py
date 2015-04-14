#!/usr/bin/env python
"""Unit tests for phonenumberutil.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/ExampleNumbersTest.java
#
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
import re
import unittest

from phonenumbers import PhoneNumberType, PhoneMetadata, NumberParseException
from phonenumbers import phonenumberutil, PhoneNumber, is_emergency_number
from phonenumbers import shortnumberinfo, ShortNumberCost, AsYouTypeFormatter
from phonenumbers import PhoneNumberMatcher, Leniency
from phonenumbers.util import prnt
from phonenumbers.re_util import fullmatch


class ExampleNumbersTest(unittest.TestCase):
    """Verifies all of the example numbers in the metadata are valid and of
    the correct type. If no example number exists for a particular type, the
    test still passes."""

    def setUp(self):
        self.invalid_cases = []
        self.wrong_type_cases = []

    def tearDown(self):
        pass

    def _checkNumbersValidAndCorrectType(self,
                                         exampleNumberRequestedType,
                                         possibleExpectedTypes):
        """
        Arguments:
        exampleNumberRequestedType -- type we are requesting an example number for
        possibleExpectedTypes -- acceptable types that this number should match, such as
              FIXED_LINE and FIXED_LINE_OR_MOBILE for a fixed line example number.
        """
        for regionCode in phonenumberutil.SUPPORTED_REGIONS:
            exampleNumber = phonenumberutil.example_number_for_type(regionCode, exampleNumberRequestedType)
            if exampleNumber is not None:
                if not phonenumberutil.is_valid_number(exampleNumber):
                    self.invalid_cases.append(exampleNumber)
                    prnt("Failed validation for %s" % exampleNumber, file=sys.stderr)
                else:
                    # We know the number is valid, now we check the type.
                    exampleNumberType = phonenumberutil.number_type(exampleNumber)
                    if exampleNumberType not in possibleExpectedTypes:
                        self.wrong_type_cases.append(exampleNumber)
                        prnt("Wrong type for %s: got %s" % (exampleNumber, exampleNumberType), file=sys.stderr)
                        prnt("Expected types: ", file=sys.stderr)
                        for phone_type in possibleExpectedTypes:
                            prnt("  %s" % phone_type, file=sys.stderr)

    def testFixedLine(self):
        fixedLineTypes = set((PhoneNumberType.FIXED_LINE, PhoneNumberType.FIXED_LINE_OR_MOBILE))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.FIXED_LINE, fixedLineTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testMobile(self):
        mobileTypes = set((PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.MOBILE, mobileTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testTollFree(self):
        tollFreeTypes = set((PhoneNumberType.TOLL_FREE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.TOLL_FREE, tollFreeTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testPremiumRate(self):
        premiumRateTypes = set((PhoneNumberType.PREMIUM_RATE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.PREMIUM_RATE, premiumRateTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testVoip(self):
        voipTypes = set((PhoneNumberType.VOIP,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.VOIP, voipTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testPager(self):
        pagerTypes = set((PhoneNumberType.PAGER,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.PAGER, pagerTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testUan(self):
        uanTypes = set((PhoneNumberType.UAN,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.UAN, uanTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testVoicemail(self):
        voicemailTypes = set((PhoneNumberType.VOICEMAIL,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.VOICEMAIL, voicemailTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testSharedCost(self):
        sharedCostTypes = set((PhoneNumberType.SHARED_COST,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.SHARED_COST, sharedCostTypes)
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testCanBeInternationallyDialled(self):
        for regionCode in phonenumberutil.SUPPORTED_REGIONS:
            exampleNumber = None
            metadata = PhoneMetadata.metadata_for_region(regionCode, None)
            desc = None
            if metadata is not None:
                desc = metadata.no_international_dialling
            try:
                if desc.example_number is not None:
                    exampleNumber = phonenumberutil.parse(desc.example_number, regionCode)

            except NumberParseException:
                _, e, _ = sys.exc_info()
                prnt("Failed parse: %s" % e, file=sys.stderr)

            if (exampleNumber is not None and
                phonenumberutil._can_be_internationally_dialled(exampleNumber)):
                self.wrong_type_cases.append(exampleNumber)
                prnt("Number %s should not be internationally diallable" % exampleNumber, file=sys.stderr)
        self.assertEqual(0, len(self.wrong_type_cases))

    def testGlobalNetworkNumbers(self):
        PhoneMetadata.load_all()
        for callingCode in PhoneMetadata._country_code_metadata.keys():
            exampleNumber = phonenumberutil.example_number_for_non_geo_entity(callingCode)
            self.assertTrue(exampleNumber is not None,
                            msg="No example phone number for calling code %s" % callingCode)
            if not phonenumberutil.is_valid_number(exampleNumber):
                self.invalid_cases.append(exampleNumber)
                prnt("Failed validation for %s" % exampleNumber, file=sys.stderr)
        self.assertEqual(0, len(self.invalid_cases))

    def testEveryRegionHasAnExampleNumber(self):
        for regionCode in phonenumberutil.SUPPORTED_REGIONS:
            exampleNumber = phonenumberutil.example_number(regionCode)
            self.assertTrue(exampleNumber is not None,
                            msg="None found for region %s" % regionCode)

    def testShortNumbersValidAndCorrectCost(self):
        invalid_string_cases = []
        for regionCode in phonenumberutil.SUPPORTED_SHORT_REGIONS:
            exampleShortNumber = shortnumberinfo._example_short_number(regionCode)
            phoneNumber = phonenumberutil.parse(exampleShortNumber, regionCode)
            if not shortnumberinfo.is_valid_short_number_for_region(phoneNumber, regionCode):
                invalid_string_case = "region_code: %s, national_number: %s" % (regionCode, exampleShortNumber)
                invalid_string_cases.append(invalid_string_case)
                prnt("Failed validation from string %s" % invalid_string_case, file=sys.stderr)
            if not shortnumberinfo.is_valid_short_number(phoneNumber):
                self.invalid_cases.append(phoneNumber)
                prnt("Failed validation for %s" % phoneNumber, file=sys.stderr)
            for cost in [ShortNumberCost.TOLL_FREE, ShortNumberCost.STANDARD_RATE,
                         ShortNumberCost.PREMIUM_RATE, ShortNumberCost.UNKNOWN_COST]:
                exampleShortNumber = shortnumberinfo._example_short_number_for_cost(regionCode, cost)
                if exampleShortNumber != "":
                    phoneNumber = phonenumberutil.parse(exampleShortNumber, regionCode)
                    if cost != shortnumberinfo.expected_cost_for_region(phoneNumber, regionCode):
                        self.wrong_type_cases.append(phoneNumber)
                        prnt("Wrong cost for %s" % phoneNumber, file=sys.stderr)
        self.assertEqual(0, len(invalid_string_cases))
        self.assertEqual(0, len(self.invalid_cases))
        self.assertEqual(0, len(self.wrong_type_cases))

    def testEmergency(self):
        wrongTypeCounter = 0
        for regionCode in phonenumberutil.SUPPORTED_SHORT_REGIONS:
            metadata = PhoneMetadata.short_metadata_for_region(regionCode, None)
            desc = metadata.emergency
            if desc.example_number is not None:
                exampleNumber = desc.example_number
                if (not fullmatch(re.compile(desc.possible_number_pattern), exampleNumber) or
                    not is_emergency_number(exampleNumber, regionCode)):
                    wrongTypeCounter += 1
                    prnt("Emergency example number test failed for %s" % regionCode, file=sys.stderr)
                elif shortnumberinfo.expected_cost_for_region(exampleNumber, regionCode) != ShortNumberCost.TOLL_FREE:
                    wrongTypeCounter += 1
                    prnt("Emergency example number not toll free for %s" % regionCode, file=sys.stderr)
        self.assertEqual(0, wrongTypeCounter)

    def testCarrierSpecificShortNumbers(self):
        wrongTagCounter = 0
        for regionCode in phonenumberutil.SUPPORTED_SHORT_REGIONS:
            # Test the carrier-specific tag.
            metadata = PhoneMetadata.short_metadata_for_region(regionCode, None)
            desc = metadata.carrier_specific
            if desc.example_number is not None:
                exampleNumber = desc.example_number
                carrierSpecificNumber = phonenumberutil.parse(exampleNumber, regionCode)
                if (not fullmatch(re.compile(desc.possible_number_pattern), exampleNumber) or
                    not shortnumberinfo.is_carrier_specific(carrierSpecificNumber)):
                    wrongTagCounter += 1
                    prnt("Carrier-specific test failed for %s" % regionCode, file=sys.stderr)
            # TODO: Test other tags here
        self.assertEqual(0, wrongTagCounter)

    def testIsCarrierSpecific(self):
        # Python version extra test: hit is_carrier_specific entrypoint
        esNumber = PhoneNumber(country_code=34, national_number=123)
        self.assertTrue(shortnumberinfo.is_carrier_specific(esNumber))
        esNumber.national_number = 512345678
        self.assertFalse(shortnumberinfo.is_carrier_specific(esNumber))

    # Extra tests that need access to the real metadata
    def testIsraelShortNumber(self):
        # Python version extra test:
        # Send in a 4-digit Israel phone number
        matcher = PhoneNumberMatcher("1234", "IL", leniency=Leniency.POSSIBLE)
        self.assertFalse(matcher.has_next())
        matcher2 = PhoneNumberMatcher("*1234", "IL", leniency=Leniency.POSSIBLE)
        self.assertTrue(matcher2.has_next())

    def testBlankMetadata(self):
        # Python version extra test
        # Some metadata is blank; check that we cope with this.
        # Example: MH (+692)
        number = phonenumberutil.parse("+6927654321", "US")
        self.assertEqual("Country Code: 692 National Number: 7654321", str(number))

    def testMetadataPrint(self):
        for callingCode in PhoneMetadata._region_available.keys():
            metadata = PhoneMetadata.metadata_for_region("GB")
            str(metadata)

    def testWhitespaceInNationalPrefixForParsing(self):
        # Python version extra test
        # AR metadata has whitespace in the RE for nationalPrefixForParsing
        number = phonenumberutil.parse("+540348215617137", "AR")
        self.assertTrue(phonenumberutil.is_valid_number(number))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumberutil.number_type(number))
        number = phonenumberutil.parse("0344615614207", "AR")
        self.assertTrue(phonenumberutil.is_valid_number(number))
        self.assertEqual(PhoneNumberType.MOBILE, phonenumberutil.number_type(number))

    def testFormatNumberForMobile(self):
        # Python version extra test.  Special cases for CO and BR in
        # format_number_for_mobile_dialing(), included here so that real metadata is used
        coNumberFixed = PhoneNumber(country_code=57, national_number=12345678)
        coNumberMobile = PhoneNumber(country_code=57, national_number=3211234567)
        peNumberFixed = PhoneNumber(country_code=51, national_number=11234567)
        brNumberFixed = PhoneNumber(country_code=55, national_number=1123456789)
        brNumberMobile = PhoneNumber(country_code=55, national_number=11961234567,
                                     preferred_domestic_carrier_code="303")
        huNumberFixed = PhoneNumber(country_code=36, national_number=12345678)
        self.assertEqual("0312345678",
                         phonenumberutil.format_number_for_mobile_dialing(coNumberFixed, "CO", False))
        self.assertEqual("03 1 2345678",
                         phonenumberutil.format_number_for_mobile_dialing(coNumberFixed, "CO", True))
        self.assertEqual("3211234567",
                         phonenumberutil.format_number_for_mobile_dialing(coNumberMobile, "CO", False))
        self.assertEqual("321 1234567",
                         phonenumberutil.format_number_for_mobile_dialing(coNumberMobile, "CO", True))
        self.assertEqual("011234567",
                         phonenumberutil.format_number_for_mobile_dialing(peNumberFixed, "PE", False))
        self.assertEqual("(01) 1234567",
                         phonenumberutil.format_number_for_mobile_dialing(peNumberFixed, "PE", True))
        self.assertEqual("",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberFixed, "BR", False))
        self.assertEqual("",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberFixed, "BR", True))
        self.assertEqual("030311961234567",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberMobile, "BR", False))
        self.assertEqual("0 303 (11) 96123-4567",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberMobile, "BR", True))
        self.assertEqual("0612345678",
                         phonenumberutil.format_number_for_mobile_dialing(huNumberFixed, "HU", False))

    def testAYTFShortNumberFormatting_AR(self):
        # Python version extra test: use real metadata so that the check for accrued digits already
        # matching a format fires.
        formatter = AsYouTypeFormatter("AR")
        self.assertEqual("1", formatter.input_digit('1'))
        self.assertEqual("10", formatter.input_digit('0'))
        self.assertEqual("101", formatter.input_digit('1'))

    def testPrintShortMetadata(self):
        # Python version extra test.  Print string representation of short metadata.
        short_metadata = PhoneMetadata.short_metadata_for_region("GB")
        self.assertEqual(r"""PhoneMetadata(id='GB', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-4679]\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', possible_number_pattern='\\d{3}', example_number='112'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[01]|1(?:[12]|[68]\\d{3})|2[123]|33|4(?:1|7\\d)|5\\d|70\\d|800\\d|9[15])|2(?:02|2(?:02|11|2)|3(?:02|45)|425)|3[13]3|4(?:0[02]|35[01]|44[45]|5\\d)|650|789|9(?:01|99)', possible_number_pattern='\\d{3,6}', example_number='150'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)""", str(short_metadata))
