"""Python phone number parsing and formatting library"""

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
