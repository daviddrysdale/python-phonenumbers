"""Auto-generated file, do not edit by hand. AN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AN = PhoneMetadata(id='AN', country_code=599, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13-79]\d{6,7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:318|5(?:25|4\d|8[239])|7(?:1[578]|50)|9(?:[48]\d{2}|50\d|7(?:2[0-2]|[34]\d|6[35-7]|77)))\d{4}|416[0239]\d{3}', possible_number_pattern=u'\d{7,8}', example_number=u'7151234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:318|5(?:1[01]|2[0-7]|5\d|8[016-8])|7(?:0[01]|[89]\d)|9(?:5(?:[1246]\d|3[01])|6(?:[1679]\d|3[01])))\d{4}|416[15-8]\d{3}', possible_number_pattern=u'\d{7,8}', example_number=u'3181234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'(?:10|69)\d{5}', possible_number_pattern=u'\d{7,8}', example_number=u'1011234'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[13-7]']),
        NumberFormat(pattern='(9)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'])])
