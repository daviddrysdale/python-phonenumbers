"""Methods for getting information about short phone numbers,
such as short codes and emergency numbers.

Note most commercial short numbers are not handled here, but by phonenumberutil.py
"""
# Based on original Java code:
#     java/src/com/google/i18n/phonenumbers/ShortNumberInfo.java
# Copyright (C) 2013 The Libphonenumber Authors
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
from .phonenumberutil import normalize_digits_only, region_codes_for_country_code
from .phonenumberutil import national_significant_number
from .phonenumberutil import _is_number_possible_for_desc, _is_number_matching_desc


class ShortNumberCost(object):
    """Cost categories of short numbers."""
    TOLL_FREE = 0
    STANDARD_RATE = 1
    PREMIUM_RATE = 2
    UNKNOWN_COST = 3


def is_possible_short_number(short_number, region_dialing_from):
    """Check whether a short number is a possible number, given the number in
    the form of a string, and the region where the number is dialed from. This
    provides a more lenient check than is_valid_short_number.

    Arguments:
    short_number -- the short number to check as a string
    region_dialing_from -- the region from which the number is dialed

    Return whether the number is a possible short number.
    """
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    if metadata is None:
        return False
    general_desc = metadata.general_desc
    return _is_number_possible_for_desc(short_number, general_desc)


def is_possible_short_number_object(numobj):
    """Check whether a short number is a possible number.  This provides a
    more lenient check than is_valid_short_number.

    Arguments:
    numobj -- the short number to check

    Return whether the number is a possible short number.
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    short_number = national_significant_number(numobj)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    if len(region_codes) > 1 and region_code is not None:
        # If a matching region had been found for the phone number from among two or more regions,
        # then we have already implicitly verified its validity for that region.
        return True
    return is_possible_short_number(short_number, region_code)


def is_valid_short_number(short_number, region_dialing_from):
    """Tests whether a short number matches a valid pattern. Note that this
    doesn't verify the number is actually in use, which is impossible to tell
    by just looking at the number itself.

    Arguments:
    short_number -- the short number to check as a string
    region_dialing_from -- the region from which the number is dialed

    Return whether the short number matches a valid pattern
    """
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    if metadata is None:
        return False
    general_desc = metadata.general_desc
    if (general_desc.national_number_pattern is None or
        not _is_number_matching_desc(short_number, general_desc)):
        return False
    short_number_desc = metadata.short_code
    if short_number_desc.national_number_pattern is None:  # pragma no cover
        return False
    return _is_number_matching_desc(short_number, short_number_desc)


def is_valid_short_number_object(numobj):
    """Tests whether a short number matches a valid pattern. Note that this
    doesn't verify the number is actually in use, which is impossible to tell by
    just looking at the number itself. See is_valid_short_number for details.

    Arguments:
    numobj - the short number for which we want to test the validity

    Return whether the short number matches a valid pattern
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    short_number = national_significant_number(numobj)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    if len(region_codes) > 1 and region_code is not None:
        # If a matching region had been found for the phone number from among two or more regions,
        # then we have already implicitly verified its validity for that region.
        return True
    return is_valid_short_number(short_number, region_code)


def expected_cost(numobj):
    """Gets the expected cost category of a short number (however, nothing is
    implied about its validity). If it is important that the number is valid,
    then its validity must first be checked using is_valid_short_number. Note
    that emergency numbers are always considered toll-free.

    Example usage:
    number = phonenumbers.parse("110", "FR");
    if phonenumbers.is_valid_short_number(number):
        cost = phonenumbers.expected_cost(number)  # ShortNumberCost
        # Do something with the cost information here.

    Arguments:
    numobj -- the short number for which we want to know the expected cost category

    Return the expected cost category of the short number. Returns
    UNKNOWN_COST if the number does not match a cost category. Note that an
    invalid number may match any cost category.
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    # Note that regionCode may be None, in which case metadata will also be None.
    metadata = PhoneMetadata.short_metadata_for_region(region_code)
    if metadata is None:
        return ShortNumberCost.UNKNOWN_COST
    national_number = national_significant_number(numobj)

    # The cost categories are tested in order of decreasing expense, since if
    # for some reason the patterns overlap the most expensive matching cost
    # category should be returned.
    if _is_number_matching_desc(national_number, metadata.premium_rate):
        return ShortNumberCost.PREMIUM_RATE
    if _is_number_matching_desc(national_number, metadata.standard_rate):
        return ShortNumberCost.STANDARD_RATE
    if _is_number_matching_desc(national_number, metadata.toll_free):
        return ShortNumberCost.TOLL_FREE
    if is_emergency_number(national_number, region_code):
        # Emergency numbers are implicitly toll-free.
        return ShortNumberCost.TOLL_FREE
    return ShortNumberCost.UNKNOWN_COST


def _region_code_for_short_number_from_region_list(numobj, region_codes):
    """Helper method to get the region code for a given phone number, from a list of possible region
    codes. If the list contains more than one region, the first region for which the number is
    valid is returned.
    """
    if len(region_codes) == 0:
        return None
    elif len(region_codes) == 1:
        return region_codes[0]
    national_number = national_significant_number(numobj)
    for region_code in region_codes:
        metadata = PhoneMetadata.short_metadata_for_region(region_code)
        if metadata is not None and _is_number_matching_desc(national_number, metadata.short_code):
            # The number is valid for this region.
            return region_code
    return None


def _example_short_number(region_code):
    """Gets a valid short number for the specified region.

    Arguments:
    region_code -- the region for which an example short number is needed.

    Returns a valid short number for the specified region. Returns an empty
    string when the metadata does not contain such information.
    """
    metadata = PhoneMetadata.short_metadata_for_region(region_code)
    if metadata is None:
        return u""
    desc = metadata.short_code
    if desc.example_number is not None:
        return desc.example_number
    return u""


def _example_short_number_for_cost(region_code, cost):
    """Gets a valid short number for the specified cost category.

    Arguments:
    region_code -- the region for which an example short number is needed.
    cost -- the cost category of number that is needed.

    Returns a valid short number for the specified region and cost
    category. Returns an empty string when the metadata does not contain such
    information, or the cost is UNKNOWN_COST.
    """
    metadata = PhoneMetadata.short_metadata_for_region(region_code)
    if metadata is None:
        return u""
    desc = None
    if cost == ShortNumberCost.TOLL_FREE:
        desc = metadata.toll_free
    elif cost == ShortNumberCost.STANDARD_RATE:
        desc = metadata.standard_rate
    elif cost == ShortNumberCost.PREMIUM_RATE:
        desc = metadata.premium_rate
    else:
        # ShortNumberCost.UNKNOWN_COST numbers are computed by the process of
        # elimination from the other cost categoried.
        pass
    if desc is not None and desc.example_number is not None:
        return desc.example_number
    return u""


def connects_to_emergency_number(number, region_code):
    """Returns whether the number might be used to connect to an emergency
    service in the given region.

    This function takes into account cases where the number might contain
    formatting, or might have additional digits appended (when it is okay to
    do that in the region specified).

    Arguments:
    number -- The phone number to test.
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
    number -- The phone number to test.
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
    metadata = PhoneMetadata.short_metadata_for_region(region_code.upper(), None)
    if metadata is None or metadata.emergency is None:
        return False
    emergency_number_pattern = re.compile(metadata.emergency.national_number_pattern)
    normalized_number = normalize_digits_only(number)

    if not allow_prefix_match or region_code == "BR" or region_code == "CL":
        # In Brazil and Chile, emergency numbers don't work when additional digits are appended.
        return fullmatch(emergency_number_pattern, normalized_number) is not None
    else:
        return emergency_number_pattern.match(normalized_number) is not None


def is_carrier_specific(numobj):
    """Given a valid short number, determines whether it is carrier-specific
    (however, nothing is implied about its validity).  If it is important that
    the number is valid, then its validity must first be checked using
    is_valid_short_number

    Arguments:
    numobj -- the valid short number to check

    Returns whether the short number is carrier-specific (assuming the input
    was a valid short number).
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    national_number = national_significant_number(numobj)
    metadata = PhoneMetadata.short_metadata_for_region(region_code)
    return (metadata is not None and _is_number_matching_desc(national_number, metadata.carrier_specific))
