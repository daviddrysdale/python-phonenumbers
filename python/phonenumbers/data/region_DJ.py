"""Auto-generated file, do not edit by hand. DJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DJ = PhoneMetadata(id='DJ', country_code=253, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[27]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:1[2-5]|7[45])\\d{5}', example_number='21360003', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='77\\d{6}', example_number='77831001', possible_length=(8,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4')])
