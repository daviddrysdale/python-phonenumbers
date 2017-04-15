"""Auto-generated file, do not edit by hand. PY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PY = PhoneMetadata(id='PY', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='128|911', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1[1-4]\\d|911', example_number='123', possible_length=(3,)),
    short_data=True)
