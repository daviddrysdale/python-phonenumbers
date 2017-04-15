"""Auto-generated file, do not edit by hand. GA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GA = PhoneMetadata(id='GA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,3}', possible_length=(2, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:730|8|3\\d{2})', example_number='1730', possible_length=(2, 4)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:730|8|3\\d{2})', example_number='1730', possible_length=(2, 4)),
    short_data=True)
