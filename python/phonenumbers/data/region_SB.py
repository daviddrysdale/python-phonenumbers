"""Auto-generated file, do not edit by hand. SB metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SB = PhoneMetadata(id='SB', country_code=677, international_prefix='0[01]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{4,6}', possible_length=(5, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[4-79]|[23]\\d|4[0-2]|5[03]|6[0-37])\\d{3}', example_number='40123', possible_length=(5,)),
    mobile=PhoneNumberDesc(national_number_pattern='48\\d{3}|7(?:30|[46-8]\\d|5[025-9]|9[0-5])\\d{4}|8[4-9]\\d{5}|9(?:1[2-9]|2[013-9]|3[0-2]|[46]\\d|5[0-46-9]|7[0-689]|8[0-79]|9[0-8])\\d{4}', example_number='7421234', possible_length=(5, 7)),
    toll_free=PhoneNumberDesc(national_number_pattern='1[38]\\d{3}', example_number='18123', possible_length=(5,)),
    voip=PhoneNumberDesc(national_number_pattern='5[12]\\d{3}', example_number='51123', possible_length=(5,)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['[7-9]'])])
