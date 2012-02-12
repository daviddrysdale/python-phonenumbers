import sys


class UnicodeMixin(object):  # pragma no cover
    """Define __str__ operator in terms of __unicode__ for Python 2/3"""
    if sys.version_info >= (3, 0):
        __str__ = lambda x: x.__unicode__()
    else:
        __str__ = lambda x: unicode(x).encode('utf-8')


class ImmutableMixin(object):
    """Mixin class to make objects of subclasses immutable"""
    _mutable = False

    def __setattr__(self, name, value):
        if self._mutable or name == "_mutable":
            object.__setattr__(self, name, value)
        else:
            raise TypeError("Can't modify immutable instance")

    def __delattr__(self, name):
        if self._mutable:
            object.__delattr__(self, name)
        else:
            raise TypeError("Can't modify immutable instance")


def mutating_method(func):
    """Decorator for methods that are allowed to modify immutable objects"""
    def wrapper(self, *__args, **__kwargs):
        old_mutable = self._mutable
        self._mutable = True
        try:
            # Call the wrapped function
            return func(self, *__args, **__kwargs)
        finally:
            self._mutable = old_mutable
    return wrapper
