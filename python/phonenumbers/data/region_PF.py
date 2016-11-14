"""Auto-generated file, do not edit by hand. PF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PF = PhoneMetadata(id='PF', country_code=689, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='4\\d{5,7}|8\\d{7}', possible_number_pattern='\\d{6}(?:\\d{2})?', possible_length=(6, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='4(?:[09][45689]\\d|4)\\d{4}', example_number='40412345', possible_length=(6, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='8[79]\\d{6}', possible_number_pattern='\\d{8}', example_number='87123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='44\\d{4}', possible_number_pattern='\\d{6}', example_number='441234', possible_length=(6,)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['4[09]|8[79]']),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['44'])])
