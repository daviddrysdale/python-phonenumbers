"""Auto-generated file, do not edit by hand. AR metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AR = PhoneMetadata(id='AR', country_code=54, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-3689]\\d{9,10}', possible_length=(6, 7, 8, 9, 10, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-3]\\d{5,9}', example_number='1234567890', possible_length=(6, 7, 8, 9, 10)),
    mobile=PhoneNumberDesc(national_number_pattern='9\\d{10}|[1-3]\\d{9}', example_number='9234567890', possible_length=(10, 11)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{8}', example_number='8034567890', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='6(0\\d|10)\\d{7}', example_number='6234567890', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0(?:(11|343|3715)15)?',
    national_prefix_transform_rule='9\\1',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['11'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{2})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['1[02-9]|[23]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{2})(\\d{4})(\\d{4})', format='\\2 15 \\3-\\4', leading_digits_pattern=['911'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{2})(\\d{4})', format='\\2 \\3-\\4', leading_digits_pattern=['9(?:1[02-9]|[23])'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0\\1 $CC'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[68]'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['11']),
        NumberFormat(pattern='(\\d{4})(\\d{2})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['1[02-9]|[23]']),
        NumberFormat(pattern='(\\d)(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['911']),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{2})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['9(?:1[02-9]|[23])']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[68]'])])
