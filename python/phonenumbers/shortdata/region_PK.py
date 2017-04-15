"""Auto-generated file, do not edit by hand. PK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PK = PhoneMetadata(id='PK', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,3}', possible_length=(2, 3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1(?:22?|5)|[56])', example_number='112', possible_length=(2, 3, 4)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:22?|5)|[56])', example_number='112', possible_length=(2, 3, 4)),
    short_data=True)
