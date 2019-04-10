"""Unit tests for phonenumbers.pb2"""
import unittest

from phonenumbers import PhoneNumber, CountryCodeSource
from phonenumbers import PhoneNumberType, phonenumberutil
from phonenumbers.pb2 import PBToPy, PyToPB


class PB2ConvertTest(unittest.TestCase):
    def _checkAllExamples(self, num_type):
        for region_code in phonenumberutil.SUPPORTED_REGIONS:
            numobj_py = phonenumberutil.example_number_for_type(region_code, num_type)
            if numobj_py is not None:
                numobj_pb = PyToPB(numobj_py)
                alt_py = PBToPy(numobj_pb)
                self.assertEqual(numobj_py, alt_py)

    def testFixedLine(self):
        self._checkAllExamples(PhoneNumberType.FIXED_LINE)

    def testMobile(self):
        self._checkAllExamples(PhoneNumberType.MOBILE)

    def testTollFree(self):
        self._checkAllExamples(PhoneNumberType.TOLL_FREE)

    def testPremiumRate(self):
        self._checkAllExamples(PhoneNumberType.PREMIUM_RATE)

    def testVoip(self):
        self._checkAllExamples(PhoneNumberType.VOIP)

    def testPager(self):
        self._checkAllExamples(PhoneNumberType.PAGER)

    def testUan(self):
        self._checkAllExamples(PhoneNumberType.UAN)

    def testVoicemail(self):
        self._checkAllExamples(PhoneNumberType.VOICEMAIL)

    def testSharedCost(self):
        self._checkAllExamples(PhoneNumberType.SHARED_COST)

    def testMissingFields(self):
        fullobj = PhoneNumber(country_code=1,
                              national_number=12345678,
                              extension=123,
                              italian_leading_zero=True,
                              number_of_leading_zeros=1,
                              raw_input="+11235678",
                              country_code_source=CountryCodeSource.FROM_NUMBER_WITH_PLUS_SIGN,
                              preferred_domestic_carrier_code="123")
        fieldnames = ('country_code', 'national_number', 'extension',
                      'italian_leading_zero', 'number_of_leading_zeros',
                      'raw_input', 'preferred_domestic_carrier_code')
        for field in fieldnames:
            numobj = PhoneNumber()
            numobj.merge_from(fullobj)
            numobj.__dict__[field] = None
            pbobj = PyToPB(numobj)
            for ii in fieldnames:
                nf = numobj.__dict__[ii]
                if nf is None:
                    self.assertFalse(pbobj.HasField(ii))
                else:
                    self.assertTrue(pbobj.HasField(ii))
