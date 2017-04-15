"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='(?:11[24]|99[3-59])', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='(?:11[249]|99[3-59])', example_number='999', possible_length=(3,)),
    short_data=True)
