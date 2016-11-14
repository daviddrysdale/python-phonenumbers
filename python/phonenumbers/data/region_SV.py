"""Auto-generated file, do not edit by hand. SV metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SV = PhoneMetadata(id='SV', country_code=503, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[267]\\d{7}|[89]\\d{6}(?:\\d{4})?', possible_number_pattern='\\d{7,8}|\\d{11}', possible_length=(7, 8, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[1-6]\\d{6}', possible_number_pattern='\\d{8}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='[67]\\d{7}', possible_number_pattern='\\d{8}', example_number='70123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4}(?:\\d{4})?', possible_number_pattern='\\d{7}(?:\\d{4})?', example_number='8001234', possible_length=(7, 11)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{4}(?:\\d{4})?', possible_number_pattern='\\d{7}(?:\\d{4})?', example_number='9001234', possible_length=(7, 11)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[267]']),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[89]']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]'])])
