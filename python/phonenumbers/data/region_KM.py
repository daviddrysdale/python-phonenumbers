"""Auto-generated file, do not edit by hand. KM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KM = PhoneMetadata(id='KM', country_code=269, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[37]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'7(?:6[0-37-9]|7[0-57-9])\d{4}', possible_number_pattern=u'\d{7}', example_number=u'7712345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'3[23]\d{5}', possible_number_pattern=u'\d{7}', example_number=u'3212345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3')])
