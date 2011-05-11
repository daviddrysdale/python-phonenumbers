"""Auto-generated file, do not edit by hand. BF metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BF = PhoneMetadata(id='BF', country_code=226, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2457]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:20(?:49|5[23]|9[016-9])|40(?:4[569]|55|7[0179])|50[34]\\d)\\d{4}', possible_number_pattern='\\d{8}', example_number='20491234'),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:[024-6]\\d|1[0-4689]|3[0-6]|7[01]|8[013-9]|9[0-4])\\d{5}', possible_number_pattern='\\d{8}', example_number='70123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4')])
