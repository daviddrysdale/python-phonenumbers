"""Auto-generated file, do not edit by hand. NZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NZ = PhoneMetadata(id='NZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,3}', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='111', example_number='111', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='111|4098', example_number='111', possible_length=(3, 4)),
    short_data=True)
