"""Auto-generated file, do not edit by hand. CH metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CH = PhoneMetadata(id='CH', country_code=41, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2[12467]|3[1-4]|4[134]|5[12568]|6[12]|[7-9]1)\d{7}', possible_number_pattern=u'\d{9}', example_number=u'212345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[46-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'741234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90[016]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'84[0248]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'840123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'878\d{6}', possible_number_pattern=u'\d{9}', example_number=u'878123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([2-9]\d)(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[2-7]|[89]1'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8[047]|90'], national_prefix_formatting_rule=u'0\\1')])
