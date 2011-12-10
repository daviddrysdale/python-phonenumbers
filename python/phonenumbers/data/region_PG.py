"""Auto-generated file, do not edit by hand. PG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PG = PhoneMetadata(id='PG', country_code=675, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{6,7}', possible_number_pattern='\\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3\\d{2}|4[257]\\d|5[34]\\d|6(?:29|4[1-9])|85[02-46-9]|9[78]\\d)\\d{4}', possible_number_pattern='\\d{7}', example_number='3123456'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:68|7[1236]\\d)\\d{5}', possible_number_pattern='\\d{7,8}', example_number='6812345'),
    toll_free=PhoneNumberDesc(national_number_pattern='180\\d{4}', possible_number_pattern='\\d{7}', example_number='1801234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='275\\d{4}', possible_number_pattern='\\d{7}', example_number='2751234'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='000', possible_number_pattern='\\d{3}', example_number='000'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[1-689]']),
        NumberFormat(pattern='(7[1-36]\\d)(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7[1-36]'])])
