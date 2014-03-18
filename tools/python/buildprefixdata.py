#!/usr/bin/env python
"""Script to read the libphonenumber per-prefix metadata and generate Python code.

Invocation:
  buildprefixdata.py [options] indir outfile module_prefix

Processes all of the per-prefix data under the given input directory and emit
generated Python code.

Options:
  --var XXX : use this prefix for variable names in generated code
  --flat    : don't do per-locale processing
  --sep C   : expect metadata to be a list with C as separator
"""

# Based on original metadata data files from libphonenumber:
#     resources/geocoding/*/*.txt, resources/carrier/*/*.txt
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
import getopt
import datetime
import math

# Use the local code in preference to any pre-installed version
sys.path.insert(0, '../../python')

from phonenumbers.util import prnt, rpr

PREFIXDATA_CHUNK_SIZE = 10000
PREFIXDATA_SUFFIX = ".txt"
BLANK_LINE_RE = re.compile(r'^\s*$', re.UNICODE)
COMMENT_LINE_RE = re.compile(r'^\s*#.*$', re.UNICODE)
DATA_LINE_RE = re.compile(r'^\+?(?P<prefix>\d+)\|(?P<stringdata>.*)$', re.UNICODE)

# Boilerplate header
PREFIXDATA_LOCALE_FILE_PROLOG = '''"""Per-prefix data, mapping each prefix to a dict of locale:name.

Auto-generated file, do not edit by hand.
"""
from %(module)s.util import u
'''
PREFIXDATA_FILE_PROLOG = '''"""Per-prefix data, mapping each prefix to a name.

Auto-generated file, do not edit by hand.
"""
from %(module)s.util import u
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


def load_locale_prefixdata_file(prefixdata, filename, locale=None, overall_prefix=None, separator=None):
    """Load per-prefix data from the given file, for the given locale and prefix.

    We assume that this file:
     - is encoded in UTF-8
     - may have comment lines (starting with #) and blank lines
     - has data lines of the form '<prefix>|<stringdata>'
     - contains only data for prefixes that are extensions of the filename.

    If overall_prefix is specified, lines are checked to ensure their prefix falls within this value.

    If locale is specified, prefixdata[prefix][locale] is filled in; otherwise, just prefixdata[prefix].

    If separator is specified, the string data will be split on this separator, and the output values
    in the dict will be tuples of strings rather than strings.
    """
    with open(filename, "rb") as infile:
        lineno = 0
        for line in infile:
            uline = line.decode('utf-8')
            lineno += 1
            dm = DATA_LINE_RE.match(uline)
            if dm:
                prefix = dm.group('prefix')
                stringdata = dm.group('stringdata')
                if stringdata != stringdata.rstrip():
                    print ("%s:%d: Warning: stripping trailing whitespace" % (filename, lineno))
                    stringdata = stringdata.rstrip()
                if overall_prefix is not None and not prefix.startswith(overall_prefix):
                    raise Exception("%s:%d: Prefix %s is not within %s" %
                                    (filename, lineno, prefix, overall_prefix))
                if separator is not None:
                    stringdata = tuple(stringdata.split(separator))
                if prefix not in prefixdata:
                    prefixdata[prefix] = {}
                if locale is not None:
                    prefixdata[prefix][locale] = stringdata
                else:
                    prefixdata[prefix] = stringdata
            elif BLANK_LINE_RE.match(uline):
                pass
            elif COMMENT_LINE_RE.match(uline):
                pass
            else:
                raise Exception("%s:%d: Unexpected line format: %s" %
                                (filename, lineno, line))


def load_locale_prefixdata(indir, separator=None):
    """Load per-prefix data from the given top-level directory.

    Prefix data is assumed to be held in files <indir>/<locale>/<prefix>.txt.
    The same prefix may occur in multiple files, giving the prefix's description
    in different locales.
    """
    prefixdata = {}  # prefix => dict mapping locale to description
    for locale in os.listdir(indir):
        if not os.path.isdir(os.path.join(indir, locale)):
            continue
        for filename in glob.glob(os.path.join(indir, locale, "*%s" % PREFIXDATA_SUFFIX)):
            overall_prefix, ext = os.path.splitext(os.path.basename(filename))
            load_locale_prefixdata_file(prefixdata, filename, locale, overall_prefix, separator)
    return prefixdata


def _stable_dict_repr(strdict):
    """Return a repr() for a dict keyed by a string, in sorted key order"""
    lines = []
    for key in sorted(strdict.keys()):
        lines.append("'%s': %s" % (key, rpr(strdict[key])))
    return "{%s}" % ", ".join(lines)


def _tuple_repr(data):
    """Return a repr() for a list/tuple"""
    if len(data) == 1:
        return "(%s,)" % rpr(data[0])
    else:
        return "(%s)" % ", ".join([rpr(x) for x in data])


def output_prefixdata_code(prefixdata, outfilename, module_prefix, varprefix, per_locale):
    """Output the per-prefix data in Python form to the given file """
    sorted_keys = sorted(prefixdata.keys())
    total_keys = len(sorted_keys)
    total_chunks = int(math.ceil(total_keys / float(PREFIXDATA_CHUNK_SIZE)))

    outdirname = os.path.dirname(outfilename)
    longest_prefix = 0
    for chunk_num in range(total_chunks):
        chunk_index = PREFIXDATA_CHUNK_SIZE * chunk_num
        chunk_keys = sorted_keys[chunk_index:chunk_index + PREFIXDATA_CHUNK_SIZE]
        chunk_data = {key: prefixdata[key] for key in chunk_keys}
        chunk_file = os.path.join(outdirname, 'data%d.py' % chunk_num)
        chunk_longest = output_prefixdata_chunk(
            chunk_data, chunk_file, module_prefix, per_locale)
        if chunk_longest > longest_prefix:
            longest_prefix = chunk_longest

    with open(outfilename, "w") as outfile:
        if per_locale:
            prnt(PREFIXDATA_LOCALE_FILE_PROLOG % {'module': module_prefix}, file=outfile)
        else:
            prnt(PREFIXDATA_FILE_PROLOG % {'module': module_prefix}, file=outfile)
        prnt(COPYRIGHT_NOTICE, file=outfile)
        prnt("%s_DATA = {}" % varprefix, file=outfile)
        for chunk_num in range(total_chunks):
            prnt("from .data%d import data" % chunk_num, file=outfile)
            prnt("%s_DATA.update(data)" % varprefix, file=outfile)
        prnt("del data", file=outfile)
        prnt("%s_LONGEST_PREFIX = %d" % (varprefix, longest_prefix), file=outfile)


def output_prefixdata_chunk(prefixdata, outfilename, module_prefix, per_locale):
    with open(outfilename, "w") as outfile:
        longest_prefix = 0
        if per_locale:
            prnt(PREFIXDATA_LOCALE_FILE_PROLOG % {'module': module_prefix}, file=outfile)
        else:
            prnt(PREFIXDATA_FILE_PROLOG % {'module': module_prefix}, file=outfile)
        prnt(COPYRIGHT_NOTICE, file=outfile)
        prnt("data = {", file=outfile)
        for prefix in prefixdata.keys():
            if len(prefix) > longest_prefix:
                longest_prefix = len(prefix)
            if per_locale:
                prnt(" '%s':%s," % (prefix, _stable_dict_repr(prefixdata[prefix])), file=outfile)
            else:
                prnt(" '%s':%s," % (prefix, _tuple_repr(prefixdata[prefix])), file=outfile)
        prnt("}", file=outfile)
    return longest_prefix


def _standalone(argv):
    """Parse the given input directory and emit generated code."""
    varprefix = "GEOCODE"
    per_locale = True
    separator = None
    try:
        opts, args = getopt.getopt(argv, "hv:fs:", ("help", "var=", "flat", "sep="))
    except getopt.GetoptError:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)
        elif opt in ("-v", "--var"):
            varprefix = arg
        elif opt in ("-f", "--flat"):
            per_locale = False
        elif opt in ("-s", "--sep"):
            separator = arg
        else:
            prnt("Unknown option %s" % opt, file=sys.stderr)
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)
    if len(args) != 3:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    if per_locale:
        prefixdata = load_locale_prefixdata(args[0], separator=separator)
    else:
        prefixdata = {}
        load_locale_prefixdata_file(prefixdata, args[0], separator=separator)
    output_prefixdata_code(prefixdata, args[1], args[2], varprefix, per_locale)


if __name__ == "__main__":
    _standalone(sys.argv[1:])
