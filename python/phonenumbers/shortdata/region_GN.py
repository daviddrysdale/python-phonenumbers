"""Auto-generated file, do not edit by hand. GN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GN = PhoneMetadata(id='GN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='4\\d{4}', possible_number_pattern='\\d{5}', possible_length=(5,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(),
    short_code=PhoneNumberDesc(national_number_pattern='40404', possible_number_pattern='\\d{5}', example_number='40404', possible_length=(5,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', possible_number_pattern='\\d{5}', example_number='40404', possible_length=(5,)),
    short_data=True)
