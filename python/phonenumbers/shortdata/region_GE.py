"""Auto-generated file, do not edit by hand. GE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GE = PhoneMetadata(id='GE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[041]\\d{2,4}', possible_number_pattern='\\d{3,5}', possible_length=(3, 5)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:11|22|33)|1(?:1[123]|22)', possible_number_pattern='\\d{3}', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:11|22|33)|1(?:1[123]|22)|40404', possible_number_pattern='\\d{3,5}', example_number='112', possible_length=(3, 5)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', possible_number_pattern='\\d{5}', example_number='40404', possible_length=(5,)),
    short_data=True)
