"""Auto-generated file, do not edit by hand. MM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MM = PhoneMetadata(id='MM', country_code=95, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{5,8}|8\\d{5,9}|9(?:[279]\\d{0,2}|5|[34]\\d{1,2}|6(?:\\d{1,2})?|8(?:\\d{2})?)\\d{6}', possible_length=(6, 7, 8, 9, 10), possible_length_local_only=(5,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1(?:2\\d{1,2}|[35]\\d|4(?:\\d|2[2-469]|39|6[25]|70)|6\\d?|[89][0-6]\\d)\\d{4}|2(?:2(?:000\\d{3}|\\d{4})|3\\d{4}|4(?:0\\d{5}|2[246]\\d{4}|39\\d{4}|62\\d{4}|70\\d{4}|\\d{4})|5(?:1\\d{3,6}|[02-9]\\d{3,5})|[6-9]\\d{4})|4(?:2(?:[25-8]|4(?:80)?)|3(?:2(?:02)?|[36]|4(?:70)?|56?)|[46][2-6]|5(?:[35]|4(?:70)?))\\d{4}|5(?:2(?:2(?:\\d{1,2})?|[35-8]|4(?:70)?)|3[2-68]|4(?:21?|4(?:70)?|[5-8])|5[23]|6[2-4]|7(?:[235-8]|4(?:80)?)|8(?:[25-7]|4(?:70)?)|9(?:[235-7]|4(?:70)?))\\d{4}|6(?:0[23]|1(?:2(?:0|4\\d)?|[356])|2[2-6]|3(?:[25-6]|4(?:70)?)|4(?:2(?:4\\d)?|[3-6])|5[2-4]|6[2-8]|7(?:[2367]|4(?:\\d|39|[67]0)|5\\d?|8[145]\\d)|8[245]|9(?:20?|4))\\d{4}|7(?:[04](?:[25-8]|4(?:70)?)|1(?:20?|[35-7]|4(?:70)?)|22|3[2-4]|5(?:[235-7]|4(?:70)?))\\d{4}|8(?:1(?:2\\d{1,2}|[35689]\\d|4(?:70)?\\d)|2(?:2\\d|3(?:\\d|20)|[4-8]\\d)|3(?:2|4(?:70)?)\\d|4[24-7]\\d|5[245]\\d|6[23]\\d)\\d{3}', example_number='1234567', possible_length=(6, 7, 8, 9), possible_length_local_only=(5,)),
    mobile=PhoneNumberDesc(national_number_pattern='17[01]\\d{4}|9(?:2(?:[0-4]|5\\d{2}|6[0-5]\\d)|3(?:[0-36]|4[069])\\d|4(?:0[0-4]\\d|[1379]\\d|2\\d{2}|4[0-589]\\d|5\\d{2}|88)|5[0-6]|6(?:1\\d|9\\d{2}|\\d)|7(?:3|5[0-2]|[6-9]\\d)\\d|8(?:\\d|9\\d{2})|9(?:1\\d|[5-7]\\d{2}|[089]))\\d{5}', example_number='92123456', possible_length=(7, 8, 9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='80080[01][1-9]\\d{3}', example_number='8008001234', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='(?:1(?:333|468)|2468)\\d{4}', example_number='13331234', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['1|2[245]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(2)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['251'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['16|2'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['4(?:[25]|3[24])|5[247-9]4|6[37]|7[0145]|8[13]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[4-8]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9)(\\d{3})(\\d{4,6})', format='\\1 \\2 \\3', leading_digits_pattern=['9(?:2[0-4]|[35-9]|4[137-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9)([34]\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['9(?:3[0-36]|4[0-57-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9)(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['92[56]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9)(\\d{3})(\\d{3})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['93'], national_prefix_formatting_rule='0\\1')])
