"""Auto-generated file, do not edit by hand. CW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CW = PhoneMetadata(id='CW', country_code=599, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[169]\\d{6,7}', possible_number_pattern='\\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='9(?:[48]\\d{2}|50\\d|7(?:2[0-2]|[34]\\d|6[35-7]|77))\\d{4}', possible_number_pattern='\\d{7,8}', example_number='94151234'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:5(?:[1246]\\d|3[01])|6(?:[1679]\\d|3[01]))\\d{4}', possible_number_pattern='\\d{7,8}', example_number='95181234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='(?:10|69)\\d{5}', possible_number_pattern='\\d{7}', example_number='1011234'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='955\\d{5}', possible_number_pattern='\\d{7,8}', example_number='95581234'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|911', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[13-7]']),
        NumberFormat(pattern='(9)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'])],
    main_country_for_code=True)
