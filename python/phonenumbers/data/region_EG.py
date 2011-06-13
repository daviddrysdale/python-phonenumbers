"""Auto-generated file, do not edit by hand. EG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EG = PhoneMetadata(id='EG', country_code=20, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{4,9}|[2456]\\d{8}|3\\d{7}|[89]\\d{8,9}', possible_number_pattern='\\d{5,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[35][23]|2[23]\\d|3\\d|4(?:0[2-4]|[578][23]|64)|5(?:0[234]|[57][23])|6[24-689]3|8(?:[28][2-4]|42|6[23])|9(?:[25]2|3[24]|6[23]|7[2-4]))\\d{6}|1[69]\\d{3}', possible_number_pattern='\\d{5,9}', example_number='234567890'),
    mobile=PhoneNumberDesc(national_number_pattern='1[0-246-9]\\d{7}', possible_number_pattern='\\d{9}', example_number='101234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', possible_number_pattern='\\d{10}', example_number='9001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{7,8})', format=u'\\1 \\2', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['[14-6]|[89][2-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]00)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]00'], national_prefix_formatting_rule=u'0\\1')])
