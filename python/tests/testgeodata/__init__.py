# Copyright (C) 2011-2014 The Libphonenumber Authors
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

import atexit
import os
import shelve
from phonenumbers.util import u

_DIR, _ = os.path.split(__file__)
GEOCODE_LONGEST_PREFIX = 7
GEOCODE_DATA = shelve.open(os.path.join(_DIR, "geodata.db"), "r")
atexit.register(lambda: GEOCODE_DATA.close())
