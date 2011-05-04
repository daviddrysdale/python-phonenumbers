"""Auto-generated file, do not edit by hand. LY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LY = PhoneMetadata(id='LY', country_code=218, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[25679]\d{8}', possible_number_pattern=u'\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2[1345]|5[1347]|6[123479]|71)\d{7}', possible_number_pattern=u'\d{7,9}', example_number=u'212345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9[1-6]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([25679]\d)(\d{7})', format=u'\\1-\\2', national_prefix_formatting_rule=u'0\\1')])
