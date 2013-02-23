"""Auto-generated file, do not edit by hand."""
# Copyright (C) 2010-2013 The Libphonenumber Authors
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

def _load_nongeo_region_800():
    from .region_800 import PHONE_METADATA_800
PhoneMetadata.register_nongeo_region_loader(800, _load_nongeo_region_800)

def _load_nongeo_region_979():
    from .region_979 import PHONE_METADATA_979
PhoneMetadata.register_nongeo_region_loader(979, _load_nongeo_region_979)

def _load_region_AD():
    from .region_AD import PHONE_METADATA_AD
PhoneMetadata.register_region_loader('AD', _load_region_AD)

def _load_region_AE():
    from .region_AE import PHONE_METADATA_AE
PhoneMetadata.register_region_loader('AE', _load_region_AE)

def _load_region_AO():
    from .region_AO import PHONE_METADATA_AO
PhoneMetadata.register_region_loader('AO', _load_region_AO)

def _load_region_AR():
    from .region_AR import PHONE_METADATA_AR
PhoneMetadata.register_region_loader('AR', _load_region_AR)

def _load_region_AU():
    from .region_AU import PHONE_METADATA_AU
PhoneMetadata.register_region_loader('AU', _load_region_AU)

def _load_region_BR():
    from .region_BR import PHONE_METADATA_BR
PhoneMetadata.register_region_loader('BR', _load_region_BR)

def _load_region_BS():
    from .region_BS import PHONE_METADATA_BS
PhoneMetadata.register_region_loader('BS', _load_region_BS)

def _load_region_BY():
    from .region_BY import PHONE_METADATA_BY
PhoneMetadata.register_region_loader('BY', _load_region_BY)

def _load_region_DE():
    from .region_DE import PHONE_METADATA_DE
PhoneMetadata.register_region_loader('DE', _load_region_DE)

def _load_region_GB():
    from .region_GB import PHONE_METADATA_GB
PhoneMetadata.register_region_loader('GB', _load_region_GB)

def _load_region_IT():
    from .region_IT import PHONE_METADATA_IT
PhoneMetadata.register_region_loader('IT', _load_region_IT)

def _load_region_JP():
    from .region_JP import PHONE_METADATA_JP
PhoneMetadata.register_region_loader('JP', _load_region_JP)

def _load_region_KR():
    from .region_KR import PHONE_METADATA_KR
PhoneMetadata.register_region_loader('KR', _load_region_KR)

def _load_region_MX():
    from .region_MX import PHONE_METADATA_MX
PhoneMetadata.register_region_loader('MX', _load_region_MX)

def _load_region_NZ():
    from .region_NZ import PHONE_METADATA_NZ
PhoneMetadata.register_region_loader('NZ', _load_region_NZ)

def _load_region_PL():
    from .region_PL import PHONE_METADATA_PL
PhoneMetadata.register_region_loader('PL', _load_region_PL)

def _load_region_RE():
    from .region_RE import PHONE_METADATA_RE
PhoneMetadata.register_region_loader('RE', _load_region_RE)

def _load_region_SG():
    from .region_SG import PHONE_METADATA_SG
PhoneMetadata.register_region_loader('SG', _load_region_SG)

def _load_region_US():
    from .region_US import PHONE_METADATA_US
PhoneMetadata.register_region_loader('US', _load_region_US)

def _load_region_YT():
    from .region_YT import PHONE_METADATA_YT
PhoneMetadata.register_region_loader('YT', _load_region_YT)


# A mapping from a country code to the region codes which
# denote the country/region represented by that country code.
# In the case of multiple countries sharing a calling code,
# such as the NANPA countries, the one indicated with
# "main_country_for_code" in the metadata should be first.
_COUNTRY_CODE_TO_REGION_CODE = {
    1: ("US", "BS",),
    39: ("IT",),
    44: ("GB",),
    48: ("PL",),
    49: ("DE",),
    52: ("MX",),
    54: ("AR",),
    55: ("BR",),
    61: ("AU",),
    64: ("NZ",),
    65: ("SG",),
    81: ("JP",),
    82: ("KR",),
    244: ("AO",),
    262: ("RE", "YT",),
    375: ("BY",),
    376: ("AD",),
    800: ("001",),
    971: ("AE",),
    979: ("001",),
}
