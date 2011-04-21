"""Auto-generated file, do not edit by hand. KY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KY = PhoneMetadata(id='KY', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[3589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'345(?:2(?:22|44)|444|6(?:23|38|40)|7(?:6[6-9]|77)|8(?:00|1[45]|25|4[89]|88)|9(?:14|4[035-9]))\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'3452221234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'345(?:32[3-79]|5(?:1[467]|2[5-7]|4[5-9])|9(?:1[679]|2[4-9]|3[89]))\d{4}', possible_number_pattern=u'\d{10}', example_number=u'3453231234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002345678'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}|345976\d{4}', possible_number_pattern=u'\d{10}', example_number=u'9002345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='345')
