#!/usr/bin/env python
import doctest
import unittest
import phonenumbers.pb2
from tests.pb2 import *

if __name__ == '__main__':
    doctest.testmod(phonenumbers.pb2)
    unittest.main()
