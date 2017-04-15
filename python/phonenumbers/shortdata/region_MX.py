"""Auto-generated file, do not edit by hand. MX metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MX = PhoneMetadata(id='MX', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[0579]\\d{2,4}', possible_length=(3, 4, 5)),
    premium_rate=PhoneNumberDesc(national_number_pattern='53053|7766', example_number='7766', possible_length=(4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:6[0568]|80)|911', example_number='066', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:[249]0|3[01]|5[015]|6[01568]|7[0-578]|8[089])|53053|7766|911', example_number='030', possible_length=(3, 4, 5)),
    short_data=True)
