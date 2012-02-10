#!/usr/bin/env python
import sys
import re
import glob

import phonenumbers

INTERNAL_FILES = ['phonenumbers/util.py',
                  'phonenumbers/re_util.py',
                  'phonenumbers/unicode_util.py']
CLASS_RE = re.compile(r"^class +([A-Za-z][_A-Za-z0-9]+)[ \(:]")
FUNCTION_RE = re.compile("^def +([A-Za-z][_A-Za-z0-9]+)[ \(]")
CONSTANT_RE = re.compile("^([A-Z][_A-Z0-9]+) *= *")

grepped_all = set()
for filename in glob.glob('phonenumbers/*.py'):
    if filename in INTERNAL_FILES:
        continue
    with file(filename, "r") as infile:
        for line in infile:
            m = CLASS_RE.match(line)
            if m:
                grepped_all.add(m.group(1))
            m = FUNCTION_RE.match(line)
            if m:
                grepped_all.add(m.group(1))
            m = CONSTANT_RE.match(line)
            if m:
                grepped_all.add(m.group(1))

code_all = set(phonenumbers.__all__)
code_not_grepped = (code_all - grepped_all)
grepped_not_code = (grepped_all - code_all)
if len(code_not_grepped) > 0:
    print >> sys.stderr, "Found the following in __all__ but not in grepped code:"
    for identifier in code_not_grepped:
        print >> sys.stderr, "  %s" % identifier
if len(grepped_not_code) > 0:
    print >> sys.stderr, "Found the following in grepped code but not in__all__:"
    for identifier in grepped_not_code:
        print >> sys.stderr, "  %s" % identifier
