from re import Match
from re import Pattern
from typing import Optional

def fullmatch(pattern: Pattern[str], string: str, flags: int = ...) -> Optional[Match[str]]: ...
