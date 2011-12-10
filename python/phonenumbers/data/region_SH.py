"""Auto-generated file, do not edit by hand. SH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SH = PhoneMetadata(id='SH', country_code=290, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{3}', possible_number_pattern='\\d{4}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[2-468]\\d|7[01])\\d{2}', possible_number_pattern='\\d{4}', example_number='2158'),
    mobile=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:[59]\\d|7[2-9])\\d{2}', possible_number_pattern='\\d{4}', example_number='5012'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='9(?:11|99)', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'))
