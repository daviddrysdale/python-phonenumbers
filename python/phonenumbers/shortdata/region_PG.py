"""Auto-generated file, do not edit by hand. PG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PG = PhoneMetadata(id='PG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='0\\d{2}|1\\d{2,6}', possible_length=(3, 4, 5, 6, 7)),
    emergency=PhoneNumberDesc(national_number_pattern='000|11[01]', example_number='000', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='000|1(?:1[01]|5\\d{2}|6\\d{2,5})', example_number='000', possible_length=(3, 4, 5, 6, 7)),
    sms_services=PhoneNumberDesc(national_number_pattern='16\\d{2,5}', example_number='1612', possible_length=(4, 5, 6, 7)),
    short_data=True)
