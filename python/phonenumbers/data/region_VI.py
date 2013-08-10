"""Auto-generated file, do not edit by hand. VI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VI = PhoneMetadata(id='VI', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[3589]\\d{9}', possible_number_pattern='\\d{7}(?:\\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern='340(?:2(?:01|2[067]|36|44|77)|3(?:32|44)|4(?:4[38]|7[34])|5(?:1[34]|55)|6(?:26|4[23]|9[023])|7(?:[17]\\d|27)|884|998)\\d{4}', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='3406421234'),
    mobile=PhoneNumberDesc(national_number_pattern='340(?:2(?:01|2[067]|36|44|77)|3(?:32|44)|4(?:4[38]|7[34])|5(?:1[34]|55)|6(?:26|4[23]|9[023])|7(?:[17]\\d|27)|884|998)\\d{4}', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='3406421234'),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|55|66|77|88)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='8002345678'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='9002345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='5(?:00|33|44)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='5002345678'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='911', possible_number_pattern='\\d{3}', example_number='911'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='1',
    national_prefix_for_parsing='1',
    leading_digits='340')
