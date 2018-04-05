"""Auto-generated file, do not edit by hand. BE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BE = PhoneMetadata(id='BE', country_code=32, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7,8}', possible_length=(8, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[0-69]|[23][2-8]|4[23]|5\\d|6[013-57-9]|71|8[1-79]|9[2-4])\\d{6}|80[2-8]\\d{5}', example_number='12345678', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:56|6[0135-8]|[79]\\d|8[3-9])\\d{6}', example_number='470123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800[1-9]\\d{4}', example_number='80012345', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:70(?:2[0-57]|3[0457]|44|69|7[0579])|90(?:0[0-35-8]|1[36]|2[0-3568]|3[0135689]|4[2-68]|5[1-68]|6[0-378]|7[23568]|9[34679]))\\d{4}', example_number='90012345', possible_length=(8,)),
    uan=PhoneNumberDesc(national_number_pattern='78[0-7]\\d{5}', example_number='78102345', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['4[5-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[23]|4[23]|9[2-4]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[156]|7[018]|8(?:0[1-9]|[1-79])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['(?:80|9)0'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
