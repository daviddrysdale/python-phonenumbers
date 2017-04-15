"""Auto-generated file, do not edit by hand. TD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TD = PhoneMetadata(id='TD', country_code=235, international_prefix='00|16',
    general_desc=PhoneNumberDesc(national_number_pattern='[2679]\\d{7}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='22(?:[3789]0|5[0-5]|6[89])\\d{4}', example_number='22501234', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:6[023568]\\d|77\\d|9\\d{2})\\d{5}', example_number='63012345', possible_length=(8,)),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4')])
