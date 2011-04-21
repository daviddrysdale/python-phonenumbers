"""Auto-generated file, do not edit by hand. VE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VE = PhoneMetadata(id='VE', country_code=58, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[24589]\d{9}', possible_number_pattern=u'\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:12|3[457-9]|[58][1-9]|[467]\d|9[1-6])|50[01])\d{7}', possible_number_pattern=u'\d{7,10}', example_number=u'2121234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'4(?:1[24-8]|2[46])\d{7}', possible_number_pattern=u'\d{10}', example_number=u'4121234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{7}', possible_number_pattern=u'\d{10}', example_number=u'8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{7}', possible_number_pattern=u'\d{10}', example_number=u'9001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'(1\d{2})|0',
    number_format=[NumberFormat(pattern='(\d{3})(\d{7})', format=u'\\1-\\2', national_prefix_formatting_rule=u'0\\1', domestic_carrier_code_formatting_rule=u'$CC \\1')])
