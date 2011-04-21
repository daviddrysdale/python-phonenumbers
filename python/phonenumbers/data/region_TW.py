"""Auto-generated file, do not edit by hand. TW metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TW = PhoneMetadata(id='TW', country_code=886, international_prefix='0(?:0[25679]|19)',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{7,8}', possible_number_pattern=u'\d{8,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2-8]\d{7,8}', possible_number_pattern=u'\d{8,9}', example_number=u'21234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9\d{8}', possible_number_pattern=u'\d{9}', example_number=u'912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{6}', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    preferred_extn_prefix=u'#',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([2-8])(\d{3,4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-7]|8[1-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['80|9'], national_prefix_formatting_rule=u'0\\1')])
