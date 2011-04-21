"""Auto-generated file, do not edit by hand. SJ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SJ = PhoneMetadata(id='SJ', country_code=47, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'0\d{4}|[4789]\d{7}', possible_number_pattern=u'\d{5}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'79\d{6}', possible_number_pattern=u'\d{8}', example_number=u'79123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:4[015-8]|9\d)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'41234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80[01]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'82[09]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'82012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'810(?:0[0-6]|[2-8]\d)\d{3}', possible_number_pattern=u'\d{8}', example_number=u'81021234'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'880\d{5}', possible_number_pattern=u'\d{8}', example_number=u'88012345'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'0\d{4}|81(?:0(?:0[7-9]|1\d)|5\d{2})\d{3}', possible_number_pattern=u'\d{5}(?:\d{3})?', example_number=u'01234'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    leading_zero_possible=True)
