"""Auto-generated file, do not edit by hand. MY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MY = PhoneMetadata(id='MY', country_code=60, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13-9]\d{7,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3\d{2}|[4-79]\d|8[2-9])\d{6}', possible_number_pattern=u'\d{6,9}', example_number=u'312345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'1[0-46-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1[38]00\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1300123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'1600\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1600123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'1700\d{6}', possible_number_pattern=u'\d{10}', example_number=u'1700123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'154\d{7}', possible_number_pattern=u'\d{10}', example_number=u'1541234567'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([4-79])(\d{3})(\d{4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['[4-79]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(3)(\d{4})(\d{4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['3'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([18]\d)(\d{3})(\d{3,4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['1[0-46-9][1-9]|8'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1)([36-8]00)(\d{2})(\d{4})', format=u'\\1-\\2-\\3-\\4', leading_digits_pattern=['1[36-8]0']),
        NumberFormat(pattern='(154)(\d{3})(\d{4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['15'], national_prefix_formatting_rule=u'0\\1')])
