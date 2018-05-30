"""Auto-generated file, do not edit by hand. PM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PM = PhoneMetadata(id='PM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d|3103', possible_length=(2, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1[578]', example_number='17', possible_length=(2,)),
    short_code=PhoneNumberDesc(national_number_pattern='1[578]|3103', example_number='17', possible_length=(2, 4)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='3103', example_number='3103', possible_length=(4,)),
    short_data=True)
