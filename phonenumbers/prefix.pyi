from typing import Optional

from .phonenumber import PhoneNumber

_LOCALE_NORMALIZATION_MAP: dict[str, str]

def _may_fall_back_to_english(lang: str) -> bool: ...
def _full_locale(lang: str, script: Optional[str], region: Optional[str]) -> str: ...
def _find_lang(langdict: dict[str, str], lang: str, script: Optional[str], region: Optional[str]) -> Optional[str]: ...
def _prefix_description_for_number(
    data: dict[str, dict[str, str]],
    longest_prefix: int,
    numobj: PhoneNumber,
    lang: str,
    script: Optional[str] = ...,
    region: Optional[str] = ...
) -> str: ...