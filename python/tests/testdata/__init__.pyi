_AVAILABLE_REGION_CODES: list[str]
_AVAILABLE_NONGEO_COUNTRY_CODES: list[int]

def _load_region(code: str | int) -> None: ...
_COUNTRY_CODE_TO_REGION_CODE: dict[int, tuple[str, ...]]
