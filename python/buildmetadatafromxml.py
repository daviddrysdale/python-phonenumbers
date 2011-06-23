#!/usr/bin/env python
"""Script to read the libphonenumber XML metadata and generate Python code.

Invocation:
  buildmetadatafromxml.py infile.xml outdir

Processes the given XML metadata file and emit generated Python code.
The output directory will be created if it does not exist, and
__init__.py and per-region data files will be created in the directory.
"""

# Based on original Java code and XML file:
#     resources/PhoneNumberMetadata.xml
#     java/resources/com/google/i18n/phonenumbers/BuildMetadataFromXml.java
#   Copyright (C) 2010-2011 Google Inc.
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
#  - The XML includes territory/areaCodeOptional? and territory/shortCode?
#    elements, which are PhoneNumberDesc instances; these do not
#    appear to be used in the libphonenumber Java source code.

import sys
import os
import re
import datetime

from lxml import etree  # From http://lxml.de/, run 'easy_install lxml'

# Pull in the data structure definitions
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

# Convention: variables beginning with 'x' are XML objects

# Top-level XML element containing data
TOP_XPATH = "/phoneNumberMetadata/territories"
# XML element name for the territory element
TERRITORY_TAG = "territory"

# Boilerplate text for generated Python files
METADATA_FILE_PROLOG = '"""Auto-generated file, do not edit by hand."""'
_COUNTRY_CODE_TO_REGION_CODE_PROLOG = '''
# A mapping from a country code to the region codes which
# denote the country/region represented by that country code.
# In the case of multiple countries sharing a calling code,
# such as the NANPA countries, the one indicated with
# "main_country_for_code" in the metadata should be first.'''

# Boilerplate header for individual region data files
_REGION_METADATA_PROLOG = '''"""Auto-generated file, do not edit by hand. %s metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata
'''

# Copyright notice covering the XML metadata; include current year.
COPYRIGHT_NOTICE = """# Copyright (C) 2010-%s Google Inc.
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
        results = xtag.xpath(eltname)
        if len(results) > 1:
            raise Exception("Multiple elements found where 0/1 expected")
        elif len(results) == 1:
            return xtag.xpath(eltname)[0]
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
        national_prefix = u""
    rule = re.sub(u'\$NP', national_prefix, rule)
    rule = re.sub(u'\$FG', u'$1', rule)
    return rule


class XNumberFormat(object):
    """Parsed NumberFormat objects from XML element"""
    def __init__(self, owning_xterr, xtag, national_prefix, national_prefix_formatting_rule, carrier_code_formatting_rule):
        if xtag is None:
            self.o = None
            self.io = None
        else:
            self.o = NumberFormat()
            # Find the REQUIRED attribute
            self.o.pattern = xtag.attrib['pattern']
            # Find the IMPLIED attribute(s)
            self.o.domestic_carrier_code_formatting_rule = xtag.get('carrierCodeFormattingRule', None)
            self.o.national_prefix_formatting_rule = xtag.get('nationalPrefixFormattingRule', None)

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
                self.o.format = re.sub('\$', ur'\\', self.o.format)
            xleading_digits = xtag.xpath("leadingDigits")
            for xleading_digit in xleading_digits:
                self.o.leading_digits_pattern.append(_dews_re(xleading_digit.text))

            # Add this NumberFormat object into the owning metadata
            owning_xterr.o.number_format.append(self.o)

            # Extract the pattern for international format; if not present, use the national format.
            # If the intlFormat is set to "NA" the intlFormat should be ignored.
            self.io = NumberFormat(pattern=self.o.pattern,
                                   leading_digits_pattern=self.o.leading_digits_pattern)

            intl_format = _get_unique_child_value(xtag, "intlFormat")
            if intl_format is None:
                # Default to use the same as the national pattern if none is defined.
                self.io.format = self.o.format
            else:
                # Replace '$1' etc  with '\1' to match Python regexp group reference format
                intl_format = re.sub('\$', ur'\\', intl_format)
                if intl_format != "NA":
                    self.io.format = intl_format
                owning_xterr.has_explicit_intl_format = True
            if self.io.format is not None:
                # Add this international NumberFormat object into the owning metadata
                owning_xterr.o.intl_number_format.append(self.io)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return unicode(self.o)


class XPhoneNumberDesc(object):
    """Parse PhoneNumberDesc object from XML element"""
    def __init__(self, xtag,
                 template=None, fill_na=True):
        self.o = PhoneNumberDesc()
        self.o.national_number_pattern = None
        self.o.possible_number_pattern = None
        self.o.example_number = None
        if xtag is None:
            if fill_na:
                self.o.national_number_pattern = "NA"
                self.o.possible_number_pattern = "NA"
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

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return unicode(self.o)


class XTerritory(object):
    """Parse PhoneMetadata from XML element (territory)"""
    def __init__(self, xterritory):
        # Retrieve the REQUIRED attributes
        id = xterritory.attrib['id']
        self.o = PhoneMetadata(id, register=False)
        self.o.country_code = int(xterritory.attrib['countryCode'])
        self.o.international_prefix = xterritory.attrib['internationalPrefix']
        # Retrieve the IMPLIED attributes
        self.o.leading_digits = xterritory.get('leadingDigits', None)
        self.o.preferred_international_prefix = xterritory.get('preferredInternationalPrefix', None)
        self.o.national_prefix = xterritory.get('nationalPrefix', None)
        self.o.national_prefix_for_parsing = xterritory.get('nationalPrefixForParsing', None)
        self.o.national_prefix_transform_rule = xterritory.get('nationalPrefixTransformRule', None)
        if self.o.national_prefix_transform_rule is not None:
            # Replace '$1' etc  with '\1' to match Python regexp group reference format
            self.o.national_prefix_transform_rule = re.sub('\$', r'\\', self.o.national_prefix_transform_rule)
        self.o.preferred_extn_prefix = xterritory.get('preferredExtnPrefix', None)
        national_prefix_formatting_rule = xterritory.get('nationalPrefixFormattingRule', None)
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

        if 'mainCountryForCode' in xterritory.attrib:
            if xterritory.attrib['mainCountryForCode'] != 'true':
                raise Exception("Unexpected value for mainCountryForCode attribute")
            self.o.main_country_for_code = True
        else:
            self.o.main_country_for_code = False
        if 'leadingZeroPossible' in xterritory.attrib:
            if xterritory.attrib['leadingZeroPossible'] != 'true':
                raise Exception("Unexpected value for leadingZeroPossible attribute")
            self.o.leading_zero_possible = True
        else:
            self.o.leading_zero_possible = False
        # Retrieve the various PhoneNumberDesc elements.  The general_desc is
        # first and most important; it will be used to fill out missing fields in
        # many of the other PhoneNumberDesc elements.
        self.o.general_desc = XPhoneNumberDesc(_get_unique_child(xterritory, 'generalDesc'),
                                               fill_na=False)
        self.o.no_international_dialling = XPhoneNumberDesc(_get_unique_child(xterritory, 'noInternationalDialling'),
                                                            template=self.o.general_desc.o)
        self.o.area_code_optional = XPhoneNumberDesc(_get_unique_child(xterritory, 'areaCodeOptional'),
                                                     template=self.o.general_desc.o)
        self.o.fixed_line = XPhoneNumberDesc(_get_unique_child(xterritory, 'fixedLine'),
                                             template=self.o.general_desc.o, fill_na=False)
        self.o.mobile = XPhoneNumberDesc(_get_unique_child(xterritory, 'mobile'),
                                         template=self.o.general_desc.o, fill_na=False)
        self.o.pager = XPhoneNumberDesc(_get_unique_child(xterritory, 'pager'),
                                        template=self.o.general_desc.o)
        self.o.toll_free = XPhoneNumberDesc(_get_unique_child(xterritory, 'tollFree'),
                                            template=self.o.general_desc.o)
        self.o.premium_rate = XPhoneNumberDesc(_get_unique_child(xterritory, 'premiumRate'),
                                               template=self.o.general_desc.o)
        self.o.shared_cost = XPhoneNumberDesc(_get_unique_child(xterritory, 'sharedCost'),
                                              template=self.o.general_desc.o)
        self.o.personal_number = XPhoneNumberDesc(_get_unique_child(xterritory, 'personalNumber'),
                                                  template=self.o.general_desc.o)
        self.o.voip = XPhoneNumberDesc(_get_unique_child(xterritory, 'voip'),
                                       template=self.o.general_desc.o)
        self.o.uan = XPhoneNumberDesc(_get_unique_child(xterritory, 'uan'),
                                      template=self.o.general_desc.o)
        self.o.short_code = XPhoneNumberDesc(_get_unique_child(xterritory, 'shortCode'),
                                             template=self.o.general_desc.o)
        # Look for available formats
        self.has_explicit_intl_format = False
        formats = _get_unique_child(xterritory, "availableFormats")
        if formats is not None:
            for xelt in formats.xpath("numberFormat"):
                # Create an XNumberFormat object, which contains a NumberFormat object
                # or two, and which self-registers them with self.o
                XNumberFormat(self,
                              xelt,
                              self.o.national_prefix,
                              national_prefix_formatting_rule,
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

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return unicode(self.o)


class XPhoneNumberMetadata(object):
    """Entire collection of phone number metadata retrieved from XML"""
    def __init__(self, filename):
        # Load the XML data from the given filename
        with file(filename) as infile:
            xtree = etree.parse(infile)
        # Move to the top-level element of interest
        xterritories = xtree.xpath(TOP_XPATH)[0]
        # Iterate over the child elements, as there isn't any complex nesting or
        # tree structures in the XML DTD.
        self.territory = {}
        for xterritory in xterritories.iterchildren(tag=etree.Element):
            if xterritory.tag == TERRITORY_TAG:
                terrobj = XTerritory(xterritory)
                if terrobj.o.id in self.territory:
                    raise Exception("Duplicate entry for %s" % terrobj.o.id)
                self.territory[terrobj.o.id] = terrobj
            else:
                raise Exception("Unexpected element %s found" % xterritory.tag)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u'\n'.join([u"%s: %s" % (country_id, territory) for country_id, territory in self.territory.items()])

    def emit_metadata_for_region_py(self, region, region_filename):
        """Emit Python code generating the metadata for the given region"""
        terrobj = self.territory[region]
        with open(region_filename, "w") as outfile:
            print >> outfile, _REGION_METADATA_PROLOG % terrobj.o.id
            print >> outfile, "PHONE_METADATA_%s = %s" % (terrobj.o.id, terrobj)

    def emit_metadata_py(self, datadir):
        """Emit Python code for the phone number metadata to the given file, and
        to a data/ subdirectory in the same directory as that file."""

        if not os.path.isdir(datadir):
            os.mkdir(datadir)
        modulefilename = os.path.join(datadir, '__init__.py')

        # First, generate all of the individual per-region files in that directory
        for country_id in sorted(self.territory.keys()):
            filename = os.path.join(datadir, "region_%s.py" % country_id)
            self.emit_metadata_for_region_py(country_id, filename)

        # Now build a module file that includes them all
        with open(modulefilename, "w") as outfile:
            print >> outfile, METADATA_FILE_PROLOG
            print >> outfile, COPYRIGHT_NOTICE
            for country_id in sorted(self.territory.keys()):
                print >> outfile, "from region_%s import PHONE_METADATA_%s" % (country_id, country_id)
            # Emit the mapping from country code to region code
            print >> outfile, _COUNTRY_CODE_TO_REGION_CODE_PROLOG
            print >> outfile, "_COUNTRY_CODE_TO_REGION_CODE = {"
            # Build up the map
            country_code_to_region_code = {}
            for country_id in sorted(self.territory.keys()):
                terrobj = self.territory[country_id]
                country_code = int(terrobj.o.country_code)
                if country_code not in country_code_to_region_code:
                    country_code_to_region_code[country_code] = []
                if terrobj.o.main_country_for_code:
                    country_code_to_region_code[country_code].insert(0, country_id)
                else:
                    country_code_to_region_code[country_code].append(country_id)

            for country_code in sorted(country_code_to_region_code.keys()):
                country_ids = country_code_to_region_code[country_code]
                print >> outfile, '    %d: ("%s",),' % (country_code, '", "'.join(country_ids))
            print >> outfile, "}"


def _standalone(argv):
    """Parse the given XML file and emit generated code."""
    if len(sys.argv) != 3:
        print >> sys.stderr, __doc__
        sys.exit(1)
    pmd = XPhoneNumberMetadata(sys.argv[1])
    pmd.emit_metadata_py(sys.argv[2])


if __name__ == "__main__":
    _standalone(sys.argv[1:])
