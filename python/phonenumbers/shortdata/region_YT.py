"""Auto-generated file, do not edit by hand. YT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_YT = PhoneMetadata(id='YT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,2}', possible_length=(2, 3)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|5)', example_number='15', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:12|5)', example_number='112', possible_length=(2, 3)),
    short_data=True)
