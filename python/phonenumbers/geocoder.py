"""Phone number geocoding functionality

>>> import phonenumbers
>>> from phonenumbers.geocoder import area_description_for_number
>>> gb_number = phonenumbers.parse("+442083612345", "GB")
>>> de_number = phonenumbers.parse("0891234567", "DE")
>>> ch_number = phonenumbers.parse("0431234567", "CH")
>>> print repr(area_description_for_number(gb_number, "en"))
u'London'
>>> print repr(area_description_for_number(gb_number, "fr"))
u''
>>> print repr(area_description_for_number(gb_number, "en", region="GB"))
u'London'
>>> print repr(area_description_for_number(gb_number, "en", region="US"))
u'London'
>>> print repr(area_description_for_number(de_number, "en"))
u'Munich'
>>> print repr(area_description_for_number(de_number, "de"))
u'M\\xfcnchen'
>>> print repr(area_description_for_number(ch_number, "de"))
u'Z\\xfcrich'
>>> print repr(area_description_for_number(ch_number, "en"))
u'Zurich'
>>> print repr(area_description_for_number(ch_number, "fr"))
u'Zurich'
>>> print repr(area_description_for_number(ch_number, "it"))
u'Zurigo'

"""
# Based very loosely on original Java code:
#     java/src/com/google/i18n/phonenumbers/geocoding/PhoneNumberOfflineGeocoder.java
#   Copyright (C) 2009-2011 The Libphonenumber Authors
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

from phonenumbers import format_number, PhoneNumberFormat, is_valid_number
from phonenumbers import region_code_for_number
from geodata import GEOCODE_DATA, GEOCODE_LONGEST_PREFIX
from geodata.locale import LOCALE_DATA


def _may_fall_back_to_english(lang):
    # Don't fall back to English if the requested language is among the following:
    # - Chinese
    # - Japanese
    # - Korean
    return lang != "zh" and lang != "ja" and lang != "ko"


def _find_lang(langdict, lang, script, region):
    """Return the entry in the dictionary for the given language information."""
    # First look for lang, script as a combination
    lang_script = "%s_%s" % (lang, script)
    if lang_script in langdict:
        return langdict[lang_script]
    # Next look for lang, region as a combination
    lang_region = "%s_%s" % (lang, region)
    if lang_region in langdict:
        return langdict[lang_region]
    # Fall back to bare language code lookup
    if lang in langdict:
        return langdict[lang]
    # Possibly fall back to english
    if _may_fall_back_to_english(lang):
        return langdict.get("en", None)
    else:
        return None


def area_description_for_number(numobj, lang, script=None, region=None):
    """Return a text description of the area of a PhoneNumber for the given language.

    Arguments:
    numobj -- The PhoneNumber object for which we want to get a text description.
    lang -- A 2-letter lowercase ISO 639-1 language code for the language in
                  which the description should be returned (e.g. "en")
    script -- A 4-letter titlecase (first letter uppercase, rest lowercase)
                  ISO script code as defined in ISO 15924, separated by an
                  underscore (e.g. "Hant")
    region --  A 2-letter uppercase ISO 3166-1 country code (e.g. "GB")

    Returns a text description in the given language code, for the given phone
    number's area, or an empty string if no description is available."""
    e164_num = format_number(numobj, PhoneNumberFormat.E164)
    if not e164_num.startswith('+'):  # pragma no cover
        raise Exception("Expect E164 number to start with +")
    for prefix_len in xrange(GEOCODE_LONGEST_PREFIX, 0, -1):
        prefix = e164_num[1:(1 + prefix_len)]
        if prefix in GEOCODE_DATA:
            # This prefix is present in the geocoding data, as a dictionary
            # mapping language info to location name.
            name = _find_lang(GEOCODE_DATA[prefix], lang, script, region)
            if name is not None:
                return name
            else:
                return u""
    return u""


def country_name_for_number(numobj, lang, script=None, region=None):
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
    number_region = region_code_for_number(numobj)
    if number_region in LOCALE_DATA:
        # The Locale data has a set of names for this region, in various languages.
        name = LOCALE_DATA[number_region].get(lang, "")
        if name.startswith('*'):
            # If the location name is "*<other_lang>", this indicates that the
            # name is held elsewhere, specifically in the [other_lang] entry
            other_lang = name[1:]
            name = LOCALE_DATA[number_region].get(other_lang, "")
        return name
    return u""


def description_for_valid_number(numobj, lang, script=None, region=None):
    """Return a text description of a PhoneNumber object for the given language.

    The description might consist of the name of the country where the phone
    number is from and/or the name of the geographical area the phone number
    is from.  This function assumes the validity of the number passed in has
    already been checked.

    Arguments:
    numobj -- A valid PhoneNumber object for which we want to get a text
                  description.
    lang -- A 2-letter lowercase ISO 639-1 language code for the language in
                  which the description should be returned (e.g. "en")
    script -- A 4-letter titlecase (first letter uppercase, rest lowercase)
                  ISO script code as defined in ISO 15924, separated by an
                  underscore (e.g. "Hant")
    region --  A 2-letter uppercase ISO 3166-1 country code (e.g. "GB")

    Returns a text description in the given language code, for the given phone
    number, or an empty string if no description is available."""
    area_description = area_description_for_number(numobj, lang, script, region)
    if area_description != "":
        return area_description
    else:
        # Fall back to the description of the number's region
        return country_name_for_number(numobj, lang, script, region)


def description_for_number(numobj, lang, script=None, region=None):
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
    if not is_valid_number(numobj):
        return ""
    return description_for_valid_number(numobj, lang, script, region)

if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
