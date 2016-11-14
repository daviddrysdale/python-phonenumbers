"""Auto-generated file, do not edit by hand. ME metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ME = PhoneMetadata(id='ME', country_code=382, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7,8}', possible_number_pattern='\\d{6,9}', possible_length=(8, 9), possible_length_local_only=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:20[2-8]|3(?:0[2-7]|[12][35-7]|3[4-7])|4(?:0[2367]|1[267])|5(?:0[467]|1[267]|2[367]))\\d{5}', possible_number_pattern='\\d{6,8}', example_number='30234567', possible_length=(8,), possible_length_local_only=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:00\\d|3[24]\\d|61\\d|7(?:[0-8]\\d|9(?:[3-9]|[0-2]\\d))|[89]\\d{2})\\d{4}', possible_number_pattern='\\d{8,9}', example_number='67622901', possible_length=(8, 9)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{6}', possible_number_pattern='\\d{8}', example_number='80080002', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:9(?:4[1568]|5[178]))\\d{5}', possible_number_pattern='\\d{8}', example_number='94515151', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='78[1-9]\\d{5}', possible_number_pattern='\\d{8}', example_number='78108780', possible_length=(8,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='77\\d{6}', possible_number_pattern='\\d{8}', example_number='77273012', possible_length=(8,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[2-57-9]|6[036-9]', '[2-57-9]|6(?:[03689]|7(?:[0-8]|9[3-9]))'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(67)(9)(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['679', '679[0-2]'], national_prefix_formatting_rule='0\\1')])
