"""Auto-generated file, do not edit by hand. SD metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SD = PhoneMetadata(id='SD', country_code=249, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1(?:[25]\\d|8[3567])\\d{6}', possible_number_pattern='\\d{9}', example_number='121231234'),
    mobile=PhoneNumberDesc(national_number_pattern='9[1259]\\d{7}', possible_number_pattern='\\d{9}', example_number='911231234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', national_prefix_formatting_rule=u'0\\1')])
