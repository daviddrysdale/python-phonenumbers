"""Auto-generated file, do not edit by hand. JO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JO = PhoneMetadata(id='JO', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|9[127])|911', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:09|1[0-2]|9[0-24-79])|9(?:0903|11|8788)', example_number='111', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='9(?:0903|8788)', example_number='90903', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='9(?:0903|8788)', example_number='90903', possible_length=(5,)),
    short_data=True)
