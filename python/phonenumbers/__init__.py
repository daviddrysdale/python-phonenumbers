"""Python phone number parsing and formatting library

Examples of use:

>>> import phonenumbers
>>> x = phonenumbers.parse("+442083661177", None)
>>> print x
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> type(x)
<class 'phonenumbers.phonenumber.PhoneNumber'>
>>> str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))
'020 8366 1177'
>>> str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
'+44 20 8366 1177'
>>> str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164))
'+442083661177'
>>> y = phonenumbers.parse("020 8366 1177", "GB")
>>> print y
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> x == y
True
>>>
>>> formatter = phonenumbers.AsYouTypeFormatter("US")
>>> print formatter.input_digit("6")
6
>>> print formatter.input_digit("5")
65
>>> print formatter.input_digit("0")
650
>>> print formatter.input_digit("2")
650-2
>>> print formatter.input_digit("5")
650-25
>>> print formatter.input_digit("3")
650-253
>>> print formatter.input_digit("2")
650-2532
>>> print formatter.input_digit("2")
(650) 253-22
>>> print formatter.input_digit("2")
(650) 253-222
>>> print formatter.input_digit("2")
(650) 253-2222
>>>
>>> text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
>>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
...     print match
...
PhoneNumberMatch [11,23) 510-748-8230
PhoneNumberMatch [51,62) 703-4800500
>>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
...     print phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
...
+15107488230
+17034800500
>>>
"""

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
#
# 'Some people, when confronted with a problem, think "I know,
# I'll use regular expressions."  Now they have two problems.'
#                                                   -- jwz 1997-08-12

# Data class definitions
from .phonenumber import PhoneNumber, CountryCodeSource, FrozenPhoneNumber
from .phonemetadata import REGION_CODE_FOR_NON_GEO_ENTITY, NumberFormat, PhoneNumberDesc, PhoneMetadata
# Functionality
from .asyoutypeformatter import AsYouTypeFormatter
from .phonenumberutil import (COUNTRY_CODE_TO_REGION_CODE, SUPPORTED_REGIONS, SUPPORTED_SHORT_REGIONS, UNKNOWN_REGION,
                              MatchType, NumberParseException, PhoneNumberFormat,
                              PhoneNumberType, ValidationResult,
                              convert_alpha_characters_in_number,
                              country_code_for_region,
                              country_code_for_valid_region,
                              example_number,
                              example_number_for_type,
                              example_number_for_non_geo_entity,
                              format_by_pattern,
                              format_in_original_format,
                              format_national_number_with_carrier_code,
                              format_national_number_with_preferred_carrier_code,
                              format_number_for_mobile_dialing,
                              format_number,
                              format_out_of_country_calling_number,
                              format_out_of_country_keeping_alpha_chars,
                              is_alpha_number,
                              is_nanpa_country,
                              is_number_match,
                              is_possible_number,
                              is_possible_number_string,
                              is_possible_number_with_reason,
                              is_valid_number,
                              is_valid_number_for_region,
                              length_of_geographical_area_code,
                              length_of_national_destination_code,
                              national_significant_number,
                              ndd_prefix_for_region,
                              normalize_digits_only,
                              number_type,
                              parse,
                              region_code_for_country_code,
                              region_codes_for_country_code,
                              region_code_for_number,
                              truncate_too_long_number,)
from .shortnumberinfo import (ShortNumberCost,
                              is_possible_short_number,
                              is_possible_short_number_object,
                              is_valid_short_number,
                              is_valid_short_number_object,
                              expected_cost,
                              connects_to_emergency_number,
                              is_emergency_number,
                              is_carrier_specific)
from .phonenumbermatcher import PhoneNumberMatch, PhoneNumberMatcher, Leniency


# The geodata occupies a lot of space, so only perform the import on first use
# of geocoder functionality.
def country_name_for_number(*args, **kwargs):
    """Return the given PhoneNumber object's country name in the given language.

    Arguments:
    numobj -- The PhoneNumber object for which we want to get a text description.
    lang -- A 2-letter lowercase ISO 639-1 language code for the language in
                  which the description should be returned (e.g. "en")
    script -- A 4-letter titlecase (first letter uppercase, rest lowercase)
                  ISO script code as defined in ISO 15924, separated by an
                  underscore (e.g. "Hant")
    region --  A 2-letter uppercase ISO 3166-1 country code (e.g. "GB")

    The script and region parameters are currently ignored.

    Returns a text description in the given language code, for the given phone
    number's region, or an empty string if no description is available."""
    from .geocoder import country_name_for_number as real_fn
    return real_fn(*args, **kwargs)


def description_for_number(*args, **kwargs):
    """Return a text description of a PhoneNumber object for the given language.

    The description might consist of the name of the country where the phone
    number is from and/or the name of the geographical area the phone number
    is from.  This function explicitly checks the validity of the number passed in

    Arguments:
    numobj -- The PhoneNumber object for which we want to get a text description.
    lang -- A 2-letter lowercase ISO 639-1 language code for the language in
                  which the description should be returned (e.g. "en")
    script -- A 4-letter titlecase (first letter uppercase, rest lowercase)
                  ISO script code as defined in ISO 15924, separated by an
                  underscore (e.g. "Hant")
    region --  A 2-letter uppercase ISO 3166-1 country code (e.g. "GB")

    Returns a text description in the given language code, for the given phone
    number, or an empty string if no description is available."""
    from .geocoder import description_for_number as real_fn
    return real_fn(*args, **kwargs)


def description_for_valid_number(*args, **kwargs):
    """Return a text description of a PhoneNumber object, in the language
    provided.

    The description might consist of the name of the country where the phone
    number is from and/or the name of the geographical area the phone number
    is from if more detailed information is available.

    If the phone number is from the same region as the user, only a
    lower-level description will be returned, if one exists. Otherwise, the
    phone number's region will be returned, with optionally some more detailed
    information.

    For example, for a user from the region "US" (United States), we would
    show "Mountain View, CA" for a particular number, omitting the United
    States from the description. For a user from the United Kingdom (region
    "GB"), for the same number we may show "Mountain View, CA, United States"
    or even just "United States".

    This function assumes the validity of the number passed in has already
    been checked, and that the number is suitable for geocoding.  We consider
    fixed-line and mobile numbers possible candidates for geocoding.

    Arguments:
    numobj -- A valid PhoneNumber object for which we want to get a text
                  description.
    lang -- A 2-letter lowercase ISO 639-1 language code for the language in
                  which the description should be returned (e.g. "en")
    script -- A 4-letter titlecase (first letter uppercase, rest lowercase)
                  ISO script code as defined in ISO 15924, separated by an
                  underscore (e.g. "Hant")
    region -- The region code for a given user. This region will be omitted
                  from the description if the phone number comes from this
                  region. It is a two-letter uppercase ISO country code as
                  defined by ISO 3166-1.

    Returns a text description in the given language code, for the given phone
    number, or an empty string if no description is available."""
    from .geocoder import description_for_valid_number as real_fn
    return real_fn(*args, **kwargs)


# Version number is taken from the upstream libphonenumber version
# together with an indication of the version of the Python-specific code.
__version__ = "5.8b1"

__all__ = ['PhoneNumber', 'CountryCodeSource', 'FrozenPhoneNumber',
           'REGION_CODE_FOR_NON_GEO_ENTITY', 'NumberFormat', 'PhoneNumberDesc', 'PhoneMetadata',
           'AsYouTypeFormatter',
           # items from phonenumberutil.py
           'COUNTRY_CODE_TO_REGION_CODE', 'SUPPORTED_REGIONS', 'SUPPORTED_SHORT_REGIONS',
           'UNKNOWN_REGION', 'NON_DIGITS_PATTERN',
           'MatchType', 'NumberParseException', 'PhoneNumberFormat',
           'PhoneNumberType', 'ValidationResult',
           'choose_formatting_pattern_for_number',
           'convert_alpha_characters_in_number',
           'country_code_for_region',
           'country_code_for_valid_region',
           'example_number',
           'example_number_for_type',
           'example_number_for_non_geo_entity',
           'format_by_pattern',
           'format_in_original_format',
           'format_national_number_with_carrier_code',
           'format_national_number_with_preferred_carrier_code',
           'format_nsn_using_pattern',
           'format_number_for_mobile_dialing',
           'format_number',
           'format_out_of_country_calling_number',
           'format_out_of_country_keeping_alpha_chars',
           'is_alpha_number',
           'is_nanpa_country',
           'is_number_match',
           'is_possible_number',
           'is_possible_number_string',
           'is_possible_number_with_reason',
           'is_valid_number',
           'is_valid_number_for_region',
           'length_of_geographical_area_code',
           'length_of_national_destination_code',
           'national_significant_number',
           'ndd_prefix_for_region',
           'normalize_digits_only',
           'number_type',
           'parse',
           'region_code_for_country_code',
           'region_codes_for_country_code',
           'region_code_for_number',
           'truncate_too_long_number',
           # end of items from phonenumberutil.py
           # items from shortnumberinfo.py
           'ShortNumberCost',
           'is_possible_short_number',
           'is_possible_short_number_object',
           'is_valid_short_number',
           'is_valid_short_number_object',
           'expected_cost',
           'connects_to_emergency_number',
           'is_emergency_number',
           'is_carrier_specific',
           # end of items from shortnumberinfo.py
           'PhoneNumberMatch', 'PhoneNumberMatcher', 'Leniency',
           'country_name_for_number',
           'description_for_number',
           'description_for_valid_number',
           ]

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
