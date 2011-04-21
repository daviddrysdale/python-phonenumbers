"""Auto-generated file, do not edit by hand. KI metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KI = PhoneMetadata(id='KI', country_code=686, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-689]\d{4}', possible_number_pattern=u'\d{5}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:[234]\d|50|8[1-5])\d{3}', possible_number_pattern=u'\d{5}', example_number=u'31234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[69]\d{4}', possible_number_pattern=u'\d{5}', example_number=u'61234'),
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
    number_format=[NumberFormat(pattern='(\d{5})', format=u'\\1', national_prefix_formatting_rule=u'0\\1')])
