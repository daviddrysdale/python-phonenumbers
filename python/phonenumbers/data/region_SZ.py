"""Auto-generated file, do not edit by hand. SZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SZ = PhoneMetadata(id='SZ', country_code=268, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[027]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:2(?:0[07]|[13]7|2[57])|3(?:0[34]|[1278]3|3[23]|[46][34])|(?:40[4-69]|67)|5(?:0[5-7]|1[6-9]|[23][78]|48|5[01]))\d{4}', possible_number_pattern=u'\d{8}', example_number=u'22171234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[6-8]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'76123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'0800\d{4}', possible_number_pattern=u'\d{8}', example_number=u'08001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'0800\d{4}', possible_number_pattern=u'\d{8}', example_number=u'08001234'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[027]'])],
    leading_zero_possible=True)
