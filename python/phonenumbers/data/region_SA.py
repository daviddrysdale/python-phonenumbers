"""Auto-generated file, do not edit by hand. SA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SA = PhoneMetadata(id='SA', country_code=966, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-467]\\d{7}|5\\d{8}|(?:8|92)\\d{9}', possible_number_pattern='\\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[12][24-8]|3[35-8]|4[34-68]|6[2-5]|7[235-7])\\d{6}', possible_number_pattern='\\d{7,8}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[013-689]\\d|8111)\\d{6}', possible_number_pattern='\\d{9,10}', example_number='512345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9200\\d{7}', possible_number_pattern='\\d{11}', example_number='92001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='99[7-9]', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([1-467])(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-467]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9200)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(5\\d)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(800)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['80'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(8111)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['81'], national_prefix_formatting_rule=u'0\\1')])
