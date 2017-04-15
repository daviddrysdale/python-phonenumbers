"""Auto-generated file, do not edit by hand. SG metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SG = PhoneMetadata(id='SG', country_code=65, international_prefix='0[0-3][0-9]',
    general_desc=PhoneNumberDesc(national_number_pattern='[13689]\\d{7,10}', possible_length=(8, 10, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[36]\\d{7}', example_number='31234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='[89]\\d{7}', example_number='81234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1?800\\d{7}', example_number='8001234567', possible_length=(10, 11)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900\\d{7}', example_number='19001234567', possible_length=(11,)),
    national_prefix_for_parsing='777777',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[369]|8[1-9]']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1[89]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['800'])])
