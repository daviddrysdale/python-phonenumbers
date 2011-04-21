"""Auto-generated file, do not edit by hand. BG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BG = PhoneMetadata(id='BG', country_code=359, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{6,8}', possible_number_pattern=u'\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2\d|[36]\d|5[1-9]|8[1-6]|9[1-7])\d{5,6}|(?:4(?:[124-7]\d|3[1-6])|7(?:0[1-9]|[1-9]\d))\d{4,5}', possible_number_pattern=u'\d{7,8}', example_number=u'2123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:8[7-9]|98)\d{7}|4(?:3[0789]|8\d)\d{5}', possible_number_pattern=u'\d{8,9}', example_number=u'48123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'700\d{5}', possible_number_pattern=u'\d{7,9}', example_number=u'70012345'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(2)(\d{3})(\d{3,4})', format=u'\\1/\\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1/\\2', leading_digits_pattern=['43[124-7]|70[1-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{2})', format=u'\\1/\\2 \\3', leading_digits_pattern=['43[124-7]|70[1-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{2})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[78]00'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{2,3})', format=u'\\1/\\2 \\3', leading_digits_pattern=['[356]|7[1-9]|8[1-6]|9[1-7]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['48|8[7-9]|9[08]'], national_prefix_formatting_rule=u'0\\1')])
