"""Auto-generated file, do not edit by hand. KW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KW = PhoneMetadata(id='KW', country_code=965, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[12569]\\d{6,7}', possible_length=(7, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:18\\d|2(?:[23]\\d{2}|4(?:[1-35-9]\\d|44)|5(?:0[034]|[2-46]\\d|5[1-3]|7[1-7])))\\d{4}', example_number='22345678', possible_length=(7, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5(?:[05]\\d{2}|1[0-7]\\d|2(?:22|5[25])|6[56]\\d)|6(?:0[034679]\\d|222|5[015-9]\\d|6\\d{2}|7(?:0[013-9]|[67]\\d)|9(?:[069]\\d|3[039]))|9(?:0[09]\\d|22\\d|4[01479]\\d|55\\d|6[0679]\\d|7(?:02|[1-9]\\d)|8[057-9]\\d|9\\d{2}))\\d{4}', example_number='50012345', possible_length=(8,)),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['[16]|2(?:[0-35-9]|4[0-35-9])|52[25]|9[024-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['244|5(?:[015]|6[56])'])],
    mobile_number_portable_region=True)
