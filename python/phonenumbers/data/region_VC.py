"""Auto-generated file, do not edit by hand. VC metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VC = PhoneMetadata(id='VC', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[5789]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'784(?:266|3(?:6[6-9]|7\d|8[0-24-6])|4(?:38|5[0-36-8]|8\d|9[01])|555|638|784)\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'7842661234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'784(?:4(?:3[0-24]|5[45]|9[2-5])|5(?:2[6-9]|3[0-3]|93))\d{4}', possible_number_pattern=u'\d{10}', example_number=u'7844301234'),
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
    leading_digits='784')
