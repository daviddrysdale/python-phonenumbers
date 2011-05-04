"""Auto-generated file, do not edit by hand. PE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PE = PhoneMetadata(id='PE', country_code=51, international_prefix='19(?:1[124]|77|90)00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[14-9]\d{7,8}', possible_number_pattern=u'\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1\d|4[1-4]|5[1-46]|6[1-7]|7[2-46]|8[2-4])\d{6}', possible_number_pattern=u'\d{6,8}', example_number=u'11234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9\d{8}', possible_number_pattern=u'\d{9}', example_number=u'912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    preferred_extn_prefix=u' Anexo ',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(1)(\d{7})', format=u'\\1 \\2', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'(\\1)'),
        NumberFormat(pattern='([4-8]\d)(\d{6})', format=u'\\1 \\2', leading_digits_pattern=['[4-8]'], national_prefix_formatting_rule=u'(\\1)'),
        NumberFormat(pattern='(9\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'\\1')])
