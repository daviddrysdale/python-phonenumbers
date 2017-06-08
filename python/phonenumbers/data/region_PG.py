"""Auto-generated file, do not edit by hand. PG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PG = PhoneMetadata(id='PG', country_code=675, international_prefix='140[1-3]|00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{6,7}', possible_length=(7, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3[0-2]\\d|4[257]\\d|5[34]\\d|64[1-9]|77(?:[0-24]\\d|30)|85[02-46-9]|9[78]\\d)\\d{4}', example_number='3123456', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:[0-689]\\d|75)\\d{5}', example_number='70123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180\\d{4}', example_number='1801234', possible_length=(7,)),
    voip=PhoneNumberDesc(national_number_pattern='2(?:0[0-47]|7[568])\\d{4}', example_number='2751234', possible_length=(7,)),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[13-689]|27']),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['20|7'])])
