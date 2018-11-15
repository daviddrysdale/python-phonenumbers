"""Auto-generated file, do not edit by hand. KE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KE = PhoneMetadata(id='KE', country_code=254, international_prefix='000',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:(?:2|80)0\\d?|[4-7]\\d\\d|900)\\d{6}|[4-6]\\d{6,7}', possible_length=(7, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='20\\d{6,7}|(?:4[0-6]|5\\d|6[0-24-9])\\d{7}|(?:4[0245]|6[014-9])\\d{6}|5[1-79]\\d{5,6}|(?:4[245]|6[01457-9])\\d{5}', example_number='202012345', possible_length=(7, 8, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='7\\d{8}', example_number='712123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800[24-8]\\d{5,6}', example_number='800223456', possible_length=(9, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[02-9]\\d{5}', example_number='900223456', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{5,7})', format='\\1 \\2', leading_digits_pattern=['[24-6]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
