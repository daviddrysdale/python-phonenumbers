"""Auto-generated file, do not edit by hand. NG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NG = PhoneMetadata(id='NG', country_code=234, international_prefix='009',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:20)?((?:[124-7]|9\\d{3})\\d{6}|[1-9]\\d{7}|[78]\\d{9,13})|(?:[124-7]|9\\d{3})\\d{6}|[1-9]\\d{7}|[78]\\d{9,13}', possible_length=(7, 8, 10, 11, 12, 13, 14), possible_length_local_only=(5, 6, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:20)?((?:(?:[1-356]\\d|4[02-8]|8[2-9])\\d|9(?:0[3-9]|[1-9]\\d))\\d{5}|7(?:0(?:[013-689]\\d|2[0-24-9])\\d{3,4}|[1-79]\\d{6})|(?:[12]\\d|4[147]|5[14579]|6[1578]|7[1-3578])\\d{5})|(?:(?:[1-356]\\d|4[02-8]|8[2-9])\\d|9(?:0[3-9]|[1-9]\\d))\\d{5}|7(?:0(?:[013-689]\\d|2[0-24-9])\\d{3,4}|[1-79]\\d{6})|(?:[12]\\d|4[147]|5[14579]|6[1578]|7[1-3578])\\d{5}', example_number='18040123', possible_length=(7, 8, 10), possible_length_local_only=(5, 6, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:702[0-24-9]|819[01])\\d{6}|(?:70[13-689]|8(?:0[1-9]|1[0-8])|9(?:0[1-9]|1[1-356]))\\d{7}', example_number='8021234567', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7,11}', example_number='80017591759', possible_length=(10, 11, 12, 13, 14)),
    uan=PhoneNumberDesc(national_number_pattern='700\\d{7,11}', example_number='7001234567', possible_length=(10, 11, 12, 13, 14)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['78'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[12]|9(?:0[3-9]|[1-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[3-7]|8[2-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[7-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4,5})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{5})(\\d{5,6})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
