"""Auto-generated file, do not edit by hand."""
# Copyright (C) 2010-2018 The Libphonenumber Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from phonenumbers.phonemetadata import PhoneMetadata

_AVAILABLE_REGION_CODES = ['AD','AE','AM','AO','AR','AU','BB','BR','BS','BY','CA','CC','CN','CX','DE','FR','GB','GG','HU','IT','JP','KR','MX','NZ','PL','RE','RU','SE','SG','TA','US','UZ','YT']
_AVAILABLE_NONGEO_COUNTRY_CODES = [800, 882, 979]

def _load_region(code):
    __import__("region_%s" % code, globals(), locals(),
               fromlist=["PHONE_METADATA_%s" % code], level=1)

for region_code in _AVAILABLE_REGION_CODES:
    PhoneMetadata.register_region_loader(region_code, _load_region)


for country_code in _AVAILABLE_NONGEO_COUNTRY_CODES:
    PhoneMetadata.register_nongeo_region_loader(country_code, _load_region)


# A mapping from a country code to the region codes which
# denote the country/region represented by that country code.
# In the case of multiple countries sharing a calling code,
# such as the NANPA countries, the one indicated with
# "main_country_for_code" in the metadata should be first.
_COUNTRY_CODE_TO_REGION_CODE = {
    1: ("US", "BB", "BS", "CA",),
    7: ("RU",),
    33: ("FR",),
    36: ("HU",),
    39: ("IT",),
    44: ("GB", "GG",),
    46: ("SE",),
    48: ("PL",),
    49: ("DE",),
    52: ("MX",),
    54: ("AR",),
    55: ("BR",),
    61: ("AU", "CC", "CX",),
    64: ("NZ",),
    65: ("SG",),
    81: ("JP",),
    82: ("KR",),
    86: ("CN",),
    244: ("AO",),
    262: ("RE", "YT",),
    290: ("TA",),
    374: ("AM",),
    375: ("BY",),
    376: ("AD",),
    800: ("001",),
    882: ("001",),
    971: ("AE",),
    979: ("001",),
    998: ("UZ",),
}
