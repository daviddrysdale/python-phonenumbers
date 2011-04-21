"""Auto-generated file, do not edit by hand. CZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CZ = PhoneMetadata(id='CZ', country_code=420, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2\d{8}|(?:3[1257-9]|4[16-9]|5[13-9])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'212345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'60[1-8]\d{6}|7[2379]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'601123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90[0689]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8[134]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'811234567'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70[01]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'700123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([2-9]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3')])
