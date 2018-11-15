"""Auto-generated file, do not edit by hand. NG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NG = PhoneMetadata(id='NG', country_code=234, international_prefix='009',
    general_desc=PhoneNumberDesc(national_number_pattern='[78]\\d{10,13}|[7-9]\\d{9}|[1-9]\\d{7}|[124-7]\\d{6}', possible_length=(7, 8, 10, 11, 12, 13, 14), possible_length_local_only=(5, 6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:(?:[1-356]\\d|4[02-8]|7[0-79]|8[2-9])\\d|9(?:0[3-9]|[1-9]\\d))\\d{5}|(?:[12]\\d|4[147]|5[14579]|6[1578]|7[0-3578])\\d{5}', example_number='18040123', possible_length=(7, 8), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:1(?:(?:7[34]|95)\\d|8(?:04|[124579]\\d|8[0-3]))|287[0-7]|3(?:18[1-8]|88[0-7]|9(?:6[1-5]|8[5-9]))|4(?:[28]8[0-2]|6(?:7[1-9]|8[02-47]))|5(?:2(?:7[7-9]|8\\d)|38[1-79]|48[0-7]|68[4-7])|6(?:2(?:7[7-9]|8\\d)|4(?:3[7-9]|[68][129]|7[04-69]|9[1-8])|58[0-2]|98[7-9])|7(?:0(?:[1-689]\\d|7[0-3])\\d\\d|38[0-7]|69[1-8]|78[2-4])|8(?:(?:0(?:1[01]|[2-9]\\d)|1(?:[0-8]\\d|9[01]))\\d\\d|28[3-9]|38[0-2]|4(?:2[12]|3[147-9]|5[346]|7[4-9]|8[014-689]|90)|58[1-8]|78[2-9]|88[5-7])|9(?:0[235-9]\\d\\d|8[07])\\d)\\d{4}', example_number='8021234567', possible_length=(8, 10), possible_length_local_only=(6, 7)),
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
