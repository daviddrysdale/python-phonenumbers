#!/usr/bin/env python
"""Script to read the libphonenumber XML metadata and generate Python code.

Invocation:
  buildmetadatafromxml.py infile.xml outdir module_prefix

Processes the given XML metadata file and emit generated Python code.
The output directory will be created if it does not exist, and
__init__.py and per-region data files will be created in the directory.
"""

# Based on original Java code and XML file:
#     resources/PhoneNumberMetadata.xml
#     java/resources/com/google/i18n/phonenumbers/BuildMetadataFromXml.java
# Copyright (C) 2010-2011 The Libphonenumber Authors
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
#
# This code was originally developed from the XML file, and the DTD within it.
# Subsequently, post-processing code was added to match the behaviour of
# BuildMetadataFromXml.java
#
# OPEN QUERIES/ISSUES
#  - The XML includes territory/areaCodeOptional? elements, which are
#    PhoneNumberDesc instances; these do not appear to be used in the
#    libphonenumber Java source code.

# import to allow this code to work with Python2.5
from __future__ import with_statement

import sys
import os
import re
import getopt
import datetime
from xml.etree import ElementTree as etree

# Use the local code in preference to any pre-installed version
sys.path.insert(0, '../../python')

# Pull in the data structure definitions
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata
from phonenumbers.phonemetadata import REGION_CODE_FOR_NON_GEO_ENTITY
from phonenumbers.util import UnicodeMixin, u, prnt

# Convention: variables beginning with 'x' are XML objects

# Top-level XML element containing data
TOP_XPATH = "territories"
# XML element name for the territory element
TERRITORY_TAG = "territory"
# Marker for unavailable entries
DATA_NA = "NA"

# Boilerplate text for generated Python files
METADATA_FILE_PROLOG = '"""Auto-generated file, do not edit by hand."""'
METADATA_FILE_IMPORT = "from %(module)s.phonemetadata import RegionCode, PhoneMetadata\n"
METADATA_FILE_LOOP = '''
def _load_region(code):
    __import__("region_%%s" %% code, globals(), locals(),
               fromlist=["PHONE_METADATA_%%s" %% code], level=1)

for region_code in _AVAILABLE_REGION_CODES:
    PhoneMetadata.register_%(prefix)sregion_loader(region_code, _load_region)
'''
METADATA_NONGEO_FILE_LOOP = '''
for country_code in _AVAILABLE_NONGEO_COUNTRY_CODES:
    PhoneMetadata.register_nongeo_region_loader(country_code, _load_region)
'''

_COUNTRY_CODE_TO_REGION_CODE_PROLOG = '''
# A mapping from a country code to the region codes which
# denote the country/region represented by that country code.
# In the case of multiple countries sharing a calling code,
# such as the NANPA countries, the one indicated with
# "main_country_for_code" in the metadata should be first.'''

# Boilerplate header for individual region data files
_REGION_METADATA_PROLOG = '''"""Auto-generated file, do not edit by hand. %(region)s metadata"""
from %(module)s.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata
'''

# Boilerplate header for individual country-code alternate number format data files
_ALT_FORMAT_METADATA_PROLOG = '''"""Auto-generated file, do not edit by hand. %s metadata"""
from %s.phonemetadata import NumberFormat
'''

# Copyright notice covering the XML metadata; include current year.
COPYRIGHT_NOTICE = """# Copyright (C) 2010-%s The Libphonenumber Authors
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
""" % datetime.datetime.now().year


# XML processing utility functions that are useful for the particular
# structure of the phone number metadata
def _get_unique_child(xtag, eltname):
    """Get the unique child element under xtag with name eltname"""
    try:
        results = xtag.findall(eltname)
        if len(results) > 1:
            raise Exception("Multiple elements found where 0/1 expected")
        elif len(results) == 1:
            return results[0]
        else:
            return None
    except Exception:
        return None


def _get_unique_child_value(xtag, eltname):
    """Get the text content of the unique child element under xtag with name eltname"""
    xelt = _get_unique_child(xtag, eltname)
    if xelt is None:
        return None
    else:
        return xelt.text


def get_true_attrib(xtag, aname):
    if aname in xtag.attrib:
        if xtag.attrib[aname] != 'true':
            raise Exception("Unexpected value %s for %s attribute" % (xtag.attrib[aname], aname))
        return True
    else:
        return False


def _dews_re(re_str):
    """Remove all whitespace in given regular expression string"""
    if re_str is None:
        return None
    else:
        return re.sub(r'\s', '', re_str)


def _expand_formatting_rule(rule, national_prefix):
    """Formatting rules can include terms "$NP" and "$FG",
    These get replaced with:
     "$NP" => the national prefix
     "$FG" => the first group, i.e. "$1"
    """
    if rule is None:
        return None
    if national_prefix is None:
        national_prefix = u("")
    rule = re.sub(u("\$NP"), national_prefix, rule)
    rule = re.sub(u("\$FG"), u("$1"), rule)
    return rule


class XAlternateNumberFormat(UnicodeMixin):
    """Parse alternate NumberFormat objects from XML element"""
    def __init__(self, xtag):
        if xtag is None:
            self.o = None
        else:
            self.o = NumberFormat()
            self.o._mutable = True
            self.o.pattern = xtag.attrib['pattern']  # REQUIRED attribute
            self.o.format = _get_unique_child_value(xtag, 'format')
            if self.o.format is None:
                raise Exception("No format pattern found")
            else:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                self.o.format = re.sub('\$', u(r'\\'), self.o.format)
            xleading_digits = xtag.findall("leadingDigits")
            for xleading_digit in xleading_digits:
                self.o.leading_digits_pattern.append(_dews_re(xleading_digit.text))
            # Currently this assumes no intlFormat elements in the element

    def __unicode__(self):
        return u(self.o)


class XNumberFormat(UnicodeMixin):
    """Parsed NumberFormat objects from XML element"""
    def __init__(self, owning_xterr, xtag, national_prefix,
                 national_prefix_formatting_rule,
                 national_prefix_optional_when_formatting,
                 carrier_code_formatting_rule):
        if xtag is None:
            self.o = None
            self.io = None
        else:
            self.o = NumberFormat()
            self.o._mutable = True
            # Find the REQUIRED attribute
            self.o.pattern = xtag.attrib['pattern']
            # Find the IMPLIED attribute(s)
            self.o.domestic_carrier_code_formatting_rule = xtag.get('carrierCodeFormattingRule', None)
            self.o.national_prefix_formatting_rule = xtag.get('nationalPrefixFormattingRule', None)
            self.o.national_prefix_optional_when_formatting = get_true_attrib(xtag, 'nationalPrefixOptionalWhenFormatting')

            # Post-process formatting rules for expansions and defaults
            if self.o.national_prefix_formatting_rule is not None:
                # expand abbreviations
                self.o.national_prefix_formatting_rule = _expand_formatting_rule(self.o.national_prefix_formatting_rule,
                                                                                   national_prefix)
            else:
                # set to territory-wide formatting rule
                self.o.national_prefix_formatting_rule = national_prefix_formatting_rule
            if self.o.national_prefix_formatting_rule is not None:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                self.o.national_prefix_formatting_rule = re.sub('\$', r'\\', self.o.national_prefix_formatting_rule)

            if not self.o.national_prefix_optional_when_formatting:
                # If attrib is False, it was missing and inherits territory-wide value
                self.o.national_prefix_optional_when_formatting = national_prefix_optional_when_formatting

            if self.o.domestic_carrier_code_formatting_rule is not None:
                # expand abbreviations
                self.o.domestic_carrier_code_formatting_rule = _expand_formatting_rule(self.o.domestic_carrier_code_formatting_rule,
                                                                                         national_prefix)
            else:
                # set to territory-wide formatting rule
                self.o.domestic_carrier_code_formatting_rule = carrier_code_formatting_rule
            if self.o.domestic_carrier_code_formatting_rule is not None:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                self.o.domestic_carrier_code_formatting_rule = re.sub('\$(\d)', r'\\\1', self.o.domestic_carrier_code_formatting_rule)

            self.o.format = _get_unique_child_value(xtag, 'format')
            if self.o.format is None:
                raise Exception("No format pattern found")
            else:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                self.o.format = re.sub('\$', u(r'\\'), self.o.format)
            xleading_digits = xtag.findall("leadingDigits")
            for xleading_digit in xleading_digits:
                self.o.leading_digits_pattern.append(_dews_re(xleading_digit.text))

            # Add this NumberFormat object into the owning metadata
            owning_xterr.o.number_format.append(self.o)

            # Extract the pattern for international format; if not present, use the national format.
            # If the intlFormat is set to "NA" the intlFormat should be ignored.
            self.io = NumberFormat(pattern=self.o.pattern,
                                   leading_digits_pattern=self.o.leading_digits_pattern)
            self.io._mutable = True

            intl_format = _get_unique_child_value(xtag, "intlFormat")
            if intl_format is None:
                # Default to use the same as the national pattern if none is defined.
                self.io.format = self.o.format
            else:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                intl_format = re.sub('\$', u(r'\\'), intl_format)
                if intl_format != DATA_NA:
                    self.io.format = intl_format
                owning_xterr.has_explicit_intl_format = True
            if self.io.format is not None:
                # Add this international NumberFormat object into the owning metadata
                owning_xterr.o.intl_number_format.append(self.io)

    def __unicode__(self):
        return u(self.o)


class XPhoneNumberDesc(UnicodeMixin):
    """Parse PhoneNumberDesc object from XML element"""
    def __init__(self, xtag, template=None, fill_na=True):
        self.o = PhoneNumberDesc()
        self.o._mutable = True
        self.o.national_number_pattern = None
        self.o.possible_number_pattern = None
        self.o.example_number = None
        if xtag is None:
            if fill_na:
                self.o.national_number_pattern = DATA_NA
                self.o.possible_number_pattern = DATA_NA
                return
        # Start with the template values
        if template is not None:
            self.o.national_number_pattern = template.national_number_pattern
            self.o.possible_number_pattern = template.possible_number_pattern
            self.o.example_number = template.example_number
        # Overwrite with any values in the XML
        if xtag is not None:
            national_number_pattern = _dews_re(_get_unique_child_value(xtag, 'nationalNumberPattern'))
            if national_number_pattern is not None:
                self.o.national_number_pattern = national_number_pattern
            possible_number_pattern = _dews_re(_get_unique_child_value(xtag, 'possibleNumberPattern'))
            if possible_number_pattern is not None:
                self.o.possible_number_pattern = possible_number_pattern
            example_number = _get_unique_child_value(xtag, 'exampleNumber')
            if example_number is not None:
                self.o.example_number = example_number

    def __unicode__(self):
        return u(self.o)


class XAlternateTerritory(UnicodeMixin):
    """Parse alternate format metadata from XML element (territory)"""
    def __init__(self, xterritory):
        self.country_code = int(xterritory.attrib['countryCode'])
        # Look for available formats
        self.number_format = []
        formats = _get_unique_child(xterritory, "availableFormats")
        if formats is not None:
            for xelt in formats.findall("numberFormat"):
                # Create an XNumberFormat object, which contains a NumberFormat object
                # or two, and which self-registers them with self.o
                self.number_format.append(XAlternateNumberFormat(xelt).o)
        if len(self.number_format) == 0:
            raise Exception("No number formats found in available formats")
        # Currently this assumes no intlFormat elements in the file

    def __unicode__(self):
        return u(self.number_format)


class XTerritory(UnicodeMixin):
    """Parse PhoneMetadata from XML element (territory)"""
    def __init__(self, xterritory, short_data):
        # Retrieve the REQUIRED attributes
        id = xterritory.attrib['id']
        self.o = PhoneMetadata(id, short_data=short_data, register=False)
        self.o._mutable = True
        if 'countryCode' in xterritory.attrib:
            self.o.country_code = int(xterritory.attrib['countryCode'])
        else:
            self.o.country_code = None
        # Retrieve the IMPLIED attributes
        self.o.international_prefix = xterritory.get('internationalPrefix', None)
        self.o.leading_digits = xterritory.get('leadingDigits', None)
        self.o.preferred_international_prefix = xterritory.get('preferredInternationalPrefix', None)
        self.o.national_prefix = xterritory.get('nationalPrefix', None)
        self.o.national_prefix_for_parsing = _dews_re(xterritory.get('nationalPrefixForParsing', None))
        self.o.national_prefix_transform_rule = xterritory.get('nationalPrefixTransformRule', None)
        if self.o.national_prefix_transform_rule is not None:
            # Replace '$1' etc  with '\1' to match Python regexp group reference format
            self.o.national_prefix_transform_rule = re.sub('\$', r'\\', self.o.national_prefix_transform_rule)
        self.o.preferred_extn_prefix = xterritory.get('preferredExtnPrefix', None)
        national_prefix_formatting_rule = xterritory.get('nationalPrefixFormattingRule', None)
        national_prefix_optional_when_formatting = get_true_attrib(xterritory, 'nationalPrefixOptionalWhenFormatting')
        carrier_code_formatting_rule = xterritory.get('carrierCodeFormattingRule', None)

        # Post-processing for the territory-default formatting rules.  These are used
        # in NumberFormat elements that don't supply their own formatting rules.
        if self.o.national_prefix is not None:
            if self.o.national_prefix_for_parsing is None:
                # Default to self.national_prefix when national_prefix_for_parsing not set
                self.o.national_prefix_for_parsing = self.o.national_prefix
        national_prefix_formatting_rule = _expand_formatting_rule(national_prefix_formatting_rule,
                                                                  self.o.national_prefix)
        carrier_code_formatting_rule = _expand_formatting_rule(carrier_code_formatting_rule,
                                                               self.o.national_prefix)
        self.o.main_country_for_code = get_true_attrib(xterritory, 'mainCountryForCode')
        self.o.leading_zero_possible = get_true_attrib(xterritory, 'leadingZeroPossible')
        self.o.mobile_number_portable_region = get_true_attrib(xterritory, 'mobileNumberPortableRegion')

        # Retrieve the various PhoneNumberDesc elements.  The general_desc is
        # first and most important; it will be used to fill out missing fields in
        # many of the other PhoneNumberDesc elements.
        self.o.general_desc = XPhoneNumberDesc(_get_unique_child(xterritory, 'generalDesc'),
                                               fill_na=False)
        # areaCodeOptional is in the XML but not used in the code.
        self.o.area_code_optional = XPhoneNumberDesc(_get_unique_child(xterritory, 'areaCodeOptional'),
                                                     template=self.o.general_desc.o)
        if not short_data:
            self.o.fixed_line = XPhoneNumberDesc(_get_unique_child(xterritory, 'fixedLine'),
                                                 template=self.o.general_desc.o, fill_na=False)
            self.o.mobile = XPhoneNumberDesc(_get_unique_child(xterritory, 'mobile'),
                                             template=self.o.general_desc.o, fill_na=False)
            self.o.pager = XPhoneNumberDesc(_get_unique_child(xterritory, 'pager'),
                                            template=self.o.general_desc.o)
            self.o.shared_cost = XPhoneNumberDesc(_get_unique_child(xterritory, 'sharedCost'),
                                                  template=self.o.general_desc.o)
            self.o.personal_number = XPhoneNumberDesc(_get_unique_child(xterritory, 'personalNumber'),
                                                      template=self.o.general_desc.o)
            self.o.voip = XPhoneNumberDesc(_get_unique_child(xterritory, 'voip'),
                                           template=self.o.general_desc.o)
            self.o.uan = XPhoneNumberDesc(_get_unique_child(xterritory, 'uan'),
                                          template=self.o.general_desc.o)
            self.o.voicemail = XPhoneNumberDesc(_get_unique_child(xterritory, 'voicemail'),
                                                template=self.o.general_desc.o)
            self.o.no_international_dialling = XPhoneNumberDesc(_get_unique_child(xterritory, 'noInternationalDialling'),
                                                                template=self.o.general_desc.o)
        else:
            self.o.standard_rate = XPhoneNumberDesc(_get_unique_child(xterritory, 'standardRate'),
                                                    template=self.o.general_desc.o)
            self.o.short_code = XPhoneNumberDesc(_get_unique_child(xterritory, 'shortCode'),
                                                 template=self.o.general_desc.o)
            self.o.carrier_specific = XPhoneNumberDesc(_get_unique_child(xterritory, 'carrierSpecific'),
                                                       template=self.o.general_desc.o)
            self.o.emergency = XPhoneNumberDesc(_get_unique_child(xterritory, 'emergency'),
                                                template=self.o.general_desc.o)
        self.o.toll_free = XPhoneNumberDesc(_get_unique_child(xterritory, 'tollFree'),
                                            template=self.o.general_desc.o)
        self.o.premium_rate = XPhoneNumberDesc(_get_unique_child(xterritory, 'premiumRate'),
                                               template=self.o.general_desc.o)
        # Look for available formats
        self.has_explicit_intl_format = False
        formats = _get_unique_child(xterritory, "availableFormats")
        if formats is not None:
            for xelt in formats.findall("numberFormat"):
                # Create an XNumberFormat object, which contains a NumberFormat object
                # or two, and which self-registers them with self.o
                XNumberFormat(self,
                              xelt,
                              self.o.national_prefix,
                              national_prefix_formatting_rule,
                              national_prefix_optional_when_formatting,
                              carrier_code_formatting_rule)
            if len(self.o.number_format) == 0:
                raise Exception("No number formats found in available formats")
        if not self.has_explicit_intl_format:
            # Only a small number of regions need to specify the intlFormats
            # in the XML.  For the majority of countries the intlNumberFormat
            # metadata is an exact copy of the national NumberFormat metadata.
            # To minimize the size of the metadata file, we only keep
            # intlNumberFormats that actually differ in some way to the
            # national formats.
            self.o.intl_number_format = []

    def identifier(self):
        if self.o.id == REGION_CODE_FOR_NON_GEO_ENTITY:
            # For non-geographical country calling codes (e.g. +800), use the
            # country calling codes instead of the region code to form the
            # file name.
            return str(self.o.country_code)
        else:
            return self.o.id

    def __unicode__(self):
        return u(self.o)


class XPhoneNumberMetadata(UnicodeMixin):
    """Entire collection of phone number metadata retrieved from XML"""
    def __init__(self, filename, short_data):
        # Load the XML data from the given filename
        with open(filename, "r") as infile:
            xtree = etree.parse(infile)
        # Move to the top-level element of interest
        xterritories = xtree.find(TOP_XPATH)
        # Iterate over the child elements, as there isn't any complex nesting or
        # tree structures in the XML DTD.
        self.territory = {}
        for xterritory in xterritories:
            if xterritory.tag == TERRITORY_TAG:
                terrobj = XTerritory(xterritory, short_data)
                id = terrobj.identifier()  # like "US" for countries, "800" for non-geo
                if id in self.territory:
                    raise Exception("Duplicate entry for %s" % id)
                self.territory[id] = terrobj
            else:
                raise Exception("Unexpected element %s found" % xterritory.tag)
        self.alt_territory = None
        self.short_data = short_data

    def add_alternate_formats(self, filename):
        """Add phone number alternate format metadata retrieved from XML"""
        with open(filename, "r") as infile:
            xtree = etree.parse(infile)
        self.alt_territory = {}  # country_code to XAlternateTerritory
        xterritories = xtree.find(TOP_XPATH)
        for xterritory in xterritories:
            if xterritory.tag == TERRITORY_TAG:
                terrobj = XAlternateTerritory(xterritory)
                id = str(terrobj.country_code)
                if id in self.alt_territory:
                    raise Exception("Duplicate entry for %s" % id)
                self.alt_territory[id] = terrobj
            else:
                raise Exception("Unexpected element %s found" % xterritory.tag)

    def __unicode__(self):
        return u("\n").join([u("%s: %s") % (country_id, territory) for country_id, territory in self.territory.items()])

    def emit_metadata_for_region_py(self, region, region_filename, module_prefix):
        """Emit Python code generating the metadata for the given region"""
        terrobj = self.territory[region]
        with open(region_filename, "w") as outfile:
            prnt(_REGION_METADATA_PROLOG % {'region': terrobj.identifier(), 'module': module_prefix}, file=outfile)
            prnt("PHONE_METADATA_%s = %s" % (terrobj.identifier(), terrobj), file=outfile)

    def emit_alt_formats_for_cc_py(self, cc, cc_filename, module_prefix):
        """Emit Python code generating the alternate format metadata for the given country code"""
        terrobj = self.alt_territory[cc]
        with open(cc_filename, "w") as outfile:
            prnt(_ALT_FORMAT_METADATA_PROLOG % (cc, module_prefix), file=outfile)
            prnt("PHONE_ALT_FORMAT_%s = %s" % (cc, terrobj), file=outfile)

    def emit_metadata_py(self, datadir, module_prefix):
        """Emit Python code for the phone number metadata to the given file, and
        to a data/ subdirectory in the same directory as that file."""

        if not os.path.isdir(datadir):
            os.mkdir(datadir)
        modulefilename = os.path.join(datadir, '__init__.py')

        # First, generate all of the individual per-region files in that directory
        for country_id in sorted(self.territory.keys()):
            filename = os.path.join(datadir, "region_%s.py" % country_id)
            self.emit_metadata_for_region_py(country_id, filename, module_prefix)

        # Same for any per-country-code alternate format files
        if self.alt_territory is not None:
            for country_code in sorted(self.alt_territory.keys()):
                filename = os.path.join(datadir, "alt_format_%s.py" % country_code)
                self.emit_alt_formats_for_cc_py(country_code, filename, module_prefix)

        # Now build a module file that includes them all
        with open(modulefilename, "w") as outfile:
            prnt(METADATA_FILE_PROLOG, file=outfile)
            prnt(COPYRIGHT_NOTICE, file=outfile)
            prnt(METADATA_FILE_IMPORT % {'module': module_prefix}, file=outfile)
            nongeo_codes = []
            country_codes = []
            for country_id in sorted(self.territory.keys()):
                terrobj = self.territory[country_id]
                if terrobj.o.id == REGION_CODE_FOR_NON_GEO_ENTITY:
                    nongeo_codes.append(country_id)  # int
                else:
                    country_codes.append("'%s'" % country_id)  # quoted string
            prnt("_AVAILABLE_REGION_CODES = tuple(map(RegionCode, (%s)))" % ",".join(country_codes), file=outfile)
            if len(nongeo_codes) > 0:
                prnt("_AVAILABLE_NONGEO_COUNTRY_CODES = (%s)" % ", ".join(nongeo_codes), file=outfile)
            register_prefix = "short_" if self.short_data else ""
            prnt(METADATA_FILE_LOOP % {'prefix': register_prefix}, file=outfile)
            if len(nongeo_codes) > 0:
                prnt(METADATA_NONGEO_FILE_LOOP, file=outfile)

            if self.alt_territory is not None:
                for country_code in sorted(self.alt_territory.keys()):
                    prnt("from .alt_format_%s import PHONE_ALT_FORMAT_%s" % (country_code, country_code), file=outfile)
                prnt("_ALT_NUMBER_FORMATS = {%s}" %
                     ", ".join(["%s: PHONE_ALT_FORMAT_%s" % (cc, cc) for cc in sorted(self.alt_territory.keys())]),
                     file=outfile)

            # Build up a map from country code (int) to list of region codes (ISO 3166-1 alpha 2)
            country_code_to_region_code = {}
            for country_id in sorted(self.territory.keys()):
                terrobj = self.territory[country_id]
                if terrobj.o.country_code is not None:
                    country_code = int(terrobj.o.country_code)
                    if country_code not in country_code_to_region_code:
                        country_code_to_region_code[country_code] = []
                    if terrobj.o.main_country_for_code:
                        country_code_to_region_code[country_code].insert(0, terrobj.o.id)
                    else:
                        country_code_to_region_code[country_code].append(terrobj.o.id)

            # Emit the mapping from country code to region code if nonempty.
            if len(country_code_to_region_code.keys()) > 0:
                prnt(_COUNTRY_CODE_TO_REGION_CODE_PROLOG, file=outfile)
                prnt("_COUNTRY_CODE_TO_REGION_CODE = dict((k, tuple(map(RegionCode, v))) for (k, v) in (", file=outfile)
                for country_code in sorted(country_code_to_region_code.keys()):
                    country_ids = country_code_to_region_code[country_code]
                    prnt('    (%d, ("%s",)),' % (country_code, '", "'.join(country_ids)), file=outfile)
                prnt("))", file=outfile)


def _standalone(argv):
    """Parse the given XML file and emit generated code."""
    alternate = None
    short_data = False
    try:
        opts, args = getopt.getopt(argv, "hsa:", ("help", "short", "alt="))
    except getopt.GetoptError:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)
        elif opt in ("-s", "--short"):
            short_data = True
        elif opt in ("-a", "--alt"):
            alternate = arg
        else:
            prnt("Unknown option %s" % opt, file=sys.stderr)
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)

    if len(args) != 3:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    pmd = XPhoneNumberMetadata(args[0], short_data)
    if alternate is not None:
        pmd.add_alternate_formats(alternate)
    pmd.emit_metadata_py(args[1], args[2])


if __name__ == "__main__":
    _standalone(sys.argv[1:])
