"""Auto-generated file, do not edit by hand. TG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TG = PhoneMetadata(id='TG', country_code=228, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[02-9]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2[2-7]|3[23]|44|55|66|77)\d{5}', possible_number_pattern=u'\d{7}', example_number=u'2212345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:0[1-9]|7[56]|8[1-7]|9\d)\d{5}', possible_number_pattern=u'\d{7}', example_number=u'0112345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3')],
    leading_zero_possible=True)
