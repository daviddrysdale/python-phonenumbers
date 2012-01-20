"""Auto-generated file, do not edit by hand. CR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CR = PhoneMetadata(id='CR', country_code=506, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[24-9]\\d{7,9}', possible_number_pattern='\\d{8,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[24-7]\\d{6}', possible_number_pattern='\\d{8}', example_number='22123456'),
    mobile=PhoneNumberDesc(national_number_pattern='5(?:0[0-4]|7[01])\\d{5}|[67][01]\\d{6}|8[36-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='83123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[059]\\d{7}', possible_number_pattern='\\d{10}', example_number='9001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='40(?:00\\d{4}|10[0-3]\\d{3}|2(?:00\\d|900)\\d{2}|3[01]\\d{4}|5\\d{5})', possible_number_pattern='\\d{8}', example_number='40001234'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|911', possible_number_pattern='\\d{3}', example_number='911'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix_for_parsing='(19(?:0[0-2]|19|77))',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[24-7]|8[3-9]'], domestic_carrier_code_formatting_rule=u'$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[89]0'], domestic_carrier_code_formatting_rule=u'$CC \\1')])
