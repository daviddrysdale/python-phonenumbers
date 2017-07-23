"""Auto-generated file, do not edit by hand. IT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IT = PhoneMetadata(id='IT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,6}', possible_length=(3, 4, 5, 6, 7)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:16\\d{3}|87)', example_number='187', possible_length=(3, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:12|4(?:[478]\\d{1,3}|55))\\d{2}', example_number='1254', possible_length=(4, 5, 6, 7)),
    emergency=PhoneNumberDesc(national_number_pattern='11[2358]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0\\d{2,3}|1(?:[2-5789]|6(?:000|111))|2\\d{2}|3[39]|4(?:82|9\\d{1,3})|5(?:00|1[58]|2[25]|3[03]|44|[59])|60|8[67]|9(?:[01]|2(?:[01]\\d{2}|[2-9])|4\\d|696))|4(?:2323|3(?:[01]|[45]\\d{2})\\d{2}|[478](?:[0-4]|[5-9]\\d{2})\\d{2}|5(?:045|5\\d{2}))', example_number='114', possible_length=(3, 4, 5, 6, 7)),
    sms_services=PhoneNumberDesc(national_number_pattern='4[3-578]\\d{3,5}', example_number='43000', possible_length=(5, 6, 7)),
    short_data=True)
