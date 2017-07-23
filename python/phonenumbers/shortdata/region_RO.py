"""Auto-generated file, do not edit by hand. RO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RO = PhoneMetadata(id='RO', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[18]\\d{2,5}', possible_length=(3, 4, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116(?:000|111)', example_number='116000', possible_length=(6,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:1(?:18(?:300|932)|[24]\\d{2})|8[48]\\d{2})', example_number='8844', possible_length=(4, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='112', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:2|6(?:000|111)|8(?:300|932))|[24]\\d{2}|9(?:21|3[02]|5[178]))|8[48]\\d{2}', example_number='112', possible_length=(3, 4, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='(?:1[24]|8[48])\\d{2}', example_number='8844', possible_length=(4,)),
    short_data=True)
