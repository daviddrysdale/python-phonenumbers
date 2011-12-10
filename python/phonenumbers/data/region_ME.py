"""Auto-generated file, do not edit by hand. ME metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ME = PhoneMetadata(id='ME', country_code=382, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7,8}', possible_number_pattern='\\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:20[2-8]|3(?:0[2-7]|1[35-7]|2[3567]|3[4-7])|4(?:0[237]|1[27])|5(?:0[47]|1[27]|2[378]))\\d{5}', possible_number_pattern='\\d{6,8}', example_number='30234567'),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:32\\d|[89]\\d{2}|7(?:[0-8]\\d|9(?:[3-9]|[0-2]\\d)))\\d{4}', possible_number_pattern='\\d{8,9}', example_number='67622901'),
    toll_free=PhoneNumberDesc(national_number_pattern='800[28]\\d{4}', possible_number_pattern='\\d{8}', example_number='80080002'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:88\\d|9(?:4[13-8]|5[16-8]))\\d{5}', possible_number_pattern='\\d{8}', example_number='94515151'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='78[134579]\\d{5}', possible_number_pattern='\\d{8}', example_number='78108780'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='77\\d{6}', possible_number_pattern='\\d{8}', example_number='77273012'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|2[234])', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-57-9]|6[3789]', '[2-57-9]|6(?:[389]|7(?:[0-8]|9[3-9]))'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(67)(9)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['679', '679[0-2]'], national_prefix_formatting_rule=u'0\\1')])
