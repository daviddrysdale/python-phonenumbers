"""Auto-generated file, do not edit by hand. CZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CZ = PhoneMetadata(id='CZ', country_code=420, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2\\d{8}|(?:3[1257-9]|4[16-9]|5[13-9])\\d{7}', possible_number_pattern='\\d{9}', example_number='212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:60[1-8]|7(?:0[25]|[2379]\\d))\\d{6}', possible_number_pattern='\\d{9}', example_number='601123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:0[05689]|76)\\d{6}', possible_number_pattern='\\d{9}', example_number='900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='8[134]\\d{7}', possible_number_pattern='\\d{9}', example_number='811234567'),
    personal_number=PhoneNumberDesc(national_number_pattern='70[01]\\d{6}', possible_number_pattern='\\d{9}', example_number='700123456'),
    voip=PhoneNumberDesc(national_number_pattern='9[17]0\\d{6}', possible_number_pattern='\\d{9}', example_number='910123456'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='9(?:5[056]|7[234])\\d{6}', possible_number_pattern='\\d{9}', example_number='972123456'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|5[058])', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='([2-9]\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3')])
