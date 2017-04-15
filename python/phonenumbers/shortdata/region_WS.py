"""Auto-generated file, do not edit by hand. WS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_WS = PhoneMetadata(id='WS', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='9\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='99[4-6]', example_number='994', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='99[4-6]', example_number='994', possible_length=(3,)),
    short_data=True)
