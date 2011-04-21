"""Auto-generated file, do not edit by hand. CA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CA = PhoneMetadata(id='CA', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{9}|3\d{6}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:04|26|[48]9|50)|3(?:06|43)|4(?:03|1[68]|38|5[06])|5(?:0[06]|1[49]|79|8[17])|6(?:0[04]|13|47)|7(?:0[059]|[18]0|78)|8(?:[06]7|19|)|90[25])[2-9]\d{6}|310\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'2042345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:2(?:04|26|[48]9|50)|3(?:06|43)|4(?:03|1[68]|38|5[06])|5(?:0[06]|1[49]|79|8[17])|6(?:0[04]|13|47)|7(?:0[059]|[18]0|78)|8(?:[06]7|19|)|90[25])[2-9]\d{6}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'2042345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}|310\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'8002123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1')
