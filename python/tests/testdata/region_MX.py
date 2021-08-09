"""Auto-generated file, do not edit by hand. MX metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MX = PhoneMetadata(id='MX', country_code=52, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{9,10}', possible_length=(10, 11), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-9]\\d{9}', example_number='2123456789', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='1\\d{10}', example_number='11234567890', possible_length=(11,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', example_number='8001234567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', example_number='9001234567', possible_length=(10,)),
    national_prefix='01',
    national_prefix_for_parsing='01|04[45](\\d{10})',
    national_prefix_transform_rule='1\\1',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]00'], national_prefix_formatting_rule='01 \\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{5})', format='\\2 \\3', leading_digits_pattern=['901'], national_prefix_formatting_rule='01 \\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['33|55|81'], national_prefix_formatting_rule='01 \\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2467]|3[0-24-9]|5[0-46-9]|8[2-9]|9[1-9]'], national_prefix_formatting_rule='01 \\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d)(\\d{2})(\\d{4})(\\d{4})', format='045 \\2 \\3 \\4', leading_digits_pattern=['1(?:33|55|81)'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})(\\d{4})', format='045 \\2 \\3 \\4', leading_digits_pattern=['1(?:[124579]|3[0-24-9]|5[0-46-9]|8[02-9])'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True)],
    intl_number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]00']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{5})', format='\\2 \\3', leading_digits_pattern=['901']),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['33|55|81']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2467]|3[0-24-9]|5[0-46-9]|8[2-9]|9[1-9]']),
        NumberFormat(pattern='(\\d)(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1(?:33|55|81)']),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1(?:[124579]|3[0-24-9]|5[0-46-9]|8[02-9])'])])
