import unittest

from phonenumbers import PhoneMetadata
from phonenumbers import phonenumberutil

# Override library metadata with the test metadata.  First save the original
# data.
REAL_REGION_LOADERS = PhoneMetadata._region_available
REAL_COUNTRY_CODE_LOADERS = PhoneMetadata._country_code_available
REAL_REGION_METADATA = PhoneMetadata._region_metadata
REAL_COUNTRY_CODE_METADATA = PhoneMetadata._country_code_metadata
REAL_CC_TO_RC = phonenumberutil.COUNTRY_CODE_TO_REGION_CODE

# Clear the data dicts.
PhoneMetadata._region_available = {}
PhoneMetadata._country_code_available = {}
PhoneMetadata._region_metadata = {}
PhoneMetadata._country_code_metadata = {}
phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = {}

# Import the test data; this will re-populate the cleared
# PhoneMetadata._region_available and PhoneMetadata._country_code_available maps
from .testdata import _COUNTRY_CODE_TO_REGION_CODE as TEST_CC_TO_RC
TEST_REGION_LOADERS = PhoneMetadata._region_available
TEST_COUNTRY_CODE_LOADERS = PhoneMetadata._country_code_available
TEST_REGION_METADATA = PhoneMetadata._region_metadata
TEST_COUNTRY_CODE_METADATA = PhoneMetadata._country_code_metadata


def reinstate_real_metadata():
    """Reinstate real phone number metadata"""
    phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = REAL_CC_TO_RC
    PhoneMetadata._region_available = REAL_REGION_LOADERS
    PhoneMetadata._country_code_available = REAL_COUNTRY_CODE_LOADERS
    PhoneMetadata._region_metadata = REAL_REGION_METADATA
    PhoneMetadata._country_code_metadata = REAL_COUNTRY_CODE_METADATA
    phonenumberutil._regenerate_derived_data()


def insert_test_metadata():
    """Insert test metadata into library"""
    phonenumberutil.COUNTRY_CODE_TO_REGION_CODE = TEST_CC_TO_RC
    PhoneMetadata._region_available = TEST_REGION_LOADERS
    PhoneMetadata._country_code_available = TEST_COUNTRY_CODE_LOADERS
    PhoneMetadata._region_metadata = TEST_REGION_METADATA
    PhoneMetadata._country_code_metadata = TEST_COUNTRY_CODE_METADATA
    phonenumberutil._regenerate_derived_data()


# Reinstate the real metadata so any importers of this module are not affected
reinstate_real_metadata()


class TestMetadataTestCase(unittest.TestCase):
    def setUp(self):
        insert_test_metadata()

    def tearDown(self):
        reinstate_real_metadata()
