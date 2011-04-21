"""Auto-generated file, do not edit by hand. AG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AG = PhoneMetadata(id='AG', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'268(?:4(?:6[0-38]|84)|56[0-2])\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'2684601234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'268(?:464|7(?:2[0-9]|64|7[0-689]|8[02-68]))\d{4}', possible_number_pattern=u'\d{10}', example_number=u'2684641234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'26848[01]\d{4}', possible_number_pattern=u'\d{10}', example_number=u'2684801234'),
    pager=PhoneNumberDesc(national_number_pattern=u'26840[69]\d{4}', possible_number_pattern=u'\d{10}', example_number=u'2684061234'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='268')
