"""Auto-generated file, do not edit by hand. EG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EG = PhoneMetadata(id='EG', country_code=20, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{4,9}|[2456]\\d{8}|3\\d{7}|[89]\\d{8,9}', possible_length=(5, 8, 9, 10), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:3[23]\\d|5(?:[23]|9\\d))|2[2-4]\\d{2}|3\\d{2}|4(?:0[2-5]|[578][23]|64)\\d|5(?:0[2-7]|[57][23])\\d|6[24-689]3\\d|8(?:2[2-57]|4[26]|6[237]|8[2-4])\\d|9(?:2[27]|3[24]|52|6[2356]|7[2-4])\\d)\\d{5}|1[69]\\d{3}', example_number='234567890', possible_length=(5, 8, 9), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='1(?:0[0-269]|1[0-245]|2[0-278])\\d{7}', example_number='1001234567', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', example_number='8001234567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', example_number='9001234567', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{7,8})', format='\\1 \\2', leading_digits_pattern=['[23]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1[012]|[89]00'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{6,7})', format='\\1 \\2', leading_digits_pattern=['1[35]|[4-6]|[89][2-9]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
