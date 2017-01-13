"""Auto-generated file, do not edit by hand. SC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SC = PhoneMetadata(id='SC', country_code=248, international_prefix='0(?:[02]|10?)',
    general_desc=PhoneNumberDesc(national_number_pattern='[24689]\\d{5,6}', possible_number_pattern='\\d{6,7}', possible_length=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='4[2-46]\\d{5}', possible_number_pattern='\\d{7}', example_number='4217123', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='2[5-8]\\d{5}', possible_number_pattern='\\d{7}', example_number='2510123', possible_length=(7,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8000\\d{3}', possible_number_pattern='\\d{7}', example_number='8000000', possible_length=(7,)),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='(?:64\\d|971)\\d{4}', possible_number_pattern='\\d{7}', example_number='6412345', possible_length=(7,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[246]'])])
