"""Auto-generated file, do not edit by hand. ER metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ER = PhoneMetadata(id='ER', country_code=291, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[178]\d{6}', possible_number_pattern=u'\d{6,7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'1(?:1[12568]|20|40|55|6[146])\d{4}|8\d{6}', possible_number_pattern=u'\d{6,7}', example_number=u'8370362'),
    mobile=PhoneNumberDesc(national_number_pattern=u'17[1-3]\d{4}|7\d{6}', possible_number_pattern=u'\d{7}', example_number=u'7123456'),
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
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', national_prefix_formatting_rule=u'0\\1')])
