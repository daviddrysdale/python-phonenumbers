"""Auto-generated file, do not edit by hand. VA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VA = PhoneMetadata(id='VA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[2358]', example_number='113', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[2358]', example_number='113', possible_length=(3,)),
    short_data=True)
