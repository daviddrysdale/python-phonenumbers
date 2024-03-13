"""Auto-generated file, do not edit by hand. CN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CN = PhoneMetadata(id='CN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d\\d(?:\\d{2,3})?', possible_length=(3, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1[09]|2(?:[02]|[13]\\d\\d))', example_number='110', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[09]|20)', example_number='110', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:00\\d\\d|1[029]|2(?:[02]|110|395))|95\\d{3,4}', example_number='110', possible_length=(3, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='1(?:00\\d\\d|12)|95\\d{3,4}', example_number='112', possible_length=(3, 5, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='121\\d\\d', example_number='12100', possible_length=(5,)),
    short_data=True)
