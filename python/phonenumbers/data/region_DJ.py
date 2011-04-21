"""Auto-generated file, do not edit by hand. DJ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DJ = PhoneMetadata(id='DJ', country_code=253, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-8]\d{5}', possible_number_pattern=u'\d{6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1[05]|[2-5]\d)\d{4}', possible_number_pattern=u'\d{6}', example_number=u'251234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[6-8]\d{5}', possible_number_pattern=u'\d{6}', example_number=u'601234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3')])
