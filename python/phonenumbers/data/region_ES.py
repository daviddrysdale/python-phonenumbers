"""Auto-generated file, do not edit by hand. ES metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ES = PhoneMetadata(id='ES', country_code=34, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[5-9]\\d{8}', possible_number_pattern='\\d{9}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='8(?:[13]0|[28][0-8]|[47][1-9]|5[01346-9]|6[0457-9])\\d{6}|9(?:[15]\\d{7}|[238][0-8]\\d{6}|4[1-9]\\d{6}|6(?:[0-8]\\d{6}|9(?:0(?:[0-57-9]\\d{4}|6(?:0[0-8]|1[1-9]|[2-9]\\d)\\d{2})|[1-9]\\d{5}))|7(?:[124-9]\\d{2}|3(?:[0-8]\\d|9[1-9]))\\d{4})', example_number='810123456', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:6\\d{6}|7[1-48]\\d{5}|9(?:6906(?:09|10)|7390\\d{2}))\\d{2}', example_number='612345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='[89]00\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='80[367]\\d{6}', possible_number_pattern='\\d{9}', example_number='803123456', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='90[12]\\d{6}', possible_number_pattern='\\d{9}', example_number='901123456', possible_length=(9,)),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{7}', possible_number_pattern='\\d{9}', example_number='701234567', possible_length=(9,)),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='51\\d{7}', possible_number_pattern='\\d{9}', example_number='511234567', possible_length=(9,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='([89]00)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]00']),
        NumberFormat(pattern='([5-9]\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[568]|[79][0-8]'])],
    mobile_number_portable_region=True)
