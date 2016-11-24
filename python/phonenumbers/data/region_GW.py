"""Auto-generated file, do not edit by hand. GW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GW = PhoneMetadata(id='GW', country_code=245, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:4(?:0\\d{5}|4\\d{7})|9\\d{8})', possible_number_pattern='\\d{7,9}', possible_length=(7, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='443(?:2[0125]|3[1245]|4[12]|5[1-4]|70|9[1-467])\\d{4}', possible_number_pattern='\\d{9}', example_number='443201234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:55\\d|6(?:6\\d|9[012])|77\\d)\\d{5}', possible_number_pattern='\\d{9}', example_number='955012345', possible_length=(9,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='40\\d{5}', possible_number_pattern='\\d{7}', example_number='4012345', possible_length=(7,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['44|9[567]']),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['40'])])
