"""Utility for international short phone numbers, such as short codes and emergency numbers.

Note most commercial short numbers are not handled here, but by phonenumberutil.py
"""
# Based on original Java code:
#     java/src/com/google/i18n/phonenumbers/ShortNumberUtil.java
# Copyright (C) 2011 The Libphonenumber Authors
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
import re

from re_util import fullmatch
from phonemetadata import PhoneMetadata
from phonenumberutil import _extract_possible_number, _PLUS_CHARS_PATTERN
from phonenumberutil import normalize_digits_only


def connects_to_emergency_number(number, region_code):
    """Returns whether the number might be used to connect to an emergency
    service in the given region.

    This function takes into account cases where the number might contain
    formatting, or might have additional digits appended (when it is okay to
    do that in the region specified).

    Arguments:
    number  -- The phone number to test.
    region_code -- The region where the phone number is being dialed.

    Returns whether the number might be used to connect to an emergency
    service in the given region.
    """
    number = _extract_possible_number(number)
    if _PLUS_CHARS_PATTERN.match(number):
        # Returns False if the number starts with a plus sign. We don't
        # believe dialing the country code before emergency numbers
        # (e.g. +1911) works, but later, if that proves to work, we can add
        # additional logic here to handle it.
        return False
    normalized_number = normalize_digits_only(number)
    metadata = PhoneMetadata.region_metadata.get(region_code.upper(), None)
    emergency_number_desc = metadata.emergency
    emergency_number_pattern = re.compile(emergency_number_desc.national_number_pattern)
    if region_code == "BR":
        # This is to prevent Brazilian local numbers which start with 911
        # being incorrectly classified as emergency numbers. In Brazil, it is
        # impossible to append additional digits to an emergency number to
        # dial the number.
        if not fullmatch(emergency_number_pattern, normalized_number):
            return False
    # Check the prefix against possible emergency numbers for this region.
    return emergency_number_pattern.match(normalized_number) is not None
