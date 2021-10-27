"""Auto-generated file, do not edit by hand. TJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TJ = PhoneMetadata(id='TJ', country_code=992, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:00|[1-57-9]\\d)\\d{7}', possible_length=(9,), possible_length_local_only=(3, 5, 6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:1[3-5]|2[245]|3[12]|4[24-7]|5[25]|72)|4(?:46|74|87))\\d{6}', example_number='372123456', possible_length=(9,), possible_length_local_only=(3, 5, 6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='41[18]\\d{6}|(?:[034]0|1[01]|2[02]|5[05]|7[07]|8[08]|9\\d)\\d{7}', example_number='917123456', possible_length=(9,)),
    preferred_international_prefix='8~10',
    number_format=[NumberFormat(pattern='(\\d{6})(\\d)(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['331', '3317']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[34]7|91[78]']),
        NumberFormat(pattern='(\\d{4})(\\d)(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3[1-5]']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[0-57-9]'])])
