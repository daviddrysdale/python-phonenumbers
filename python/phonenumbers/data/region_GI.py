"""Auto-generated file, do not edit by hand. GI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GI = PhoneMetadata(id='GI', country_code=350, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[25]\\d\\d|606)\\d{5}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='21(?:6[24-7]\\d|90[0-2])\\d{3}|2(?:00|2[25])\\d{5}', example_number='20012345', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[146-8]\\d|606)\\d{5}', example_number='57123456', possible_length=(8,)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['2'])],
    mobile_number_portable_region=True)
