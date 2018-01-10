"""Auto-generated file, do not edit by hand. CC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CC = PhoneMetadata(id='CC', country_code=61, international_prefix='(?:14(?:1[14]|34|4[17]|[56]6|7[47]|88))?001[14-689]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1458]\\d{5,9}', possible_length=(6, 7, 8, 9, 10), possible_length_local_only=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='8(?:51(?:0(?:02|31|60)|118)|91(?:0(?:1[0-2]|29)|1(?:[28]2|50|79)|2(?:10|64)|3(?:08|22|68)|4[29]8|62\\d|70[23]|959))\\d{3}', example_number='891621234', possible_length=(9,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='14(?:5\\d|71)\\d{5}|4(?:[0-3]\\d|4[047-9]|5[0-25-9]|6[6-9]|7[02-9]|8[12547-9]|9[017-9])\\d{6}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='19(?:0[0126]\\d|[679])\\d{5}', example_number='1900123456', possible_length=(8, 10)),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{2})?\\d{4}', example_number='1300123456', possible_length=(6, 10)),
    personal_number=PhoneNumberDesc(national_number_pattern='500\\d{6}', example_number='500123456', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='550\\d{6}', example_number='550123456', possible_length=(9,)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0')
