"""Auto-generated file, do not edit by hand. ES metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ES = PhoneMetadata(id='ES', country_code=34, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[5-9]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:8(?:[13]0|[28][0-8]|[47][1-9]|5[01346-9]|6[0457-9])|9(?:[1238][0-8]|[47][1-9]|[56]\\d))\\d{6}', possible_number_pattern='\\d{9}', example_number='810123456'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:6\\d|7[1-4])\\d{7}', possible_number_pattern='\\d{9}', example_number='612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='[89]00\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='80[367]\\d{6}', possible_number_pattern='\\d{9}', example_number='803123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='90[12]\\d{6}', possible_number_pattern='\\d{9}', example_number='901123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{7}', possible_number_pattern='\\d{9}', example_number='701234567'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='51\\d{7}', possible_number_pattern='\\d{9}', example_number='511234567'),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:61|8[05]|9[12])|112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='([5-9]\\d{2})(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4')])
