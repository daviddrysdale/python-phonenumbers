from typing import Any, Callable, Literal, overload

print3: Callable[..., None]
unicod = str
u = str
to_long = int

def prnt(*args: Any, **kwargs: Any) -> None: ...

class UnicodeMixin: ...

U_EMPTY_STRING: str
U_SPACE: str
U_DASH: str
U_TILDE: str
U_PLUS: str
U_STAR: str
U_ZERO: str
U_SLASH: str
U_SEMICOLON: str
U_X_LOWER: str
U_X_UPPER: str
U_PERCENT: str

def rpr(s: object) -> str: ...
@overload
def force_unicode(s: None) -> None: ...  # type: ignore[misc]
@overload
def force_unicode(s: object) -> str: ...

class ImmutableMixin:
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

def mutating_method(func: Callable[..., Any]) -> Callable[..., Any]: ...
