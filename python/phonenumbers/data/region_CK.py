"""Auto-generated file, do not edit by hand. CK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CK = PhoneMetadata(id='CK', country_code=682, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-8]\\d{4}', possible_number_pattern='\\d{5}', possible_length=(5,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2\\d|3[13-7]|4[1-5])\\d{3}', example_number='21234', possible_length=(5,)),
    mobile=PhoneNumberDesc(national_number_pattern='[5-8]\\d{4}', example_number='71234', possible_length=(5,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})', format='\\1 \\2')])
