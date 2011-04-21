"""Auto-generated file, do not edit by hand. BI metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BI = PhoneMetadata(id='BI', country_code=257, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[27]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'22(?:2[0-7]|[3-5]0)\d{4}', possible_number_pattern=u'\d{8}', example_number=u'22201234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:29\d|7(?:1[1-3]|[4-9]\d))\d{5}', possible_number_pattern=u'\d{8}', example_number=u'79561234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([27]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
