#!/usr/bin/env python
import doctest
import sys
import unittest
import phonenumbers
from phonenumbers import util
from phonenumbers import re_util
from phonenumbers import unicode_util
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from tests import *

if __name__ == '__main__':
    failures = 0
    failures += doctest.testmod(phonenumbers)[0]
    failures += doctest.testmod(util)[0]
    failures += doctest.testmod(re_util)[0]
    failures += doctest.testmod(unicode_util)[0]
    failures += doctest.testmod(geocoder)[0]
    failures += doctest.testmod(carrier)[0]
    failures += doctest.testmod(timezone)[0]
    if sys.version_info < (2, 7) or (3, 0) <= sys.version_info < (3, 1):
        unittest.main()
    else:
        prog = unittest.main(exit=False)
        sys.exit(not prog.result.wasSuccessful() or bool(failures))
