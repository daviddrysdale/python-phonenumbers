"""Auto-generated file, do not edit by hand. GT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GT = PhoneMetadata(id='GT', country_code=502, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-7]\\d{7}|1[89]\\d{9}', possible_number_pattern='\\d{8}(?:\\d{3})?', possible_length=(8, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[267][2-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='22456789', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='[345]\\d{7}', possible_number_pattern='\\d{8}', example_number='51234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='18[01]\\d{8}', possible_number_pattern='\\d{11}', example_number='18001112222', possible_length=(11,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='19\\d{9}', possible_number_pattern='\\d{11}', example_number='19001112222', possible_length=(11,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[2-7]']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1'])])
