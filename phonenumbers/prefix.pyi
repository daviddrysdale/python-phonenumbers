from typing import Optional

from .phonenumber import PhoneNumber

def _prefix_description_for_number(
    data: dict[str, dict[str, str]],
    longest_prefix: int,
    numobj: PhoneNumber,
    lang: str,
    script: Optional[str] = ...,
    region: Optional[str] = ...
) -> str: ...