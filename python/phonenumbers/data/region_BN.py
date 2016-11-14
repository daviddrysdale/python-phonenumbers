"""Auto-generated file, do not edit by hand. BN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BN = PhoneMetadata(id='BN', country_code=673, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-578]\\d{6}', possible_number_pattern='\\d{7}', possible_length=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:[013-9]\\d|2[0-7])\\d{4}|[3-5]\\d{6}', example_number='2345678', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='22[89]\\d{4}|[78]\\d{6}', example_number='7123456', possible_length=(7,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='([2-578]\\d{2})(\\d{4})', format='\\1 \\2')])
