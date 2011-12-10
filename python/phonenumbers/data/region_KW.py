"""Auto-generated file, do not edit by hand. KW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KW = PhoneMetadata(id='KW', country_code=965, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[12569]\\d{6,7}|65816\\d{6}', possible_number_pattern='\\d{7,8}|\\d{11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:18\\d|2(?:[23]\\d{2}|4[1-35-9]\\d|5(?:0[034]|[2-46]\\d|5[1-3]|7[1-7])))\\d{4}', possible_number_pattern='\\d{7,8}', example_number='22345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5(?:0[0-26]|5\\d)|6(?:0[034679]|5(?:[015-79]|8(?:[02-9]|1[0-57-9]))|6\\d|7[067]|9[69])|9(?:0[09]|4[049]|66|[79]\\d))\\d{5}', possible_number_pattern='\\d{8}', example_number='50012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='65816\\d{6}', possible_number_pattern='\\d{11}', example_number='65816123456'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3,4})', format=u'\\1 \\2', leading_digits_pattern=['[1269]']),
        NumberFormat(pattern='(5[05]\\d)(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['5']),
        NumberFormat(pattern='(65816)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['65816'])])
