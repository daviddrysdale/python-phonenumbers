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
import unittest

from phonenumbers import PhoneNumberType, PhoneMetadata, NumberParseException
from phonenumbers import phonenumberutil, PhoneNumber


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
                    print >> sys.stderr, "Failed validation for %s" % exampleNumber
                else:
                    # We know the number is valid, now we check the type.
                    exampleNumberType = phonenumberutil.number_type(exampleNumber)
                    if exampleNumberType not in possibleExpectedTypes:
                        self.wrong_type_cases.append(exampleNumber)
                        print >> sys.stderr, "Wrong type for %s: got %s" % (exampleNumber, exampleNumberType)
                        print >> sys.stderr, "Expected types: "
                        for phone_type in possibleExpectedTypes:
                            print >> sys.stderr, "  %s" % phone_type

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
        # Python version extra test
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
            metadata = PhoneMetadata.region_metadata.get(regionCode, None)
            desc = None
            if metadata is not None:
                desc = metadata.no_international_dialling
            try:
                if desc.example_number is not None:
                    exampleNumber = phonenumberutil.parse(desc.example_number, regionCode)

            except NumberParseException, e:
                print >> sys.stderr, "Failed parse: %s" % e

            if (exampleNumber is not None and
                phonenumberutil._can_be_internationally_dialled(exampleNumber)):
                self.wrong_type_cases.append(exampleNumber)
        self.assertEqual(0, len(self.wrong_type_cases))

    def testEveryRegionHasAnExampleNumber(self):
        for regionCode in phonenumberutil.SUPPORTED_REGIONS:
            exampleNumber = phonenumberutil.example_number(regionCode)
            self.assertTrue(exampleNumber is not None,
                            msg="None found for region %s" % regionCode)

    # Extra tests that need access to the real metadata
    def testBlankMetadata(self):
        # Python version extra test
        # Some metadata is blank; check that we cope with this.
        # Example: MH (+692)
        number = phonenumberutil.parse("+6927654321", "US")
        self.assertEqual("Country Code: 692 National Number: 7654321 Leading Zero: False", str(number))

    def testFormatNumberForMobile(self):
        # Python version extra test.  Special cases for CO and BR in
        # format_number_for_mobile_dialing(), included here so that real metadata is used
        coNumberFixed = PhoneNumber(country_code=57, national_number=12345678L)
        coNumberMobile = PhoneNumber(country_code=57, national_number=3211234567L)
        peNumberFixed = PhoneNumber(country_code=51, national_number=11234567L)
        brNumberFixed = PhoneNumber(country_code=55, national_number=1123456789L)
        brNumberMobile = PhoneNumber(country_code=55, national_number=1161234567L,
                                     preferred_domestic_carrier_code="303")
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
        self.assertEqual("03031161234567",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberMobile, "BR", False))
        self.assertEqual("0 303 (11) 6123-4567",
                         phonenumberutil.format_number_for_mobile_dialing(brNumberMobile, "BR", True))
