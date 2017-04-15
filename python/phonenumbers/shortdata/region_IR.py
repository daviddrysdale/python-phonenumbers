"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[025]|25)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[025]|25)', example_number='112', possible_length=(3,)),
    short_data=True)
