from .phonenumber import PhoneNumber

TIMEZONE_DATA: dict[str, tuple[str, ...]]
TIMEZONE_LONGEST_PREFIX: int
UNKNOWN_TIMEZONE: str
_UNKNOWN_TIME_ZONE_LIST: tuple[str, ...]

def time_zones_for_geographical_number(numobj: PhoneNumber) -> tuple[str, ...]: ...
def time_zones_for_number(numobj: PhoneNumber) -> tuple[str, ...]: ...
def _country_level_time_zones_for_number(numobj: PhoneNumber) -> tuple[str, ...]: ...
