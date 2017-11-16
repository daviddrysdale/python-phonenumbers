"""Auto-generated file, do not edit by hand. MR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MR = PhoneMetadata(id='MR', country_code=222, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-48]\\d{7}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='25[08]\\d{5}|35\\d{6}|45[1-7]\\d{5}', example_number='35123456', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='[234][0-46-9]\\d{6}', example_number='22123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', example_number='80012345', possible_length=(8,)),
    number_format=[NumberFormat(pattern='([2-48]\\d)(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[2-48]'])])
