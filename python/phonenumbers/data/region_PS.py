"""Auto-generated file, do not edit by hand. PS metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PS = PhoneMetadata(id='PS', country_code=970, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[24589]\d{7,8}|1(?:[78]\d{8}|[49]\d{2,3})', possible_number_pattern=u'\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:22[234789]|42[45]|82[01458]|92[369])\d{5}', possible_number_pattern=u'\d{7,8}', example_number=u'22234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'5[69]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'599123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1800\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'1(?:4|9\d)\d{2}', possible_number_pattern=u'\d{4,5}', example_number=u'19123'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'1700\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1700123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([2489])(2\d{2})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2489]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(5[69]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[78]00)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[78]'], national_prefix_formatting_rule=u'\\1')])
