"""Auto-generated file, do not edit by hand. AC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AC = PhoneMetadata(id='AC', country_code=247, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-7]\\d{3,5}', possible_number_pattern='\\d{4,6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[267]\\d|3[0-5]|4[4-69])\\d{2}', possible_number_pattern='\\d{4}', example_number='6889'),
    mobile=PhoneNumberDesc(national_number_pattern='5\\d{5}', possible_number_pattern='\\d{6}', example_number='501234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'))
