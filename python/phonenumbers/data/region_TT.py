"""Auto-generated file, do not edit by hand. TT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TT = PhoneMetadata(id='TT', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'868(?:2(?:01|2[1-4])|6(?:07|1[4-6]|2[1-9]|[3-6]\d|7[0-79]|9[0-8])|82[12])\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'8682211234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'868(?:29\d|3(?:0[1-9]|1[02-9]|[2-9]\d)|4(?:[679]\d|8[0-4])|6(?:20|78|8\d)|7(?:1[02-9]|[2-9]\d))\d{4}', possible_number_pattern=u'\d{10}', example_number=u'8682911234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002345678'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='868')
