"""Auto-generated file, do not edit by hand. NI metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NI = PhoneMetadata(id='NI', country_code=505, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[128]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2\d{7}', possible_number_pattern=u'\d{8}', example_number=u'21234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'8\d{7}', possible_number_pattern=u'\d{8}', example_number=u'81234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1800\d{4}', possible_number_pattern=u'\d{8}', example_number=u'18001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2')])
