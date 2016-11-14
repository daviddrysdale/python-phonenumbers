"""Auto-generated file, do not edit by hand. CW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CW = PhoneMetadata(id='CW', country_code=599, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[169]\\d{6,7}', possible_number_pattern='\\d{7,8}', possible_length=(7, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='9(?:[48]\\d{2}|50\\d|7(?:2[0-24]|[34]\\d|6[35-7]|77|8[7-9]))\\d{4}', example_number='94151234', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:5(?:[12467]\\d|3[01])|6(?:[15-9]\\d|3[01]))\\d{4}', example_number='95181234', possible_length=(8,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(national_number_pattern='60[0-2]\\d{4}', possible_number_pattern='\\d{7}', example_number='6001234', possible_length=(7,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(national_number_pattern='955\\d{5}', possible_number_pattern='\\d{7,8}', example_number='95581234', possible_length=(8,)),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[13-7]']),
        NumberFormat(pattern='(9)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['9'])],
    main_country_for_code=True)
