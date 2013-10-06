"""Phone number to carrier mapping functionality

>>> import phonenumbers
>>> from phonenumbers.carrier import description_for_number
>>> ro_number = phonenumbers.parse("+40721234567", "RO")
>>> str(description_for_number(ro_number, "en"))
'Vodafone'
>>> str(description_for_number(ro_number, "fr"))  # fall back to English
'Vodafone'

"""
# Based very loosely on original Java code:
#     java/carrier/src/com/google/i18n/phonenumbers/PhoneNumberToCarrierMapper.java
#   Copyright (C) 2013 The Libphonenumber Authors
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

from .phonenumberutil import PhoneNumberType, number_type
from .prefix import prefix_description_for_number
try:
    from .carrierdata import CARRIER_DATA, CARRIER_LONGEST_PREFIX
except ImportError:  # pragma no cover
    # Before the generated code exists, the carrierdata/ directory is empty.
    # The generation process imports this module, creating a circular
    # dependency.  The hack below works around this.
    import os
    import sys
    if (os.path.basename(sys.argv[0]) == "buildmetadatafromxml.py" or
        os.path.basename(sys.argv[0]) == "buildprefixdata.py"):
        print >> sys.stderr, "Failed to import generated data (but OK as during autogeneration)"
        CARRIER_DATA = {'1': {'en': u('United States')}}
        CARRIER_LONGEST_PREFIX = 1
    else:
        raise


def description_for_valid_number(numobj, lang, script=None, region=None):
    """Return a text description of a PhoneNumber object for the given language.

    The description consists of the name of the carrier the number was
    originally allocated to, however if the country supports mobile number
    portability the number might not belong to the returned carrier
    anymore. If no mapping is found an empty string is returned.

    This method assumes the validity of the number passed in has already been
    checked, and that the number is suitable for carrier lookup. We consider
    mobile and pager numbers possible candidates for carrier lookup.

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
    return prefix_description_for_number(CARRIER_DATA, CARRIER_LONGEST_PREFIX,
                                         numobj, lang, script, region)


def description_for_number(numobj, lang, script=None, region=None):
    """Return a text description of a PhoneNumber object for the given language.

    The description consists of the name of the carrier the number was
    originally allocated to, however if the country supports mobile number
    portability the number might not belong to the returned carrier
    anymore. If no mapping is found an empty string is returned.

    This function explicitly checks the validity of the number passed in

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
    ntype = number_type(numobj)
    if _is_mobile(ntype):
        return description_for_valid_number(numobj, lang, script, region)
    return ""


def _is_mobile(ntype):
    """Checks if the supplied number type supports carrier lookup"""
    return (ntype == PhoneNumberType.MOBILE or
            ntype == PhoneNumberType.FIXED_LINE_OR_MOBILE or
            ntype == PhoneNumberType.PAGER)

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
