"""Auto-generated file, do not edit by hand. AU metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='(?:14(?:1[14]|34|4[17]|[56]6|7[47]|88))?001[14-689]',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-578]\d{5,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2378]\d{8}', possible_number_pattern=u'\d{8,9}', example_number=u'212345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'4(?:[0-2]\d|3[0-57-9]|4[47-9]|5[0-37-9]|6[6-9]|7[07-9]|8[7-9])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'412345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1(?:80(?:0\d{2})?|3(?:00\d{2})?)\d{4}', possible_number_pattern=u'\d{6,10}', example_number=u'1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'190[0126]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'500\d{6}', possible_number_pattern=u'\d{9}', example_number=u'500123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'550\d{6}', possible_number_pattern=u'\d{9}', example_number=u'550123456'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'0011',
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([2378])(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2378]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(4\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['4'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(5[05]0)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[389]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1(?:[38]0|9)', '1(?:[38]00|9)'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(180)(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['180', '180[1-9]'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(13)(\d{2})(\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['13[1-9]'], national_prefix_formatting_rule=u'\\1')])
