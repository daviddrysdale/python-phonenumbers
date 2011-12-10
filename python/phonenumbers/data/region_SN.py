"""Auto-generated file, do not edit by hand. SN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SN = PhoneMetadata(id='SN', country_code=221, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[37]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='3(?:010|3(?:8[1-9]|9[2-9]))\\d{5}', possible_number_pattern='\\d{9}', example_number='301012345'),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:0[1256]0|6(?:1[23]|2[89]|3[3489]|4[6-9]|5[1-9]|6[3-9]|7[45]|8[3-8])|7(?:01|[12-79]\\d|8[0139]))\\d{5}', possible_number_pattern='\\d{9}', example_number='701012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='33301\\d{4}', possible_number_pattern='\\d{9}', example_number='333011234'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4')])
