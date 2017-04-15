"""Auto-generated file, do not edit by hand. SH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SH = PhoneMetadata(id='SH', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,3}', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='9(?:11|99)', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1\\d{2,3}|9(?:11|99)', example_number='1234', possible_length=(3, 4)),
    short_data=True)
