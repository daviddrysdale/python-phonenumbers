"""Auto-generated file, do not edit by hand. SL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SL = PhoneMetadata(id='SL', country_code=232, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[2378]\\d|99)\\d{6}', possible_length=(8,), possible_length_local_only=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='22\\d{6}', example_number='22221234', possible_length=(8,), possible_length_local_only=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:25|3[0134]|7[5-9]|8[08]|99)\\d{6}', example_number='25123456', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['[237-9]'], national_prefix_formatting_rule='(0\\1)')])
