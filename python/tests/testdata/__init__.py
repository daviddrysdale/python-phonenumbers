"""Auto-generated file, do not edit by hand."""
# Copyright (C) 2010-2012 The Libphonenumber Authors
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

from .region_800 import PHONE_METADATA_800
from .region_AD import PHONE_METADATA_AD
from .region_AO import PHONE_METADATA_AO
from .region_AR import PHONE_METADATA_AR
from .region_AU import PHONE_METADATA_AU
from .region_BR import PHONE_METADATA_BR
from .region_BS import PHONE_METADATA_BS
from .region_DE import PHONE_METADATA_DE
from .region_GB import PHONE_METADATA_GB
from .region_IT import PHONE_METADATA_IT
from .region_JP import PHONE_METADATA_JP
from .region_KR import PHONE_METADATA_KR
from .region_MX import PHONE_METADATA_MX
from .region_NZ import PHONE_METADATA_NZ
from .region_PL import PHONE_METADATA_PL
from .region_RE import PHONE_METADATA_RE
from .region_SG import PHONE_METADATA_SG
from .region_US import PHONE_METADATA_US
from .region_YT import PHONE_METADATA_YT

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
    376: ("AD",),
    800: ("001",),
}
