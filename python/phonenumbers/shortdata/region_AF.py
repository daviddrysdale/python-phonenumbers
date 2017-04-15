"""Auto-generated file, do not edit by hand. AF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AF = PhoneMetadata(id='AF', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:02|19)', example_number='119', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:02|19)|40404', example_number='119', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', example_number='40404', possible_length=(5,)),
    short_data=True)
