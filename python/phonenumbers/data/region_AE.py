"""Auto-generated file, do not edit by hand. AE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AE = PhoneMetadata(id='AE', country_code=971, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-79]\\d{7,8}|800\\d{2,9}', possible_length=(5, 6, 7, 8, 9, 10, 11, 12), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-4679][2-8]\\d{6}', example_number='22345678', possible_length=(8,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='5[024-68]\\d{7}', example_number='501234567', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='400\\d{6}|800\\d{2,9}', example_number='800123456', possible_length=(5, 6, 7, 8, 9, 10, 11, 12)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[02]\\d{5}', example_number='900234567', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='700[05]\\d{5}', example_number='700012345', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='600[25]\\d{5}', example_number='600212345', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2-4679])(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2-4679][2-8]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(5\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([479]00)(\\d)(\\d{5})', format='\\1 \\2 \\3', leading_digits_pattern=['[479]00'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='([68]00)(\\d{2,9})', format='\\1 \\2', leading_digits_pattern=['[68]00'], national_prefix_formatting_rule='\\1')])
