"""Auto-generated file, do not edit by hand. LT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LT = PhoneMetadata(id='LT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[01]\\d{1,5}', possible_length=(2, 3, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116\\d{3}', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:11?|22?|33?)|1(?:0[123]|12)', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:11?|22?|33?)|1(?:0[123]|1(?:2|6(?:000|1(?:11|23))))', example_number='112', possible_length=(2, 3, 6)),
    short_data=True)
