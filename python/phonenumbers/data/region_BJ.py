"""Auto-generated file, do not edit by hand. BJ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BJ = PhoneMetadata(id='BJ', country_code=229, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2689]\d{7}|7\d{3}', possible_number_pattern=u'\d{4,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:02|1[037]|2[45]|3[68])\d{5}', possible_number_pattern=u'\d{8}', example_number=u'20211234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'66\d{6}|9(?:0[069]|[35][0-2457-9]|[6-8]\d)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'90011234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'7[3-5]\d{2}', possible_number_pattern=u'\d{4}', example_number=u'7312'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'857[58]\d{4}', possible_number_pattern=u'\d{8}', example_number=u'85751234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
