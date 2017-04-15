"""Auto-generated file, do not edit by hand. MN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MN = PhoneMetadata(id='MN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='10[0-3]', example_number='102', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='10[0-3]', example_number='102', possible_length=(3,)),
    short_data=True)
