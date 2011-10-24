#!/usr/bin/env python
"""Script to read the libphonenumber geocoding metadata and generate Python code.

Invocation:
  buildgeocodingdata.py indir outfile

Processes all of the geocoding data under the given input directory and emit
generated Python code.
"""

# Based on original geocoding data files from libphonenumber:
#     resources/geocoding/*/*.txt
# Copyright (C) 2011 The Libphonenumber Authors
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
import os
import sys
import glob
import re
import datetime

GEODATA_SUFFIX = ".txt"
BLANK_LINE_RE = re.compile(ur'^\s*$', re.UNICODE)
COMMENT_LINE_RE = re.compile(ur'^\s*#.*$', re.UNICODE)
DATA_LINE_RE = re.compile(ur'^(?P<prefix>\d+)\|(?P<location>.*)$', re.UNICODE)

# Boilerplate header
GEODATA_FILE_PROLOG = '''"""Geocoding data, mapping each prefix to a dict of locale:locationname.

Auto-generated file, do not edit by hand.
"""
'''

# Copyright notice covering the XML metadata; include current year.
COPYRIGHT_NOTICE = """# Copyright (C) 2011-%s The Libphonenumber Authors
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


def load_geodata_file(geodata, filename, locale, overall_prefix):
    """Load geocoding data from the given file, for the given locale and prefix.

    We assume that this file:
     - is encoded in UTF-8
     - may have comment lines (starting with #) and blank lines
     - has data lines of the form '<prefix>|<location_name>'
     - contains only data for prefixes that are extensions of the filename.
    """
    with open(filename, "rb") as infile:
        lineno = 0
        for line in infile:
            uline = line.decode('utf-8')
            lineno += 1
            dm = DATA_LINE_RE.match(uline)
            if dm:
                prefix = dm.group('prefix')
                location = dm.group('location')
                if not prefix.startswith(overall_prefix):
                    raise Exception("%s:%d: Prefix %s is not within %s" %
                                    (filename, lineno, prefix, overall_prefix))
                if prefix not in geodata:
                    geodata[prefix] = {}
                geodata[prefix][locale] = location
            elif BLANK_LINE_RE.match(uline):
                pass
            elif COMMENT_LINE_RE.match(uline):
                pass
            else:
                raise Exception("%s:%d: Unexpected line format: %s" %
                                (filename, lineno, line))


def load_geodata(indir):
    """Load geocoding data from the given top-level directory.

    Geocoding data is assumed to be held in files <indir>/<locale>/<prefix>.txt.
    The same prefix may occur in multiple files, giving the location's name in
    different locales.
    """
    geodata = {}  # prefix => dict mapping location to location name
    for locale in os.listdir(indir):
        if not os.path.isdir(os.path.join(indir, locale)):
            continue
        for filename in glob.glob(os.path.join(indir, locale, "*%s" % GEODATA_SUFFIX)):
            overall_prefix, ext = os.path.splitext(os.path.basename(filename))
            load_geodata_file(geodata, filename, locale, overall_prefix)
    return geodata


def _stable_dict_repr(strdict):
    """Return a repr() for a dict keyed by a string, in sorted key order"""
    # '4143':{'fr': u'Zurich', 'de': u'Z\xfcrich', 'en': u'Zurich', 'it': u'Zurigo'},
    lines = []
    for key in sorted(strdict.keys()):
        lines.append("%r: %r" % (key, strdict[key]))
    return "{%s}" % ", ".join(lines)


def output_geodata_code(geodata, outfilename):
    """Output the geocoding data in Python form to the given file """
    with open(outfilename, "w") as outfile:
        longest_prefix = 0
        print >> outfile, GEODATA_FILE_PROLOG
        print >> outfile, COPYRIGHT_NOTICE
        print >> outfile, "GEOCODE_DATA = {"
        for prefix in sorted(geodata.keys()):
            if len(prefix) > longest_prefix:
                longest_prefix = len(prefix)
            print >> outfile, " '%s':%s," % (prefix, _stable_dict_repr(geodata[prefix]))
        print >> outfile, "}"
        print >> outfile, "GEOCODE_LONGEST_PREFIX = %d" % longest_prefix


def _standalone(argv):
    """Parse the given input directory and emit generated code."""
    if len(argv) != 2:
        print >> sys.stderr, __doc__
        sys.exit(1)
    geodata = load_geodata(argv[0])
    output_geodata_code(geodata, argv[1])


if __name__ == "__main__":
    _standalone(sys.argv[1:])
