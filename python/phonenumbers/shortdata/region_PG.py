"""Auto-generated file, do not edit by hand. PG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PG = PhoneMetadata(id='PG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='0\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='000', example_number='000', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='000', example_number='000', possible_length=(3,)),
    short_data=True)
