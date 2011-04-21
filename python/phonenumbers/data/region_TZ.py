"""Auto-generated file, do not edit by hand. TZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TZ = PhoneMetadata(id='TZ', country_code=255, international_prefix='00[056]',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{9}', possible_number_pattern=u'\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[2-8]\d{7}', possible_number_pattern=u'\d{7,9}', example_number=u'222345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:6[158]|7[1-9])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80[08]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{7}', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:40|6[01])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'840123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'41\d{7}', possible_number_pattern=u'\d{9}', example_number=u'412345678'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([24]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[24]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([67]\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[67]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\d{2})(\d{2})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1')])
