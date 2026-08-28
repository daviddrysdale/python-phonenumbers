"""Auto-generated file, do not edit by hand. GM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GM = PhoneMetadata(id='GM', country_code=220, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[48]\\d{8}|[2-9]\\d{6}', possible_length=(7, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:4(?:[23]\\d\\d|4(?:1[024679]|(?:4(?:[237-9]\\d|4[14-9])|8[0-389]\\d)\\d|5(?:5(?:3\\d|4[0-7])|[67]\\d\\d)))|5(?:5(?:3\\d|4[0-7])|6[67]\\d|7(?:1[04]|2[035]|3[58]|48))|8[0-389]\\d\\d)\\d{3}|44[6-9]\\d{4}', example_number='5661234', possible_length=(7, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:(?:[23679]\\d|4[015]|8(?:(?:3[35]|6[68]|99)\\d|7(?:[27]\\d|4[015])))\\d|5(?:[0-489]\\d|56))\\d{4}|8[4-7]\\d{5}', example_number='3012345', possible_length=(7, 9)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[235-9]|4(?:[0-35]|4[16-9])']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[48]'])])
