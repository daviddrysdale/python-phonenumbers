"""Auto-generated file, do not edit by hand. MM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MM = PhoneMetadata(id='MM', country_code=95, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[124-8]\\d{5,7}|9\\d{7,8}', possible_number_pattern='\\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1\\d|2|4[2-6]|5[2-9]|6\\d|7[0-5]|8[1-6])\\d{5}|1333\\d{4}', possible_number_pattern='\\d{5,8}', example_number='1234567'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:[25689]\\d|444)\\d{5}', possible_number_pattern='\\d{8,9}', example_number='92123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(1)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1']),
        NumberFormat(pattern='(1)(3)(33\\d)(\\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['133', '1333']),
        NumberFormat(pattern='(2)(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2']),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[4-8]']),
        NumberFormat(pattern='(9444)(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['94']),
        NumberFormat(pattern='(9)([25689]\\d{2})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9[25689]'])])
