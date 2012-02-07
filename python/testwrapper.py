#!/usr/bin/env python
import doctest
import unittest
import phonenumbers
from phonenumbers import util
from phonenumbers import re_util
from phonenumbers import unicode_util
from phonenumbers import geocoder
from tests import *

if __name__ == '__main__':
    doctest.testmod(phonenumbers)
    doctest.testmod(util)
    doctest.testmod(re_util)
    doctest.testmod(unicode_util)
    doctest.testmod(geocoder)
    unittest.main()
