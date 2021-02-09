"""Auto-generated file, do not edit by hand. CI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CI = PhoneMetadata(id='CI', country_code=225, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[02]\\d{9}|[02-9]\\d{7}', possible_length=(8, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:0[023]|[15]\\d{3}|7(?:2(?:0[23]|1[2357]|[23][45]|4[3-5])|3(?:06|1[69]|[2-6]7)))|3(?:0[06]|1[069]|[2-4][07]|5[09]|6[08]))\\d{5}|2(?:1[02357]|[23][045]|4[03-5])\\d{5}', example_number='21234567', possible_length=(8, 10)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:(?:0(?:[15]\\d\\d|7(?:[04-8][7-9]|9[78]))|[457]\\d|6[014-9]|8[4-9]|9[4-8])\\d\\d|2[0-3]80)\\d{4}|0[1-9]\\d{6}', example_number='01234567', possible_length=(8, 10)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[03-9]|2(?:[02-4]|1[023578])', '[03-9]|2(?:[02-4]|1(?:[02357]|80))']),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d)(\\d{5})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['2']),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['0'])])
