"""Auto-generated file, do not edit by hand. IQ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IQ = PhoneMetadata(id='IQ', country_code=964, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-7]\d{7,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'1\d{7}|(?:2[13-5]|3[02367]|4[023]|5[03]|6[026])\d{6,7}', possible_number_pattern=u'\d{6,9}', example_number=u'12345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[5-9]\d{8}', possible_number_pattern=u'\d{10}', example_number=u'7912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(1)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([2-6]\d)(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-6]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(7[5-9]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule=u'0\\1')])
