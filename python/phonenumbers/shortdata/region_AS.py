"""Auto-generated file, do not edit by hand. AS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AS = PhoneMetadata(id='AS', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[49]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='911', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='40404|911', example_number='911', possible_length=(3, 5)),
    short_data=True)
