"""Auto-generated file, do not edit by hand. 808 metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_808 = PhoneMetadata(id='001', country_code=808, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{8}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(),
    mobile=PhoneNumberDesc(),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(national_number_pattern='\\d{8}', possible_number_pattern='\\d{8}', example_number='12345678', possible_length=(8,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2')],
    leading_zero_possible=True)
