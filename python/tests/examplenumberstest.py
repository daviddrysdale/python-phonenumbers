#!/usr/bin/env python
"""Unit tests for phonenumberutil.py"""

# Based on original Java code:
#     java/test/com/google/i18n/phonenumbers/ExampleNumbersTest.java
#
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
import sys
import unittest

import pathfix
pathfix.fix()

from phonenumbers import PhoneNumberType, PhoneMetadata, NumberParseException
from phonenumbers import phonenumberutil


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
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testMobile(self):
        mobileTypes = set((PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.MOBILE, mobileTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testTollFree(self):
        tollFreeTypes = set((PhoneNumberType.TOLL_FREE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.TOLL_FREE, tollFreeTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testPremiumRate(self):
        premiumRateTypes = set((PhoneNumberType.PREMIUM_RATE,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.PREMIUM_RATE, premiumRateTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testVoip(self):
        voipTypes = set((PhoneNumberType.VOIP,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.VOIP, voipTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testPager(self):
        pagerTypes = set((PhoneNumberType.PAGER,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.PAGER, pagerTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testUan(self):
        uanTypes = set((PhoneNumberType.UAN,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.UAN, uanTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

    def testSharedCost(self):
        sharedCostTypes = set((PhoneNumberType.SHARED_COST,))
        self._checkNumbersValidAndCorrectType(PhoneNumberType.SHARED_COST, sharedCostTypes)
        self.assertEquals(0, len(self.invalid_cases))
        self.assertEquals(0, len(self.wrong_type_cases))

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
        self.assertEquals(0, len(self.wrong_type_cases))

    def testBlankMetadata(self):
        # Python version extra test
        # Some metadata is blank; check that we cope with this.
        # Example: MH (+692)
        number = phonenumberutil.parse("+6921234567", "US")
        self.assertEquals("Country Code: 692 National Number: 1234567 Leading Zero: False", str(number))
