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
from .util import U_EMPTY_STRING, prnt
from .phonemetadata import PhoneMetadata
from .phonenumberutil import _extract_possible_number, _PLUS_CHARS_PATTERN
from .phonenumberutil import normalize_digits_only, region_codes_for_country_code
from .phonenumberutil import national_significant_number, _match_national_number


# Import auto-generated data structures
try:
    from .shortdata import _AVAILABLE_REGION_CODES as _AVAILABLE_SHORT_REGION_CODES
except ImportError:  # pragma no cover
    # Before the generated code exists, the shortdata/ directory is empty.
    # The generation process imports this module, creating a circular
    # dependency.  The hack below works around this.
    import os
    import sys
    if (os.path.basename(sys.argv[0]) == "buildmetadatafromxml.py" or
        os.path.basename(sys.argv[0]) == "buildprefixdata.py"):
        prnt("Failed to import generated shortdata (but OK as during autogeneration)", file=sys.stderr)
        _AVAILABLE_SHORT_REGION_CODES = []
    else:
        raise

SUPPORTED_SHORT_REGIONS = _AVAILABLE_SHORT_REGION_CODES

# In these countries, if extra digits are added to an emergency number, it no longer connects
# to the emergency service.
_REGIONS_WHERE_EMERGENCY_NUMBERS_MUST_BE_EXACT = {"BR", "CL", "NI"}


class ShortNumberCost(object):
    """Cost categories of short numbers."""
    TOLL_FREE = 0
    STANDARD_RATE = 1
    PREMIUM_RATE = 2
    UNKNOWN_COST = 3


def _region_dialing_from_matches_number(numobj, region_dialing_from):
    """Helper method to check that the country calling code of the number matches
    the region it's being dialed from."""
    region_codes = region_codes_for_country_code(numobj.country_code)
    return (region_dialing_from in region_codes)


def is_possible_short_number_for_region(short_numobj, region_dialing_from):
    """Check whether a short number is a possible number when dialled from a
    region. This provides a more lenient check than
    is_valid_short_number_for_region.

    Arguments:
    short_numobj -- the short number to check as a PhoneNumber object.
    region_dialing_from -- the region from which the number is dialed

    Return whether the number is a possible short number.
    """
    if not _region_dialing_from_matches_number(short_numobj, region_dialing_from):
        return False
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    if metadata is None:  # pragma no cover
        return False
    short_numlen = len(national_significant_number(short_numobj))
    return (short_numlen in metadata.general_desc.possible_length)


def is_possible_short_number(numobj):
    """Check whether a short number is a possible number.

    If a country calling code is shared by multiple regions, this returns True
    if it's possible in any of them. This provides a more lenient check than
    is_valid_short_number.

    Arguments:
    numobj -- the short number to check

    Return whether the number is a possible short number.
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    short_number_len = len(national_significant_number(numobj))

    for region in region_codes:
        metadata = PhoneMetadata.short_metadata_for_region(region)
        if metadata is None:
            continue
        if short_number_len in metadata.general_desc.possible_length:
            return True
    return False


def is_valid_short_number_for_region(short_numobj, region_dialing_from):
    """Tests whether a short number matches a valid pattern in a region.

    Note that this doesn't verify the number is actually in use, which is
    impossible to tell by just looking at the number itself.

    Arguments:
    short_numobj -- the short number to check as a PhoneNumber object.
    region_dialing_from -- the region from which the number is dialed

    Return whether the short number matches a valid pattern
    """
    if not _region_dialing_from_matches_number(short_numobj, region_dialing_from):
        return False
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    if metadata is None:  # pragma no cover
        return False
    short_number = national_significant_number(short_numobj)
    general_desc = metadata.general_desc
    if not _matches_possible_number_and_national_number(short_number, general_desc):
        return False
    short_number_desc = metadata.short_code
    if short_number_desc.national_number_pattern is None:  # pragma no cover
        return False
    return _matches_possible_number_and_national_number(short_number, short_number_desc)


def is_valid_short_number(numobj):
    """Tests whether a short number matches a valid pattern.

    If a country calling code is shared by multiple regions, this returns True
    if it's valid in any of them. Note that this doesn't verify the number is
    actually in use, which is impossible to tell by just looking at the number
    itself. See is_valid_short_number_for_region for details.

    Arguments:
    numobj - the short number for which we want to test the validity

    Return whether the short number matches a valid pattern
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    if len(region_codes) > 1 and region_code is not None:
        # If a matching region had been found for the phone number from among two or more regions,
        # then we have already implicitly verified its validity for that region.
        return True
    return is_valid_short_number_for_region(numobj, region_code)


def expected_cost_for_region(short_numobj, region_dialing_from):
    """Gets the expected cost category of a short number when dialled from a
    region (however, nothing is implied about its validity). If it is
    important that the number is valid, then its validity must first be
    checked using is_valid_short_number_for_region. Note that emergency
    numbers are always considered toll-free.

    Example usage:
    short_number = "110"
    region_code = "FR"
    if phonenumbers.is_valid_short_number_for_region(short_number, region_code):
        cost = phonenumbers.expected_cost(short_number, region_code)  # ShortNumberCost
        # Do something with the cost information here.

    Arguments:
    short_numobj -- the short number for which we want to know the expected cost category
              as a PhoneNumber object.
    region_dialing_from -- the region from which the number is dialed

    Return the expected cost category for that region of the short
    number. Returns UNKNOWN_COST if the number does not match a cost
    category. Note that an invalid number may match any cost category.
    """
    if not _region_dialing_from_matches_number(short_numobj, region_dialing_from):
        return ShortNumberCost.UNKNOWN_COST
    # Note that region_dialing_from may be None, in which case metadata will also be None.
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    if metadata is None:  # pragma no cover
        return ShortNumberCost.UNKNOWN_COST
    short_number = national_significant_number(short_numobj)

    # The possible lengths are not present for a particular sub-type if they match the general
    # description; for this reason, we check the possible lengths against the general description
    # first to allow an early exit if possible.
    if not(len(short_number) in metadata.general_desc.possible_length):
        return ShortNumberCost.UNKNOWN_COST

    # The cost categories are tested in order of decreasing expense, since if
    # for some reason the patterns overlap the most expensive matching cost
    # category should be returned.
    if _matches_possible_number_and_national_number(short_number, metadata.premium_rate):
        return ShortNumberCost.PREMIUM_RATE
    if _matches_possible_number_and_national_number(short_number, metadata.standard_rate):
        return ShortNumberCost.STANDARD_RATE
    if _matches_possible_number_and_national_number(short_number, metadata.toll_free):
        return ShortNumberCost.TOLL_FREE
    if is_emergency_number(short_number, region_dialing_from):  # pragma no cover
        # Emergency numbers are implicitly toll-free.
        return ShortNumberCost.TOLL_FREE
    return ShortNumberCost.UNKNOWN_COST


def expected_cost(numobj):
    """Gets the expected cost category of a short number (however, nothing is
    implied about its validity). If the country calling code is unique to a
    region, this method behaves exactly the same as
    expected_cost_for_region. However, if the country calling code is
    shared by multiple regions, then it returns the highest cost in the
    sequence PREMIUM_RATE, UNKNOWN_COST, STANDARD_RATE, TOLL_FREE. The reason
    for the position of UNKNOWN_COST in this order is that if a number is
    UNKNOWN_COST in one region but STANDARD_RATE or TOLL_FREE in another, its
    expected cost cannot be estimated as one of the latter since it might be a
    PREMIUM_RATE number.

    For example, if a number is STANDARD_RATE in the US, but TOLL_FREE in
    Canada, the expected cost returned by this method will be STANDARD_RATE,
    since the NANPA countries share the same country calling code.

    Note: If the region from which the number is dialed is known, it is highly preferable to call
    expected_cost_for_region instead.

    Arguments:
    numobj -- the short number for which we want to know the expected cost category

    Return the highest expected cost category of the short number in the
    region(s) with the given country calling code
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    if len(region_codes) == 0:
        return ShortNumberCost.UNKNOWN_COST
    if len(region_codes) == 1:
        return expected_cost_for_region(numobj, region_codes[0])
    cost = ShortNumberCost.TOLL_FREE
    for region_code in region_codes:
        cost_for_region = expected_cost_for_region(numobj, region_code)
        if cost_for_region == ShortNumberCost.PREMIUM_RATE:
            return ShortNumberCost.PREMIUM_RATE
        elif cost_for_region == ShortNumberCost.UNKNOWN_COST:
            return ShortNumberCost.UNKNOWN_COST
        elif cost_for_region == ShortNumberCost.STANDARD_RATE:
            if cost != ShortNumberCost.UNKNOWN_COST:
                cost = ShortNumberCost.STANDARD_RATE
        elif cost_for_region == ShortNumberCost.TOLL_FREE:
            # Do nothing
            pass
        else:  # pragma no cover
            raise Exception("Unrecognized cost for region: %s", cost_for_region)
    return cost


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
        if metadata is not None and _matches_possible_number_and_national_number(national_number, metadata.short_code):
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
        return U_EMPTY_STRING
    desc = metadata.short_code
    if desc.example_number is not None:
        return desc.example_number
    return U_EMPTY_STRING


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
        return U_EMPTY_STRING
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
    return U_EMPTY_STRING


def connects_to_emergency_number(number, region_code):
    """Returns whether the given number, exactly as dialled, might be used to
    connect to an emergency service in the given region.

    This function accepts a string, rather than a PhoneNumber, because it
    needs to distinguish cases such as "+1 911" and "911", where the former
    may not connect to an emergency service in all cases but the latter would.

    This function takes into account cases where the number might contain
    formatting, or might have additional digits appended (when it is okay to
    do that in the specified region).

    Arguments:
    number -- The phone number to test.
    region_code -- The region where the phone number is being dialed.

    Returns whether the number might be used to connect to an emergency
    service in the given region.
    """
    return _matches_emergency_number_helper(number, region_code, True)  # Allows prefix match


def is_emergency_number(number, region_code):
    """Returns true if the given number exactly matches an emergency service
    number in the given region.

    This method takes into account cases where the number might contain
    formatting, but doesn't allow additional digits to be appended.  Note that
    is_emergency_number(number, region) implies
    connects_to_emergency_number(number, region).

    Arguments:
    number -- The phone number to test.
    region_code -- The region where the phone number is being dialed.

    Returns if the number exactly matches an emergency services number in the
    given region.
    """
    return _matches_emergency_number_helper(number, region_code, False)  # Doesn't allow prefix match


def _matches_emergency_number_helper(number, region_code, allow_prefix_match):
    possible_number = _extract_possible_number(number)
    if _PLUS_CHARS_PATTERN.match(possible_number):
        # Returns False if the number starts with a plus sign. We don't
        # believe dialing the country code before emergency numbers
        # (e.g. +1911) works, but later, if that proves to work, we can add
        # additional logic here to handle it.
        return False
    metadata = PhoneMetadata.short_metadata_for_region(region_code.upper(), None)
    if metadata is None or metadata.emergency is None:
        return False

    normalized_number = normalize_digits_only(possible_number)
    allow_prefix_match_for_region = (allow_prefix_match and
                                     (region_code not in _REGIONS_WHERE_EMERGENCY_NUMBERS_MUST_BE_EXACT))
    return _match_national_number(normalized_number, metadata.emergency,
                                  allow_prefix_match_for_region)


def is_carrier_specific(numobj):
    """Given a valid short number, determines whether it is carrier-specific
    (however, nothing is implied about its validity).  Carrier-specific numbers
    may connect to a different end-point, or not connect at all, depending
    on the user's carrier. If it is important that the number is valid, then
    its validity must first be checked using is_valid_short_number or
    is_valid_short_number_for_region.

    Arguments:
    numobj -- the valid short number to check

    Returns whether the short number is carrier-specific, assuming the input
    was a valid short number.
    """
    region_codes = region_codes_for_country_code(numobj.country_code)
    region_code = _region_code_for_short_number_from_region_list(numobj, region_codes)
    national_number = national_significant_number(numobj)
    metadata = PhoneMetadata.short_metadata_for_region(region_code)
    return (metadata is not None and
            _matches_possible_number_and_national_number(national_number, metadata.carrier_specific))


def is_carrier_specific_for_region(numobj, region_dialing_from):
    """Given a valid short number, determines whether it is carrier-specific when
    dialed from the given region (however, nothing is implied about its
    validity). Carrier-specific numbers may connect to a different end-point,
    or not connect at all, depending on the user's carrier. If it is important
    that the number is valid, then its validity must first be checked using
    isValidShortNumber or isValidShortNumberForRegion. Returns false if the
    number doesn't match the region provided.

    Arguments:
    numobj -- the valid short number to check
    region_dialing_from -- the region from which the number is dialed

    Returns whether the short number is carrier-specific, assuming the input
    was a valid short number.
    """
    if not _region_dialing_from_matches_number(numobj, region_dialing_from):
        return False
    national_number = national_significant_number(numobj)
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    return (metadata is not None and
            _matches_possible_number_and_national_number(national_number, metadata.carrier_specific))


def is_sms_service_for_region(numobj, region_dialing_from):
    """Given a valid short number, determines whether it is an SMS service
    (however, nothing is implied about its validity). An SMS service is where
    the primary or only intended usage is to receive and/or send text messages
    (SMSs). This includes MMS as MMS numbers downgrade to SMS if the other
    party isn't MMS-capable. If it is important that the number is valid, then
    its validity must first be checked using is_valid_short_number or
    is_valid_short_number_for_region.  Returns False if the number doesn't
    match the region provided.

    Arguments:
    numobj -- the valid short number to check
    region_dialing_from -- the region from which the number is dialed

    Returns whether the short number is an SMS service in the provided region,
    assuming the input was a valid short number.
    """
    if not _region_dialing_from_matches_number(numobj, region_dialing_from):
        return False
    metadata = PhoneMetadata.short_metadata_for_region(region_dialing_from)
    return (metadata is not None and
            _matches_possible_number_and_national_number(national_significant_number(numobj), metadata.sms_services))


# TODO: Once we have benchmarked ShortNumberInfo, consider if it is worth
# keeping this performance optimization.
def _matches_possible_number_and_national_number(number, number_desc):
    if number_desc is None:
        return False
    if len(number_desc.possible_length) > 0 and not (len(number) in number_desc.possible_length):
        return False
    return _match_national_number(number, number_desc, False)
