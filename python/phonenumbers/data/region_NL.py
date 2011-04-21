"""Auto-generated file, do not edit by hand. NL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NL = PhoneMetadata(id='NL', country_code=31, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{6,9}', possible_number_pattern=u'\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1[0135-8]|2[02-69]|3[0-68]|4[0135-9]|[57]\d|8[478])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'101234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6[1-58]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{4,7}', possible_number_pattern=u'\d{7,10}', example_number=u'8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90[069]\d{4,7}', possible_number_pattern=u'\d{7,10}', example_number=u'9001234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'85\d{7}', possible_number_pattern=u'\d{9}'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([1-578]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[035]|2[0346]|3[03568]|4[0356]|5[0358]|7|8[458]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([1-5]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[16-8]|2[259]|3[124]|4[17-9]|5[124679]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(6)(\d{8})', format=u'\\1 \\2', leading_digits_pattern=['6'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]0\d)(\d{4,7})', format=u'\\1 \\2', leading_digits_pattern=['80|9'], national_prefix_formatting_rule=u'0\\1')])
