import threading
from typing import Callable, Optional

from .util import ImmutableMixin
from .util import UnicodeMixin

REGION_CODE_FOR_NON_GEO_ENTITY: str

class NumberFormat(UnicodeMixin, ImmutableMixin):
    pattern: Optional[str] = ...
    format: Optional[str] = ...
    leading_digits_pattern: list[str] = ...
    national_prefix_formatting_rule: Optional[str] = ...
    national_prefix_optional_when_formatting: Optional[bool] = ...
    domestic_carrier_code_formatting_rule: Optional[str] = ...
    def __init__(
        self,
        pattern: Optional[str] = ...,
        format: Optional[str] = ...,
        leading_digits_pattern: Optional[list[str]] = ...,
        national_prefix_formatting_rule: Optional[str] = ...,
        national_prefix_optional_when_formatting: Optional[bool] = ...,
        domestic_carrier_code_formatting_rule: Optional[str] = ...,
    ) -> None: ...
    def merge_from(self, other: NumberFormat) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __unicode__(self) -> str: ...

class PhoneNumberDesc(UnicodeMixin, ImmutableMixin):
    national_number_pattern: Optional[str] = ...
    example_number: Optional[str] = ...
    possible_length: tuple[int, ...] = ...
    possible_length_local_only: tuple[int, ...] = ...
    def __init__(
        self,
        national_number_pattern: Optional[str] = ...,
        example_number: Optional[str] = ...,
        possible_length: Optional[tuple[int, ...]] = ...,
        possible_length_local_only: Optional[tuple[int, ...]] = ...,
    ) -> None: ...
    def merge_from(self, other: PhoneNumberDesc) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __unicode__(self) -> str: ...

def _same_pattern(left: Optional[PhoneNumberDesc], right: Optional[PhoneNumberDesc]) -> bool: ...

class PhoneMetadata(UnicodeMixin, ImmutableMixin):
    _metadata_lock: threading.Lock
    _region_available: dict[str, Optional[Callable[[str], None]]]
    _short_region_available: dict[str, Optional[Callable[[str], None]]]
    _country_code_available: dict[int, Optional[Callable[[int], None]]]
    _region_metadata: dict[str, PhoneMetadata]
    _short_region_metadata: dict[str, PhoneMetadata]
    _country_code_metadata: dict[int, PhoneMetadata]
    general_desc: Optional[PhoneNumberDesc]
    fixed_line: Optional[PhoneNumberDesc]
    mobile: Optional[PhoneNumberDesc]
    toll_free: Optional[PhoneNumberDesc]
    premium_rate: Optional[PhoneNumberDesc]
    shared_cost: Optional[PhoneNumberDesc]
    personal_number: Optional[PhoneNumberDesc]
    voip: Optional[PhoneNumberDesc]
    pager: Optional[PhoneNumberDesc]
    uan: Optional[PhoneNumberDesc]
    emergency: Optional[PhoneNumberDesc]
    voicemail: Optional[PhoneNumberDesc]
    short_code: Optional[PhoneNumberDesc]
    standard_rate: Optional[PhoneNumberDesc]
    carrier_specific: Optional[PhoneNumberDesc]
    sms_services: Optional[PhoneNumberDesc]
    no_international_dialling: Optional[PhoneNumberDesc]
    id: str
    country_code: Optional[int]
    international_prefix: Optional[str]
    preferred_international_prefix: Optional[str]
    national_prefix: Optional[str]
    preferred_extn_prefix: Optional[str]
    national_prefix_for_parsing: Optional[str]
    national_prefix_transform_rule: Optional[str]
    same_mobile_and_fixed_line_pattern: bool
    number_format: list[NumberFormat]
    intl_number_format: list[NumberFormat]
    main_country_for_code: bool
    leading_digits: Optional[str]
    leading_zero_possible: bool
    mobile_number_portable_region: bool
    short_data: bool
    @classmethod
    def metadata_for_region(kls, region_code: str, default: Optional[PhoneMetadata] = ...) -> Optional[PhoneMetadata]: ...
    @classmethod
    def short_metadata_for_region(kls, region_code: str, default: Optional[PhoneMetadata] = ...) -> Optional[PhoneMetadata]: ...
    @classmethod
    def metadata_for_nongeo_region(kls, country_code: int, default: Optional[PhoneMetadata] = ...) -> Optional[PhoneMetadata]: ...
    @classmethod
    def metadata_for_region_or_calling_code(kls, country_calling_code: int, region_code: str) -> Optional[PhoneMetadata]: ...
    @classmethod
    def register_region_loader(kls, region_code: str, loader: Callable[[str], None]) -> None: ...
    @classmethod
    def register_short_region_loader(kls, region_code: str, loader: Callable[[str], None]) -> None: ...
    @classmethod
    def register_nongeo_region_loader(kls, country_code: int, loader: Callable[[int], None]) -> None: ...
    @classmethod
    def load_all(kls) -> None: ...
    def __init__(
        self,
        id: str,
        general_desc: Optional[PhoneNumberDesc] = ...,
        fixed_line: Optional[PhoneNumberDesc] = ...,
        mobile: Optional[PhoneNumberDesc] = ...,
        toll_free: Optional[PhoneNumberDesc] = ...,
        premium_rate: Optional[PhoneNumberDesc] = ...,
        shared_cost: Optional[PhoneNumberDesc] = ...,
        personal_number: Optional[PhoneNumberDesc] = ...,
        voip: Optional[PhoneNumberDesc] = ...,
        pager: Optional[PhoneNumberDesc] = ...,
        uan: Optional[PhoneNumberDesc] = ...,
        emergency: Optional[PhoneNumberDesc] = ...,
        voicemail: Optional[PhoneNumberDesc] = ...,
        short_code: Optional[PhoneNumberDesc] = ...,
        standard_rate: Optional[PhoneNumberDesc] = ...,
        carrier_specific: Optional[PhoneNumberDesc] = ...,
        sms_services: Optional[PhoneNumberDesc] = ...,
        no_international_dialling: Optional[PhoneNumberDesc] = ...,
        country_code: Optional[int] = ...,
        international_prefix: Optional[str] = ...,
        preferred_international_prefix: Optional[str] = ...,
        national_prefix: Optional[str] = ...,
        preferred_extn_prefix: Optional[str] = ...,
        national_prefix_for_parsing: Optional[str] = ...,
        national_prefix_transform_rule: Optional[str] = ...,
        number_format: Optional[list[NumberFormat]] = ...,
        intl_number_format: Optional[list[NumberFormat]] = ...,
        main_country_for_code: bool = ...,
        leading_digits: Optional[str] = ...,
        leading_zero_possible: bool = ...,
        mobile_number_portable_region: bool = ...,
        short_data: bool = ...,
        register: bool = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __unicode__(self) -> str: ...
