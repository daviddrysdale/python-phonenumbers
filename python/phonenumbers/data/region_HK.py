"""Auto-generated file, do not edit by hand. HK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HK = PhoneMetadata(id='HK', country_code=852, international_prefix='00(?:[126-9]|30|5[09])?',
    general_desc=PhoneNumberDesc(national_number_pattern='[235-7]\\d{7}|8\\d{7,8}|9\\d{4,10}', possible_number_pattern='\\d{5,11}', possible_length=(5, 6, 7, 8, 9, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[23]\\d|58)\\d{6}', possible_number_pattern='\\d{8}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[1-79]\\d|6\\d{2}|8[4-79]\\d|9(?:0[1-9]|[1-8]\\d))\\d{5}', possible_number_pattern='\\d{8}', example_number='51234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900(?:[0-24-9]\\d{7}|3\\d{1,4})', possible_number_pattern='\\d{5,11}', example_number='90012345678', possible_length=(5, 6, 7, 8, 11)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(national_number_pattern='8[1-3]\\d{6}', possible_number_pattern='\\d{8}', example_number='81123456', possible_length=(8,)),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(national_number_pattern='7\\d{7}', possible_number_pattern='\\d{8}', example_number='71234567', possible_length=(8,)),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[235-7]|[89](?:0[1-9]|[1-9])']),
        NumberFormat(pattern='(800)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['800']),
        NumberFormat(pattern='(900)(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['900']),
        NumberFormat(pattern='(900)(\\d{2,5})', format='\\1 \\2', leading_digits_pattern=['900'])],
    mobile_number_portable_region=True)
