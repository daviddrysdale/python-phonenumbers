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

from .re_util import fullmatch
from .phonemetadata import PhoneMetadata
from .phonenumberutil import _extract_possible_number, _PLUS_CHARS_PATTERN
from .phonenumberutil import normalize_digits_only


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
    return _matches_emergency_number_helper(number, region_code, True)  # Allows prefix match


def is_emergency_number(number, region_code):
    """Returns true if the number exactly matches an emergency service number
    in the given region.

    This method takes into account cases where the number might contain
    formatting, but doesn't allow additional digits to be appended.

    Arguments:
    number  -- The phone number to test.
    region_code -- The region where the phone number is being dialed.

    Returns if the number exactly matches an emergency services number in the
    given region.
    """
    return _matches_emergency_number_helper(number, region_code, False)  # Doesn't allow prefix match


def _matches_emergency_number_helper(number, region_code, allow_prefix_match):
    number = _extract_possible_number(number)
    if _PLUS_CHARS_PATTERN.match(number):
        # Returns False if the number starts with a plus sign. We don't
        # believe dialing the country code before emergency numbers
        # (e.g. +1911) works, but later, if that proves to work, we can add
        # additional logic here to handle it.
        return False
    metadata = PhoneMetadata.region_metadata.get(region_code.upper(), None)
    if metadata is None or metadata.emergency is None:
        return False
    emergency_number_pattern = re.compile(metadata.emergency.national_number_pattern)
    normalized_number = normalize_digits_only(number)

    if not allow_prefix_match or region_code == "BR":
        # In Brazil, it is impossible to append additional digits to an
        # emergency number to dial the number.
        return fullmatch(emergency_number_pattern, normalized_number) is not None
    else:
        return emergency_number_pattern.match(normalized_number) is not None
