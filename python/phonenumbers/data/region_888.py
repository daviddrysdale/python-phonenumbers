"""Auto-generated file, do not edit by hand. 888 metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_888 = PhoneMetadata(id='001', country_code=888, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{11}', possible_number_pattern='\\d{11}', possible_length=(11,)),
    fixed_line=PhoneNumberDesc(),
    mobile=PhoneNumberDesc(),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='\\d{11}', possible_number_pattern='\\d{11}', example_number='12345678901', possible_length=(11,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{5})', format='\\1 \\2 \\3')],
    leading_zero_possible=True)
