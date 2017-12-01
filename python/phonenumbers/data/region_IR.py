"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=98, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-8]\\d{5,9}|9(?:[0-4]\\d{8}|9\\d{8})', possible_length=(6, 7, 10), possible_length_local_only=(4, 5, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:(?:1[137]|2[13-68]|3[1458]|4[145]|5[1468]|6[16]|7[1467]|8[13467])(?:\\d{8}|(?:[16]|[289]\\d?)\\d{3}))|94(?:000|11[0-7]|2\\d{2}|30[01]|440)\\d{5}', example_number='2123456789', possible_length=(6, 7, 10), possible_length_local_only=(4, 5, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:0(?:[1-3]\\d{2}|44\\d)|[13]\\d{3}|2[0-2]\\d{2}|9(?:[01]\\d{2}|44\\d|810|9(?:0[013]|1[134]|21|9[89])))\\d{5}', example_number='9123456789', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='(?:[2-6]0\\d|993)\\d{7}', example_number='9932123456', possible_length=(10,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:9411[1-7]|94440)\\d{5}', example_number='9411110000', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{4,5})', format='\\1 \\2', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4,5})', format='\\1', leading_digits_pattern=['96'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule='0\\1')])
