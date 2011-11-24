import sys


class UnicodeMixin(object):  # pragma no cover
    """Define __str__ operator in terms of __unicode__ for Python 2/3"""
    if sys.version_info >= (3, 0):
        __str__ = lambda x: x.__unicode__()
    else:
        __str__ = lambda x: unicode(x).encode('utf-8')
