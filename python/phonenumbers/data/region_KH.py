"""Auto-generated file, do not edit by hand. KH metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KH = PhoneMetadata(id='KH', country_code=855, international_prefix='00[178]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7,9}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2[3-6]|3[2-6]|4[2-4]|[5-7][2-5])[2-47-9]\\d{5}', possible_number_pattern='\\d{6,8}', example_number='23456789'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:(?:1[0-35-9]|9[1-49])[1-9]|8(?:0[89]|5[2-689]))\\d{5}', possible_number_pattern='\\d{8}', example_number='91234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800(?:1\\d|2[09])\\d{4}', possible_number_pattern='\\d{10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900(?:1\\d|2[09])\\d{4}', possible_number_pattern='\\d{10}', example_number='1900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1\\d[1-9]|[2-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[89]00)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[89]0'])])
