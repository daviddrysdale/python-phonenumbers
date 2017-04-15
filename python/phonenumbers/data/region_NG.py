"""Auto-generated file, do not edit by hand. NG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NG = PhoneMetadata(id='NG', country_code=234, international_prefix='009',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-6]\\d{5,8}|9\\d{5,9}|[78]\\d{5,13}', possible_length=(7, 8, 10, 11, 12, 13, 14), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[12]\\d{6,7}|9(?:0[3-9]|[1-9]\\d)\\d{5}|(?:3\\d|4[023568]|5[02368]|6[02-469]|7[4-69]|8[2-9])\\d{6}|(?:4[47]|5[14579]|6[1578]|7[0-357])\\d{5,6}|(?:78|41)\\d{5}', example_number='12345678', possible_length=(7, 8), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:1(?:7[34]\\d|8(?:04|[124579]\\d|8[0-3])|95\\d)|287[0-7]|3(?:18[1-8]|88[0-7]|9(?:8[5-9]|6[1-5]))|4(?:28[0-2]|6(?:7[1-9]|8[02-47])|88[0-2])|5(?:2(?:7[7-9]|8\\d)|38[1-79]|48[0-7]|68[4-7])|6(?:2(?:7[7-9]|8\\d)|4(?:3[7-9]|[68][129]|7[04-69]|9[1-8])|58[0-2]|98[7-9])|7(?:38[0-7]|69[1-8]|78[2-4])|8(?:28[3-9]|38[0-2]|4(?:2[12]|3[147-9]|5[346]|7[4-9]|8[014-689]|90)|58[1-8]|78[2-9]|88[5-7])|98[07]\\d)\\d{4}|(?:70(?:[1-689]\\d|7[0-3])|8(?:0(?:1[01]|[2-9]\\d)|1(?:[0-8]\\d|9[01]))|90[235-9]\\d)\\d{6}', example_number='8021234567', possible_length=(8, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7,11}', example_number='80017591759', possible_length=(10, 11, 12, 13, 14)),
    uan=PhoneNumberDesc(national_number_pattern='700\\d{7,11}', example_number='7001234567', possible_length=(10, 11, 12, 13, 14)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[12]|9(?:0[3-9]|[1-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[3-6]|7(?:[1-79]|0[1-9])|8[2-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['70|8[01]|90[235-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([78]00)(\\d{4})(\\d{4,5})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]00'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([78]00)(\\d{5})(\\d{5,6})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]00'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(78)(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['78'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
