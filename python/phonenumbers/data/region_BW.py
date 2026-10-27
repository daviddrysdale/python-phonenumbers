"""Auto-generated file, do not edit by hand. BW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BW = PhoneMetadata(id='BW', country_code=267, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='90\\d{5}|(?:0800|[2-6]|(?:7|800)\\d)\\d{6}', possible_length=(7, 8, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:1[01]|31|[469]\\d|5[0-2]|7[5-7]|89)|3(?:[15-79]\\d|2[1-5]|45|8[0-5])|4(?:[38]0|42|51|[679]\\d)|5(?:[056][01]|1[23]|2[034]|[347-9]\\d)|6(?:0[01]|[258]\\d|[34]0|6[03]))\\d{4}', example_number='2401234', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:[1-8]\\d{3}|9(?:(?:[03]\\d|2[0-7])\\d|1(?:0[13-9]|1[0-35-9]|2\\d|3[0-8])))\\d{3}', example_number='71123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='(?:0800|800\\d)\\d{6}', example_number='0800012345', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{5}', example_number='9012345', possible_length=(7,)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['90']),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[2-6]']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['7']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['8'])])
