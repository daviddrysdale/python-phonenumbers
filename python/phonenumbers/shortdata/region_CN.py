"""Auto-generated file, do not edit by hand. CN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CN = PhoneMetadata(id='CN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d\\d(?:\\d(?:\\d(?:\\d(?:\\d\\d(?:\\d{3,4})?)?)?)?)?', possible_length=(3, 4, 5, 6, 8, 11, 12)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1[09]|2(?:[02]|1\\d\\d|395))', example_number='110', possible_length=(3, 5)),
    premium_rate=PhoneNumberDesc(national_number_pattern='106[26]\\d{4}', example_number='10620000', possible_length=(8,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[09]|20)', example_number='110', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:(?:0(?:[0-2]\\d|6(?:(?:[268]\\d|[39](?:[0-49]|[5-8]\\d{4}))\\d\\d|5)|8)|2[13]\\d)\\d|1[0249]|6[08])|9[56]\\d{3,4}|1(?:0(?:0|690\\d{6})|2[023])', example_number='100', possible_length=(3, 4, 5, 6, 8, 11, 12)),
    standard_rate=PhoneNumberDesc(national_number_pattern='1(?:0(?:(?:[0-2]\\d|8)\\d|6[3589]\\d(?:\\d{3}(?:\\d{3,4})?)?)|1[24]|23(?:[0-8]\\d|9[0-46-9])?|6[08])|9[56]\\d{3,4}|100', example_number='100', possible_length=(3, 4, 5, 6, 8, 11, 12)),
    sms_services=PhoneNumberDesc(national_number_pattern='1(?:06\\d\\d(?:\\d{3}(?:\\d{3,4})?)?|2110)', example_number='10600', possible_length=(5, 8, 11, 12)),
    short_data=True)
