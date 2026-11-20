"""Auto-generated file, do not edit by hand. BF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BF = PhoneMetadata(id='BF', country_code=226, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[024-7]\\d{7}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[045]\\d{6}', example_number='20491234', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:0[1-7]|4[4-6]|5[0-8]|[67]\\d)\\d{6}', example_number='70123456', possible_length=(8,)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[024-7]'])])
