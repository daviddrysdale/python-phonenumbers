"""Auto-generated file, do not edit by hand. RU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RU = PhoneMetadata(id='RU', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[01]\\d{1,2}', possible_length=(2, 3)),
    emergency=PhoneNumberDesc(national_number_pattern='0[123]|112', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0[123]|112', example_number='112', possible_length=(2, 3)),
    short_data=True)
