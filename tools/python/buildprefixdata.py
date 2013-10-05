#!/usr/bin/env python
"""Script to read the libphonenumber per-prefix metadata and generate Python code.

Invocation:
  buildprefixdata.py indir outfile

Processes all of the per-prefix data under the given input directory and emit
generated Python code.
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

if sys.version_info >= (3, 0):
    import builtins
    prnt = builtins.__dict__['print']
    u = str
    u = str
else:
    def prnt(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        file = kwargs.get('file', None)
        if file is None:
            file = sys.stdout
        print >> file, sep.join([str(arg) for arg in args]) + end,

    def u(s):
        return unicode(s)

PREFIXDATA_SUFFIX = ".txt"
BLANK_LINE_RE = re.compile(r'^\s*$', re.UNICODE)
COMMENT_LINE_RE = re.compile(r'^\s*#.*$', re.UNICODE)
DATA_LINE_RE = re.compile(r'^\+?(?P<prefix>\d+)\|(?P<location>.*)$', re.UNICODE)

# Boilerplate header
PREFIXDATA_FILE_PROLOG = '''"""Per-prefix data, mapping each prefix to a dict of locale:name.

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


def load_prefixdata_file(prefixdata, filename, locale, overall_prefix):
    """Load per-prefix data from the given file, for the given locale and prefix.

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
                if location != location.rstrip():
                    print ("%s:%d: Warning: stripping trailing whitespace" % (filename, lineno))
                    location = location.rstrip()
                if not prefix.startswith(overall_prefix):
                    raise Exception("%s:%d: Prefix %s is not within %s" %
                                    (filename, lineno, prefix, overall_prefix))
                if prefix not in prefixdata:
                    prefixdata[prefix] = {}
                prefixdata[prefix][locale] = location
            elif BLANK_LINE_RE.match(uline):
                pass
            elif COMMENT_LINE_RE.match(uline):
                pass
            else:
                raise Exception("%s:%d: Unexpected line format: %s" %
                                (filename, lineno, line))


def load_prefixdata(indir):
    """Load per-prefix data from the given top-level directory.

    Prefix data is assumed to be held in files <indir>/<locale>/<prefix>.txt.
    The same prefix may occur in multiple files, giving the location's name in
    different locales.
    """
    prefixdata = {}  # prefix => dict mapping location to location name
    for locale in os.listdir(indir):
        if not os.path.isdir(os.path.join(indir, locale)):
            continue
        for filename in glob.glob(os.path.join(indir, locale, "*%s" % PREFIXDATA_SUFFIX)):
            overall_prefix, ext = os.path.splitext(os.path.basename(filename))
            load_prefixdata_file(prefixdata, filename, locale, overall_prefix)
    return prefixdata


def _stable_dict_repr(strdict):
    """Return a repr() for a dict keyed by a string, in sorted key order"""
    lines = []
    for key in sorted(strdict.keys()):
        lines.append("%r: %r" % (key, strdict[key]))
    return "{%s}" % ", ".join(lines)


def output_prefixdata_code(prefixdata, outfilename, varprefix):
    """Output the per-prefix data in Python form to the given file """
    with open(outfilename, "w") as outfile:
        longest_prefix = 0
        prnt(PREFIXDATA_FILE_PROLOG, file=outfile)
        prnt(COPYRIGHT_NOTICE, file=outfile)
        prnt("%s_DATA = {" % varprefix, file=outfile)
        for prefix in sorted(prefixdata.keys()):
            if len(prefix) > longest_prefix:
                longest_prefix = len(prefix)
            prnt(" '%s':%s," % (prefix, _stable_dict_repr(prefixdata[prefix])), file=outfile)
        prnt("}", file=outfile)
        prnt("%s_LONGEST_PREFIX = %d" % (varprefix, longest_prefix), file=outfile)


def _standalone(argv):
    """Parse the given input directory and emit generated code."""
    varprefix = "GEOCODE"
    try:
        opts, args = getopt.getopt(argv, "hv:", ("help", "var="))
    except getopt.GetoptError:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)
        elif opt in ("-v", "--var"):
            varprefix = arg
        else:
            prnt("Unknown option %s" % opt, file=sys.stderr)
            prnt(__doc__, file=sys.stderr)
            sys.exit(1)
    if len(args) != 2:
        prnt(__doc__, file=sys.stderr)
        sys.exit(1)
    prefixdata = load_prefixdata(args[0])
    output_prefixdata_code(prefixdata, args[1], varprefix)


if __name__ == "__main__":
    _standalone(sys.argv[1:])
