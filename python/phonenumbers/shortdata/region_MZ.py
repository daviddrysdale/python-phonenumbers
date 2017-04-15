"""Auto-generated file, do not edit by hand. MZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MZ = PhoneMetadata(id='MZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,3}', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[79]|9[78])', example_number='119', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:[02-5]\\d{2}|1[79]|9[78])', example_number='1011', possible_length=(3, 4)),
    short_data=True)
