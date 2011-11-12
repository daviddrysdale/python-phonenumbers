#!/usr/bin/env python
import unittest

from .phonenumbertest import PhoneNumberTest
from .phonenumberutiltest import PhoneNumberUtilTest
from .shortnumberutiltest import ShortNumberUtilTest
from .asyoutypetest import AsYouTypeFormatterTest
from .examplenumberstest import ExampleNumbersTest
from .phonenumbermatchertest import PhoneNumberMatchTest, PhoneNumberMatcherTest
from .geocodertest import PhoneNumberGeocoderTest

if __name__ == '__main__':
    unittest.main()
