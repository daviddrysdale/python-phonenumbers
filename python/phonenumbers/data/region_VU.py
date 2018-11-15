"""Auto-generated file, do not edit by hand. VU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VU = PhoneMetadata(id='VU', country_code=678, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:(?:[23]|(?:[57]\\d|90)\\d)\\d|[48]8)\\d{3}', possible_length=(5, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:(?:2[02-9]|88)\\d|3(?:[5-7]\\d|8[0-8])|48[4-9])\\d\\d', example_number='22123', possible_length=(5,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5(?:[0-689]\\d|7[2-5])|7[013-7]\\d)\\d{4}', example_number='5912345', possible_length=(7,)),
    voip=PhoneNumberDesc(national_number_pattern='90[1-9]\\d{4}', example_number='9010123', possible_length=(7,)),
    uan=PhoneNumberDesc(national_number_pattern='(?:3[03]|900\\d)\\d{3}', example_number='30123', possible_length=(5, 7)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[579]'])])
