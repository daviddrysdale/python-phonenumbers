"""Auto-generated file, do not edit by hand. AO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AO = PhoneMetadata(id='AO', country_code=244, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[29]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2\d(?:[26-9]\d|\d[26-9])\d{5}', possible_number_pattern=u'\d{9}', example_number=u'222123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9[1-3]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'923123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{3})(\d{3})', format=u'\\1 \\2 \\3')])
