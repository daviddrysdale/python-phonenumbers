"""Auto-generated file, do not edit by hand. BI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BI = PhoneMetadata(id='BI', country_code=257, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[267]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='22(?:2[0-7]|[3-5]0)\\d{4}', possible_number_pattern='\\d{8}', example_number='22201234'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[26]9|7[14-9])\\d{6}', possible_number_pattern='\\d{8}', example_number='79561234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4')])
