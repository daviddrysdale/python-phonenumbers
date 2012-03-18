import unittest

from phonenumbers import PhoneMetadata
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


class TestMetadataTestCase(unittest.TestCase):
    def setUp(self):
        insert_test_metadata()

    def tearDown(self):
        reinstate_real_metadata()
