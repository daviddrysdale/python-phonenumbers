"""Auto-generated file, do not edit by hand. GD metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GD = PhoneMetadata(id='GD', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[4589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'473(?:2(?:3[0-2]|69)|3(?:2[89]|86)|4(?:[06]8|3[5-9]|4[0-49]|5[5-79]|73|90)|63[68]|7(?:58|84)|938)\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'4732691234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'473(?:4(?:0[3-79]|1[04-9]|20|58)|53[3-8])\d{4}', possible_number_pattern=u'\d{10}', example_number=u'4734031234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='473')
