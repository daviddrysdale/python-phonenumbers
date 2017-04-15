"""Auto-generated file, do not edit by hand. TR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TR = PhoneMetadata(id='TR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[15]\\d{2,3}', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[02]|55)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[02]|55)|5420', example_number='112', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(national_number_pattern='5420', example_number='5420', possible_length=(4,)),
    short_data=True)
