"""Auto-generated file, do not edit by hand. SV metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SV = PhoneMetadata(id='SV', country_code=503, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[27]\d{7}|[89]\d{6}(?:\d{4})?', possible_number_pattern=u'\d{7,8}|\d{11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[1-6]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'21234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7\d{7}', possible_number_pattern=u'\d{8}', example_number=u'70123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{4}(?:\d{4})?', possible_number_pattern=u'\d{7}(?:\d{4})?', example_number=u'8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{4}(?:\d{4})?', possible_number_pattern=u'\d{7}(?:\d{4})?', example_number=u'9001234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[27]']),
        NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[89]']),
        NumberFormat(pattern='(\d{3})(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'])])
