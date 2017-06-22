"""Auto-generated file, do not edit by hand. GI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GI = PhoneMetadata(id='GI', country_code=350, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[256]\\d{7}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:00\\d{2}|1(?:6[24-7]\\d|90[0-2])|2(?:2[2457]\\d|50[0-2]))\\d{3}', example_number='20012345', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[46-8]|62)\\d{6}', example_number='57123456', possible_length=(8,)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['2'])])
