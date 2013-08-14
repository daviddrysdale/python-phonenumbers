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

from ..phonemetadata import PhoneMetadata

_AVAILABLE_REGION_CODES = ['AM','AR','BD','BR','CH','CR','CU','CZ','DE','EE','FJ','FK','FO','FR','GB','GG','GI','GT','GY','HT','IL','IM','IT','JE','JO','KE','KI','KW','LI','LU','MD','ME','MU','MV','MZ','NA','NC','NL','NR','PA','PY','QA','RS','SA','SB','SC','SG','SH','SR','TL','UY']

def _load_region(code):
    __import__("region_%s" % code, globals(), locals(),
               fromlist=["PHONE_METADATA_%s" % code], level=1)

for region_code in _AVAILABLE_REGION_CODES:
    PhoneMetadata.register_short_region_loader(region_code, _load_region)

