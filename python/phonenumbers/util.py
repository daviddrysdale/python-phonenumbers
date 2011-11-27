#!/usr/bin/env python
"""Python 2.x/3.x compatibility utilities.

>>> from .util import prnt, u, uchr
>>> prnt("hello")
hello
>>> prnt("hello", "world")
hello world
>>> prnt("hello", "world", sep=":")
hello:world
>>> prnt("hello", "world", sep=":", end='!\\n')
hello:world!
>>> u('\u0101') == uchr(0x0101)
True
>>> u('\u0101') == u('\U00000101')
True
>>> u('\u0101') == u('\N{LATIN SMALL LETTER A WITH MACRON}')
True
"""
import sys


if sys.version_info >= (3, 0):  # pragma no cover
    import builtins
    print3 = builtins.__dict__['print']

    u = str
    uchr = chr
    to_long = int
    # TODO create a Py3k repr-equivalent that produces something
    # parsable in Python 2 (with the assistance of this module)
    rpr = repr

    def prnt(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        file = kwargs.get('file', None)
        print3(*args, sep=sep, end=end, file=file)

    class UnicodeMixin(object):
        __str__ = lambda x: x.__unicode__()

else:  # pragma no cover
    import unicodedata
    import re
    # \N{name} = character named name in the Unicode database
    _UNAME_RE = re.compile(r'\\N\{(?P<name>[^}]+)\}')
    # \uxxxx = character with 16-bit hex value xxxx
    _U16_RE = re.compile(r'\\u(?P<hexval>[0-9a-fA-F]{4})')
    # \Uxxxxxxxx = character with 32-bit hex value xxxxxxxx
    _U32_RE = re.compile(r'\\U(?P<hexval>[0-9a-fA-F]{8})')

    def u(s):
        us = re.sub(_U16_RE, lambda m: unichr(int(m.group('hexval'), 16)), unicode(s))
        us = re.sub(_U32_RE, lambda m: unichr(int(m.group('hexval'), 16)), us)
        us = re.sub(_UNAME_RE, lambda m: unicodedata.lookup(m.group('name')), us)
        return us

    uchr = unichr
    to_long = long

    _U_SQ_RE = re.compile("^u('[^']*')")
    _U_DQ_RE = re.compile('^u("[^"]*")')
    _X_LATIN1_RE = re.compile(r"(?P<x>\\x)(?P<hexval>[0-9a-fA-Z]{2})")
    def rpr(obj):
        s = repr(obj)
        # Assume any \xYY sequences are taking advantage of Python 2's default
        # Latin-1 string encoding
        s = re.sub(_X_LATIN1_RE, '\\u00\g<hexval>', s)
        s = re.sub(_U_SQ_RE, r'u(\1)', s)
        s = re.sub(_U_DQ_RE, r'u(\1)', s)
        return s

    def prnt(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        file = kwargs.get('file', None)
        if file is None:
            file = sys.stdout
        print >> file, sep.join([str(arg) for arg in args]) + end,

    class UnicodeMixin(object):  # pragma no cover
        __str__ = lambda x: unicode(x).encode('utf-8')


if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
