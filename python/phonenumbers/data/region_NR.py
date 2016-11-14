"""Auto-generated file, do not edit by hand. NR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NR = PhoneMetadata(id='NR', country_code=674, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[458]\\d{6}', possible_number_pattern='\\d{7}', possible_length=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:444|888)\\d{4}', example_number='4441234', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='55[5-9]\\d{4}', example_number='5551234', possible_length=(7,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2')])
