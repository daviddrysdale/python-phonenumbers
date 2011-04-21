"""Auto-generated file, do not edit by hand. BN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BN = PhoneMetadata(id='BN', country_code=673, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-578]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2-5]\d{6}', possible_number_pattern=u'\d{7}', example_number=u'2345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[78]\d{6}', possible_number_pattern=u'\d{7}', example_number=u'7123456'),
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
    number_format=[NumberFormat(pattern='([2-578]\d{2})(\d{4})', format=u'\\1 \\2', national_prefix_formatting_rule=u'0\\1')])
