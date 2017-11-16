"""Auto-generated file, do not edit by hand. RU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RU = PhoneMetadata(id='RU', country_code=7, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='[347-9]\\d{9}', possible_length=(10,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:0[12]|4[1-35-79]|5[1-3]|65|8[1-58]|9[0145])|4(?:01|1[1356]|2[13467]|7[1-5]|8[1-7]|9[1-689])|8(?:1[1-8]|2[01]|3[13-6]|4[0-8]|5[15]|6[1-35-79]|7[1-37-9]))\\d{7}', example_number='3011234567', possible_length=(10,)),
    mobile=PhoneNumberDesc(national_number_pattern='9\\d{9}', example_number='9123456789', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80[04]\\d{7}', example_number='8001234567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='80[39]\\d{7}', example_number='8091234567', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='808\\d{7}', example_number='8081234567', possible_length=(10,)),
    preferred_international_prefix='8~10',
    national_prefix='8',
    national_prefix_for_parsing='8',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})', format='\\1-\\2-\\3', leading_digits_pattern=['[1-79]'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='([3489]\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2-\\3-\\4', leading_digits_pattern=['[3489]'], national_prefix_formatting_rule='8 (\\1)', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(7\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule='8 (\\1)', national_prefix_optional_when_formatting=True)],
    intl_number_format=[NumberFormat(pattern='([3489]\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2-\\3-\\4', leading_digits_pattern=['[3489]']),
        NumberFormat(pattern='(7\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7'])],
    main_country_for_code=True)
