"""Auto-generated file, do not edit by hand. VU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VU = PhoneMetadata(id='VU', country_code=678, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-57-9]\\d{4,6}', possible_number_pattern='\\d{5,7}', possible_length=(5, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2[02-9]\\d|3(?:[5-7]\\d|8[0-8])|48[4-9]|88\\d)\\d{2}', possible_number_pattern='\\d{5}', example_number='22123', possible_length=(5,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5(?:7[2-5]|[0-689]\\d)|7[013-7]\\d)\\d{4}', possible_number_pattern='\\d{7}', example_number='5912345', possible_length=(7,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='3[03]\\d{3}|900\\d{4}', possible_number_pattern='\\d{5,7}', example_number='30123', possible_length=(5, 7)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[579]'])])
