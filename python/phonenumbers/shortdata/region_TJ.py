"""Auto-generated file, do not edit by hand. TJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TJ = PhoneMetadata(id='TJ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[1-3]|12)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[1-3]|12)', example_number='112', possible_length=(3,)),
    short_data=True)
