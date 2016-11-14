"""Auto-generated file, do not edit by hand. RU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RU = PhoneMetadata(id='RU', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[01]\\d{1,2}', possible_number_pattern='\\d{2,3}', possible_length=(2, 3)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='0[123]|112', possible_number_pattern='\\d{2,3}', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0[123]|112', possible_number_pattern='\\d{2,3}', example_number='112', possible_length=(2, 3)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
