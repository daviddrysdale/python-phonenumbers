"""Auto-generated file, do not edit by hand. NP metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NP = PhoneMetadata(id='NP', country_code=977, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-8]\\d{5,7}|98[45]\\d{7}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[014-6]|2[13-79]|3[135-8]|4[146-9]|5[135-7]|6[13-9]|7[15-9]|8[1-4679]|9[1-79])\\d{6}', possible_number_pattern='\\d{6,8}', example_number='14567890'),
    mobile=PhoneNumberDesc(national_number_pattern='98[45]\\d{7}', possible_number_pattern='\\d{10}', example_number='9841234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(1)([4-6]\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[4-6]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[01]|[2-8]|9[1-79]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(98[45])(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['98'], national_prefix_formatting_rule=u'0\\1')])
