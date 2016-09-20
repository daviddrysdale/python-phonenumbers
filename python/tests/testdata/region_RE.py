"""Auto-generated file, do not edit by hand. RE metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RE = PhoneMetadata(id='RE', country_code=262, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[268]\\d{8}', possible_number_pattern='\\d{9}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='262\\d{6}', possible_number_pattern='\\d{9}', example_number='262161234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:9[23]|47)\\d{6}', possible_number_pattern='\\d{9}', example_number='692123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', possible_number_pattern='\\d{9}', example_number='801234567', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='8(?:1[01]|2[0156]|84|9[0-37-9])\\d{6}', possible_number_pattern='\\d{9}', example_number='810123456', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([268]\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', national_prefix_formatting_rule='0\\1')],
    leading_digits='262|6(?:9[23]|47)|8')
