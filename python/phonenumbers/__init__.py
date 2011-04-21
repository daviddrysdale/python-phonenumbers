"""Python phone number parsing and formatting library

Examples of use:

>>> import phonenumbers
>>> x = phonenumbers.parse("+442083661177", None)
>>> print x
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> type(x)
<class 'phonenumbers.phonenumber.PhoneNumber'>
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
u'020 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
u'+44 20 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
u'+442083661177'
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
(650
>>> print formatter.input_digit("2")
(650) 2
>>> print formatter.input_digit("5")
(650) 25
>>> print formatter.input_digit("3")
(650) 253
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
from phonenumber import PhoneNumber, CountryCodeSource
from phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata
# Functionality
from asyoutypeformatter import AsYouTypeFormatter
from phonenumberutil import *
from phonenumbermatcher import PhoneNumberMatch, PhoneNumberMatcher

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
