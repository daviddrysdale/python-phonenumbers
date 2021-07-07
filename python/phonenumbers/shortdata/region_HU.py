"""Auto-generated file, do not edit by hand. HU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HU = PhoneMetadata(id='HU', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:0[457]|1(?:2|6\\d{3}))', example_number='104', possible_length=(3, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[457]|12)', example_number='104', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[457]|1(?:2|6(?:000|1(?:11|23)))|2(?:20|7[02])|37(?:00|37|7[07])|414|777|8(?:1[27-9]|2[04]|40|[589]))', example_number='104', possible_length=(3, 4, 5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:2[27]|41|77)\\d', example_number='1220', possible_length=(4,)),
    sms_services=PhoneNumberDesc(national_number_pattern='184\\d', example_number='1840', possible_length=(4,)),
    short_data=True)
