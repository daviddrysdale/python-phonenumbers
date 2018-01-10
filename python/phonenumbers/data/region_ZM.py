"""Auto-generated file, do not edit by hand. ZM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZM = PhoneMetadata(id='ZM', country_code=260, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[289]\\d{8}', possible_length=(9,), possible_length_local_only=(6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='21[1-8]\\d{6}', example_number='211234567', possible_length=(9,), possible_length_local_only=(6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='9[4-9]\\d{7}', example_number='955123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})', format='\\1 \\2', national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='([1-8])(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='([29]\\d)(\\d{7})', format='\\1 \\2', leading_digits_pattern=['[29]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(800)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['800'], national_prefix_formatting_rule='0\\1')])
