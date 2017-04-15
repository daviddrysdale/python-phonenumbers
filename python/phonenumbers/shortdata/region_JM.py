"""Auto-generated file, do not edit by hand. JM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JM = PhoneMetadata(id='JM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[029]|911', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[029]|76)|911', example_number='911', possible_length=(3,)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='176', example_number='176', possible_length=(3,)),
    short_data=True)
