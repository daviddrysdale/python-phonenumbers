"""Auto-generated file, do not edit by hand. PF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PF = PhoneMetadata(id='PF', country_code=689, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{5}', possible_number_pattern='\\d{6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:36\\d|4(?:[02-9]\\d|1[02-9])|[5689]\\d{2})\\d{3}', possible_number_pattern='\\d{6}', example_number='401234'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[27]\\d{3}|3[0-59]\\d{2}|411[3-6])\\d{2}', possible_number_pattern='\\d{6}', example_number='212345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1[578]', possible_number_pattern='\\d{2}', example_number='15'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:36|44)\\d{4}', possible_number_pattern='\\d{6}', example_number='441234'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3')])
