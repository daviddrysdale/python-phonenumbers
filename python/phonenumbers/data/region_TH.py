"""Auto-generated file, do not edit by hand. TH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TH = PhoneMetadata(id='TH', country_code=66, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7,8}|1\\d{3}(?:\\d{5,6})?', possible_number_pattern='\\d{4}|\\d{8,10}', possible_length=(4, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2\\d|3[2-9]|4[2-5]|5[2-6]|7[3-7])\\d{6}', possible_number_pattern='\\d{8}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:14|6[1-5]|[89]\\d)\\d{7}', possible_number_pattern='\\d{9}', example_number='812345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}', example_number='1800123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900\\d{6}', possible_number_pattern='\\d{10}', example_number='1900123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='6[08]\\d{7}', possible_number_pattern='\\d{9}', example_number='601234567', possible_length=(9,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='1\\d{3}', possible_number_pattern='\\d{4}', example_number='1100', possible_length=(4,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1\\d{3}', possible_number_pattern='\\d{4}', example_number='1100', possible_length=(4,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([13-9]\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['14|[3-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1[89]00)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1')],
    mobile_number_portable_region=True)
