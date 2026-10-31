"""Additional regular expression utilities, to make it easier to sync up
with Java regular expression code.

>>> import re
>>> from .re_util import fullmatch
>>> from .util import u
>>> string = 'abcd'
>>> r1 = re.compile('abcd')
>>> r2 = re.compile('bc')
>>> r3 = re.compile('abc')
>>> fullmatch(r1, string)  # doctest: +ELLIPSIS
<...Match object...>
>>> fullmatch(r2, string)
>>> fullmatch(r3, string)
>>> r = re.compile(r'\\d{8}|\\d{10,11}')
>>> m = fullmatch(r, '1234567890')
>>> m.end()
10
>>> r = re.compile(u(r'[+\uff0b\\d]'), re.UNICODE)
>>> m = fullmatch(r, u('\uff10'))
>>> m.end()
1
"""
import re
import sys

if sys.version_info >= (3, 4):  # pragma no cover

    def fullmatch(pattern, string):
        """Try to apply the pattern at the start of the string, returning a match
        object if the whole string matches, or None if no match was found."""

        return pattern.fullmatch(string)

else:  # pragma no cover

    def fullmatch(pattern, string):
        """Try to apply the pattern at the start of the string, returning a match
        object if the whole string matches, or None if no match was found."""
        # Build a version of the pattern with a non-capturing group around it.
        # This is needed to get m.end() to correctly report the size of the
        # matched expression (as per the final doctest above).
        grouped_pattern = re.compile("^(?:%s)$" % pattern.pattern, pattern.flags)
        m = grouped_pattern.match(string)
        if m and m.end() < len(string):
            # Incomplete match (which should never happen because of the $ at the
            # end of the regexp), treat as failure.
            m = None  # pragma no cover
        return m


# Compiled regular expressions, keyed by pattern string, or None while the
# cache is off (the default).  The patterns used come from the (fixed) metadata,
# so the number of entries is bounded; holding on to them means that
# applications which work with numbers from many regions don't keep recompiling
# patterns that have dropped out of the re module's own, smaller, cache.
_COMPILED_PATTERNS = None


def enable_pattern_cache():
    """Keep every compiled metadata regular expression from now on, rather than
    relying on the re module's own (bounded) cache."""
    global _COMPILED_PATTERNS
    if _COMPILED_PATTERNS is None:
        _COMPILED_PATTERNS = {}


def re_compile(regex):
    """Return a compiled version of the given regular expression string.  Once
    enable_pattern_cache() has been called, an earlier compilation of the same
    string is re-used (as the RegexCache class in the Java code does);
    otherwise this is just re.compile."""
    if _COMPILED_PATTERNS is None:
        return re.compile(regex)
    pattern = _COMPILED_PATTERNS.get(regex, None)
    if pattern is None:
        pattern = re.compile(regex)
        _COMPILED_PATTERNS[regex] = pattern
    return pattern


if __name__ == '__main__':  # pragma no cover
    import doctest
    doctest.testmod()
