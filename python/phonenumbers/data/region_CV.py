"""Auto-generated file, do not edit by hand. CV metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CV = PhoneMetadata(id='CV', country_code=238, international_prefix='0',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[259]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:2[1-7]|3[0-8]|4[12]|5[1256]|6\d|7[1-3]|8[1-5])\d{4}', possible_number_pattern=u'\d{7}', example_number=u'2211234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:9\d|59)\d{5}', possible_number_pattern=u'\d{7}', example_number=u'9911234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3')])
