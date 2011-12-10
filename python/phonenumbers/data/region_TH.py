"""Auto-generated file, do not edit by hand. TH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TH = PhoneMetadata(id='TH', country_code=66, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7,8}|1\\d{3}(?:\\d{6})?', possible_number_pattern='\\d{4}|\\d{8,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2[1-9]|3[2-9]|4[2-5]|5[2-6]|7[3-7])\\d{6}', possible_number_pattern='\\d{8}', example_number='21234567'),
    mobile=PhoneNumberDesc(national_number_pattern='[89]\\d{8}', possible_number_pattern='\\d{9}', example_number='812345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900\\d{6}', possible_number_pattern='\\d{10}', example_number='1900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='60\\d{7}', possible_number_pattern='\\d{9}', example_number='601234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='1\\d{3}', possible_number_pattern='\\d{4}', example_number='1100'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:669|9[19])', possible_number_pattern='\\d{3,4}', example_number='191'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1\\d{3}', possible_number_pattern='\\d{4}', example_number='1100'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([3-7]\\d)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[3-7]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89])(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[89]00)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'\\1')])
