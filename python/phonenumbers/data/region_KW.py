"""Auto-generated file, do not edit by hand. KW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KW = PhoneMetadata(id='KW', country_code=965, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[12569]\\d{6,7}', possible_number_pattern='\\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:18\\d|2(?:[23]\\d{2}|4(?:[1-35-9]\\d|44)|5(?:0[034]|[2-46]\\d|5[1-3]|7[1-7])))\\d{4}', possible_number_pattern='\\d{7,8}', example_number='22345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5(?:[05]\\d|1[0-7])|6(?:0[034679]|5[015-9]|6\\d|7[067]|9[0369])|9(?:0[09]|4[049]|55|6[069]|[79]\\d|8[07-9]))\\d{5}', possible_number_pattern='\\d{8}', example_number='50012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['[1269]']),
        NumberFormat(pattern='(5[015]\\d)(\\d{5})', format='\\1 \\2', leading_digits_pattern=['5'])],
    mobile_number_portable_region=True)
