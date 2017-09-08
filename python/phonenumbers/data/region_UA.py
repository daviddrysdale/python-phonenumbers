"""Auto-generated file, do not edit by hand. UA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UA = PhoneMetadata(id='UA', country_code=380, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-9]\\d{8}', possible_length=(9,), possible_length_local_only=(5, 6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3[1-8]|4[13-8]|5[1-7]|6[12459])\\d{7}', example_number='311234567', possible_length=(9,), possible_length_local_only=(5, 6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:39|50|6[36-8]|7[1-3]|9[1-9])\\d{7}', example_number='391234567', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[2-49]\\d{5}', example_number='900212345', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='89[1-579]\\d{6}', example_number='891234567', possible_length=(9,)),
    preferred_international_prefix='0~0',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([3-9]\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[38]9|4(?:[45][0-5]|87)|5(?:0|[67][37])|6[36-8]|7|9[1-9]', '[38]9|4(?:[45][0-5]|87)|5(?:0|6(?:3[14-7]|7)|7[37])|6[36-8]|7|9[1-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([3-689]\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['(?:3[1-8]|4[136-8])2|5(?:[12457]2|6[24])|6(?:[12][29]|[49]2|5[24])|8[0-8]|90', '3(?:[1-46-8]2[013-9]|52)|4(?:[1378]2|62[013-9])|5(?:[12457]2|6[24])|6(?:[12][29]|[49]2|5[24])|8[0-8]|90'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([3-6]\\d{3})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['3(?:[1-46-8]|5[013-9])|4(?:[137][013-9]|[45][6-9]|6|8[4-6])|5(?:[1245][013-9]|3|6[0135689]|7[4-6])|6(?:[12][13-8]|[49][013-9]|5[0135-9])', '3(?:[1-46-8](?:[013-9]|22)|5[013-9])|4(?:[137][013-9]|[45][6-9]|6(?:[013-9]|22)|8[4-6])|5(?:[1245][013-9]|3|6(?:[015689]|3[02389])|7[4-6])|6(?:[12][13-8]|[49][013-9]|5[0135-9])'], national_prefix_formatting_rule='0\\1')])
