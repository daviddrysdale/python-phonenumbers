"""Auto-generated file, do not edit by hand. SL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SL = PhoneMetadata(id='SL', country_code=232, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-578]\d{7}', possible_number_pattern=u'\d{6,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[235]2[2-4][2-9]\d{4}', possible_number_pattern=u'\d{6,8}', example_number=u'22221234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:25|3[03]|44|5[056]|7[6-8]|88)[1-9]\d{5}', possible_number_pattern=u'\d{6,8}', example_number=u'25123456'),
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
    number_format=[NumberFormat(pattern='(\d{2})(\d{6})', format=u'\\1 \\2', national_prefix_formatting_rule=u'(0\\1)')])
