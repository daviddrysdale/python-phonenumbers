"""Auto-generated file, do not edit by hand. PL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PL = PhoneMetadata(id='PL', country_code=48, international_prefix='0~0',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{8}', possible_number_pattern=u'\d{9}'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[01]|6[069]|7[289]|88)\d{7}', possible_number_pattern=u'\d{9}'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'70\d{7}', possible_number_pattern=u'\d{9}'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', national_prefix_formatting_rule=u'0\\1')])
