"""Auto-generated file, do not edit by hand. LT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LT = PhoneMetadata(id='LT', country_code=370, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[3-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3[1478]|4[124-6]|52)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'31234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6\d{7}', possible_number_pattern=u'\d{8}', example_number=u'61234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90[0239]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'90012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='([34]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['37|4(?:1|5[45]|6[2-4])'], national_prefix_formatting_rule=u'8 \\1'),
        NumberFormat(pattern='([3-689]\d{2})(\d{2})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3[148]|4(?:[24]|6[09])|5(?:[0189]|28)|[689]'], national_prefix_formatting_rule=u'8 \\1'),
        NumberFormat(pattern='(5)(2[0-79]\d)(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['52[0-79]'], national_prefix_formatting_rule=u'8 \\1')])
