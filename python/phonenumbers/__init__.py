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
from .phonenumberutil import (COUNTRY_CODE_TO_REGION_CODE, SUPPORTED_REGIONS, UNKNOWN_REGION,
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
                              region_code_for_number,
                              truncate_too_long_number,)
from .shortnumberutil import connects_to_emergency_number, is_emergency_number
from .phonenumbermatcher import PhoneNumberMatch, PhoneNumberMatcher, Leniency
from .geocoder import (area_description_for_number, country_name_for_number,
                       description_for_number, description_for_valid_number)


# Version number is taken from the upstream libphonenumber version
# together with an indication of the version of the Python-specific code.
__version__ = "4.6b1"

__all__ = ['PhoneNumber', 'CountryCodeSource', 'FrozenPhoneNumber',
           'REGION_CODE_FOR_NON_GEO_ENTITY', 'NumberFormat', 'PhoneNumberDesc', 'PhoneMetadata',
           'AsYouTypeFormatter',
           # items from phonenumberutil.py
           'COUNTRY_CODE_TO_REGION_CODE', 'SUPPORTED_REGIONS', 'UNKNOWN_REGION',
           'MatchType', 'NumberParseException', 'PhoneNumberFormat',
           'PhoneNumberType', 'ValidationResult',
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
           'region_code_for_number',
           'truncate_too_long_number',
           # end of items from phonenumberutil.py
           'connects_to_emergency_number', 'is_emergency_number',
           'PhoneNumberMatch', 'PhoneNumberMatcher', 'Leniency',
           'area_description_for_number',
           'country_name_for_number',
           'description_for_number',
           'description_for_valid_number',
           ]

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
