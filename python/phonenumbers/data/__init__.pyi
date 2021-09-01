from typing import Union

from ..phonemetadata import NumberFormat

_AVAILABLE_REGION_CODES: list[str]
_AVAILABLE_NONGEO_COUNTRY_CODES: list[int]

def _load_region(code: Union[str, int]) -> None: ...

_ALT_NUMBER_FORMATS: dict[int, list[NumberFormat]]
_COUNTRY_CODE_TO_REGION_CODE: dict[int, tuple[str, ...]]
