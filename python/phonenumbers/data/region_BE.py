"""Auto-generated file, do not edit by hand. BE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BE = PhoneMetadata(id='BE', country_code=32, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7,8}', possible_number_pattern='\\d{8,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[0-69]|[23][2-8]|[49][23]|5\\d|6[013-57-9]|7[18])\\d{6}|8(?:0[1-9]|[1-69]\\d)\\d{5}', possible_number_pattern='\\d{8}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[67]\\d|8[3-9]|9[1-9])\\d{6}', possible_number_pattern='\\d{9}', example_number='470123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', possible_number_pattern='\\d{8}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:90|7[07])\\d{6}', possible_number_pattern='\\d{8}', example_number='90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='87\\d{6}', possible_number_pattern='\\d{8}', example_number='87123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[01]|12)', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(4[6-9]\\d)(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['4[6-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([2-49])(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[23]|[49][23]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([15-8]\\d)(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[156]|7[0178]|8(?:0[1-9]|[1-79])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['(?:80|9)0'], national_prefix_formatting_rule=u'0\\1')])
