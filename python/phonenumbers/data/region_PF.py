"""Auto-generated file, do not edit by hand. PF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PF = PhoneMetadata(id='PF', country_code=689, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-79]\\d{5}|8\\d{5,7}', possible_number_pattern='\\d{6}(?:\\d{2})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:4(?:[02-9]\\d|1[02-9])|[5689]\\d{2})\\d{3}', possible_number_pattern='\\d{6}', example_number='401234'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[27]\\d{2}|3[0-79]\\d|411|89\\d{3})\\d{3}', possible_number_pattern='\\d{6}(?:\\d{2})?', example_number='212345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='44\\d{4}', possible_number_pattern='\\d{6}', example_number='441234'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['89']),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3')])
