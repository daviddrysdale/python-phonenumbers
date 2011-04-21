"""Auto-generated file, do not edit by hand. LR metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LR = PhoneMetadata(id='LR', country_code=231, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'(?:[279]\d|[4-6])\d{6}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2\d{7}', possible_number_pattern=u'\d{8}', example_number=u'21234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:4[67]|5\d|6[4-8]|7\d{2})\d{5}', possible_number_pattern=u'\d{7,8}', example_number=u'4612345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([279]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[279]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([4-6])(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[4-6]'], national_prefix_formatting_rule=u'0\\1')])
