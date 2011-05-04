"""Auto-generated file, do not edit by hand. AZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AZ = PhoneMetadata(id='AZ', country_code=994, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{7,8}', possible_number_pattern=u'\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1(?:(?:[28]\d|9)\d|02|1[0-589]|3[358]|4[013-79]|5[0-479]|6[02346-9]|7[0-24-8])|2(?:16|2\d|3[0-24]|4[1468]|55|6[56]|79)|365?\d|44\d{2})\d{5}', possible_number_pattern=u'\d{5,9}', example_number=u'123123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:[46]0|5[015]|7[07])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'401234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'88\d{7}', possible_number_pattern=u'\d{9}', example_number=u'881234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900200\d{3}', possible_number_pattern=u'\d{9}', example_number=u'900200123'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['1[28]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['22'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{2,3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['3'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{3})(\d)(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['1[013-79]|2[013-9]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[4-8]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1')])
