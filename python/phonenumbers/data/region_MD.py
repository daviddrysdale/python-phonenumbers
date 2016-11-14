"""Auto-generated file, do not edit by hand. MD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MD = PhoneMetadata(id='MD', country_code=373, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[235-9]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2[1-9]\\d|3[1-79]\\d|5(?:33|5[257]))\\d{5}', example_number='22212345', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:562|6\\d{2}|7(?:[189]\\d|6[07]|7[457-9]))\\d{5}', example_number='62112345', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', possible_number_pattern='\\d{8}', example_number='80012345', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[056]\\d{5}', possible_number_pattern='\\d{8}', example_number='90012345', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='808\\d{5}', possible_number_pattern='\\d{8}', example_number='80812345', possible_length=(8,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='3[08]\\d{6}', possible_number_pattern='\\d{8}', example_number='30123456', possible_length=(8,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='803\\d{5}', possible_number_pattern='\\d{8}', example_number='80312345', possible_length=(8,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['22|3'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([25-7]\\d{2})(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['2[13-9]|[5-7]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['[89]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
