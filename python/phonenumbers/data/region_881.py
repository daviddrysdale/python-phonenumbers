"""Auto-generated file, do not edit by hand. 881 metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_881 = PhoneMetadata(id='001', country_code=881, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[67]\\d{8}', possible_number_pattern='\\d{9}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(),
    mobile=PhoneNumberDesc(national_number_pattern='[67]\\d{8}', example_number='612345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{5})', format='\\1 \\2 \\3', leading_digits_pattern=['[67]'])])
