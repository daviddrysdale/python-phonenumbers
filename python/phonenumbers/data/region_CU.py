"""Auto-generated file, do not edit by hand. CU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CU = PhoneMetadata(id='CU', country_code=53, international_prefix='119',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-57]\\d{7}|[2-47]\\d{6}|[34]\\d{5}', possible_length=(6, 7, 8), possible_length_local_only=(4, 5)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[1-4]\\d{5,6}|3(?:1\\d{6}|[23]\\d{4,6})|4(?:[125]\\d{5,6}|[36]\\d{6}|[78]\\d{4,6})|7\\d{6,7}', example_number='71234567', possible_length=(6, 7, 8), possible_length_local_only=(4, 5)),
    mobile=PhoneNumberDesc(national_number_pattern='5\\d{7}', example_number='51234567', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{6,7})', format='\\1 \\2', leading_digits_pattern=['7'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{4,6})', format='\\1 \\2', leading_digits_pattern=['[2-4]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d)(\\d{7})', format='\\1 \\2', leading_digits_pattern=['5'], national_prefix_formatting_rule='0\\1')])
