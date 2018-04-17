"""Auto-generated file, do not edit by hand. BD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BD = PhoneMetadata(id='BD', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[179]\\d{2,4}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='106', example_number='106', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[0-2]|99)|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[0-39]|5(?:0\\d|[1-4])|6(\\d{2})?|7[0-4]|8[0-29])|1[16-9]|2(?:[134]|2[0-5])|3(?:1\\d?|3\\d|6[3-6])|4(?:0\\d|1\\d{2})|5[2-9]|99)|786|5012|9(?:594|99)', example_number='103', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:11|2[13])|786|5012|9594', example_number='9594', possible_length=(3, 4)),
    sms_services=PhoneNumberDesc(national_number_pattern='9594', example_number='9594', possible_length=(4,)),
    short_data=True)
