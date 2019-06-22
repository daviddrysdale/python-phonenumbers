"""Auto-generated file, do not edit by hand. MN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MN = PhoneMetadata(id='MN', country_code=976, international_prefix='001',
    general_desc=PhoneNumberDesc(national_number_pattern='[12]\\d{7,9}|[57-9]\\d{7}', possible_length=(8, 9, 10), possible_length_local_only=(4, 5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[12](?:3[2-8]|4[2-68]|5[1-4689])\\d{6,7}|(?:11(?:3\\d|4[568])|(?:(?:21|5[0568])\\d|70[0-5])\\d)\\d{4}|[12]2(?:[1-3]\\d{5,6}|7\\d{6})', example_number='50123456', possible_length=(8, 9, 10), possible_length_local_only=(4, 5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:8(?:[05689]\\d|3[01])|9(?:[014-9]\\d|20|3[0-4]))\\d{5}', example_number='88123456', possible_length=(8,)),
    voip=PhoneNumberDesc(national_number_pattern='7(?:100|5(?:0[0579]|1[015]|[389]5|[57][57])|(?:6[0167]|7\\d|8[01])\\d)\\d{4}', example_number='75153456', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[12]1'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[57-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['[12]2[1-3]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['[12](?:27|3[2-8]|4[2-68]|5[1-4689])', '[12](?:27|3[2-8]|4[2-68]|5[1-4689])[0-3]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{4,5})', format='\\1 \\2', leading_digits_pattern=['[12]'], national_prefix_formatting_rule='0\\1')])
