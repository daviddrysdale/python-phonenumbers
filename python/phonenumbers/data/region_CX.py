"""Auto-generated file, do not edit by hand. CX metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CX = PhoneMetadata(id='CX', country_code=61, international_prefix='(?:14(?:1[14]|34|4[17]|[56]6|7[47]|88))?001[14-689]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1458]\\d{5,9}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='89164\\d{4}', possible_number_pattern='\\d{8,9}', example_number='891641234'),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[0-2]\\d|3[0-57-9]|4[47-9]|5[0-37-9]|6[6-9]|7[07-9]|8[7-9])\\d{6}', possible_number_pattern='\\d{9}', example_number='412345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:80(?:0\\d{2})?|3(?:00\\d{2})?)\\d{4}', possible_number_pattern='\\d{6,10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0126]\\d{6}', possible_number_pattern='\\d{10}', example_number='1900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='500\\d{6}', possible_number_pattern='\\d{9}', example_number='500123456'),
    voip=PhoneNumberDesc(national_number_pattern='550\\d{6}', possible_number_pattern='\\d{9}', example_number='550123456'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='000|112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0')
