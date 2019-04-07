#!/usr/bin/env python

# Original libphonenumber Java code:
#   Copyright (C) 2009-2011 The Libphonenumber Authors
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

from setuptools import setup
import sys

if sys.version_info < (2, 7):
    raise RuntimeError("Python 2.7 or newer is required")

# Discover version of phonenumbers package
from phonenumbers import __version__

# Discover whether per-prefix data is available
if 'lite' in sys.argv:
    lite = True
    del sys.argv[sys.argv.index('lite')]
else:
    lite = False
if not lite:
    try:
        import phonenumbers.tzdata
    except ImportError:
        lite = True

with io.open("README.md", mode="r", encoding="utf-8") as readme:
    long_description = readme.read()

# Various parameters depend on whether we are the lite package or not
if lite:
    pkgname = 'phonenumberslite'
    pkgs = ['phonenumbers', 'phonenumbers.data', 'phonenumbers.shortdata']
else:
    pkgname = 'phonenumbers'
    pkgs = ['phonenumbers', 'phonenumbers.data', 'phonenumbers.geodata', 'phonenumbers.shortdata',
            'phonenumbers.carrierdata', 'phonenumbers.tzdata']

setup(
    name=pkgname,
    version=__version__,
    description="Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.",
    author='David Drysdale',
    author_email='dmd@lurklurk.org',
    url='https://github.com/daviddrysdale/python-phonenumbers',
    license='Apache License 2.0',
    packages=pkgs,
    package_dir={'': 'python'},
    test_suite="tests.examplenumberstest",
    platforms='Posix; MacOS X; Windows',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Telephony',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
)
