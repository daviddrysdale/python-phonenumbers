"""Auto-generated file, do not edit by hand. PS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PS = PhoneMetadata(id='PS', country_code=970, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[24589]\\d{7,8}|1(?:[78]\\d{8}|[49]\\d{2,3})', possible_number_pattern='\\d{4,10}', possible_length=(4, 5, 8, 9, 10), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:22[234789]|42[45]|82[01458]|92[369])\\d{5}', possible_number_pattern='\\d{7,8}', example_number='22234567', possible_length=(8,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='5[69]\\d{7}', possible_number_pattern='\\d{9}', example_number='599123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}', example_number='1800123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1(?:4|9\\d)\\d{2}', possible_number_pattern='\\d{4,5}', example_number='19123', possible_length=(4, 5)),
    shared_cost=PhoneNumberDesc(national_number_pattern='1700\\d{6}', possible_number_pattern='\\d{10}', example_number='1700123456', possible_length=(10,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2489])(2\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2489]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(5[69]\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1[78]00)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1[78]'], national_prefix_formatting_rule='\\1')])
