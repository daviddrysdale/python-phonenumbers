"""Auto-generated file, do not edit by hand. EC metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EC = PhoneMetadata(id='EC', country_code=593, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{7}|1\d{9,10}', possible_number_pattern=u'\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2-7][2-7]\d{6}', possible_number_pattern=u'\d{7,8}', example_number=u'22123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[89]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'99123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1800\d{6,7}', possible_number_pattern=u'\d{10,11}', example_number=u'18001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['[2-7]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1800)(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'\\1')],
    intl_number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[2-7]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(1800)(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'(0\\1)')])
