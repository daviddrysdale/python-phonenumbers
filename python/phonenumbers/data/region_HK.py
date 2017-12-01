"""Auto-generated file, do not edit by hand. HK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HK = PhoneMetadata(id='HK', country_code=852, international_prefix='00(?:[126-9]|30|5[09])?',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-7]\\d{7}|8[0-3]\\d{6,7}|9\\d{4,10}', possible_length=(5, 6, 7, 8, 9, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:[13-8]\\d|2[013-9]|9[0-24-9])|3(?:[1569][0-24-9]|4[0-246-9]|7[0-24-69]|89)|58[01])\\d{5}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:464|5(?:[1-59][0-46-9]|6[0-4689]|7[0-469])|6(?:0[1-9]|[1459]\\d|[2368][0-57-9]|7[0-79])|9(?:0[1-9]|1[02-9]|[2358][0-8]|[467]\\d))\\d{5}', example_number='51234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900(?:[0-24-9]\\d{7}|3\\d{1,4})', example_number='90012345678', possible_length=(5, 6, 7, 8, 11)),
    personal_number=PhoneNumberDesc(national_number_pattern='8(?:1[1-4679]|2[0-367]|3[02-47])\\d{5}', example_number='81123456', possible_length=(8,)),
    pager=PhoneNumberDesc(national_number_pattern='7(?:1[0-369]|[23][0-37-9]|47|5[1578]|6[0235]|7[278]|8[236-9]|9[025-9])\\d{5}', example_number='71234567', possible_length=(8,)),
    uan=PhoneNumberDesc(national_number_pattern='30(?:0[1-9]|[15-7]\\d|2[047]|89)\\d{4}', example_number='30161234', possible_length=(8,)),
    preferred_international_prefix='00',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[2-7]|[89](?:0[1-9]|[1-9])']),
        NumberFormat(pattern='(800)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['800']),
        NumberFormat(pattern='(900)(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['900']),
        NumberFormat(pattern='(900)(\\d{2,5})', format='\\1 \\2', leading_digits_pattern=['900'])],
    mobile_number_portable_region=True)
