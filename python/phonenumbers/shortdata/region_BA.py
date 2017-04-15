"""Auto-generated file, do not edit by hand. BA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BA = PhoneMetadata(id='BA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='12[234]', example_number='122', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='12[234]', example_number='122', possible_length=(3,)),
    short_data=True)
