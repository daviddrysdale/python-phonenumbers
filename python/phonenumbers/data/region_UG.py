"""Auto-generated file, do not edit by hand. UG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UG = PhoneMetadata(id='UG', country_code=256, international_prefix='00[057]',
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{9}', possible_length=(9,), possible_length_local_only=(5, 6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='20(?:[0147]\\d{3}|2(?:40|[5-9]\\d)\\d|3(?:0[0-4]|[2367]\\d)\\d|5[0-4]\\d{2}|6(?:00[0-2]|30[0-4]|[5-9]\\d{2})|8[0-2]\\d{2})\\d{3}|[34]\\d{8}', example_number='312345678', possible_length=(9,), possible_length_local_only=(5, 6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:0[0-7]\\d|[1578]\\d{2}|2(?:[03]\\d|60)|30\\d|4[0-4]\\d|9(?:[0-6]\\d|74))\\d{5}', example_number='712345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800[123]\\d{5}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[123]\\d{6}', example_number='901123456', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['20[0-8]|4(?:6[45]|[7-9])|[7-9]', '20(?:[013-8]|2[5-9])|4(?:6[45]|[7-9])|[7-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['3|4(?:[1-5]|6[0-36-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(2024)(\\d{5})', format='\\1 \\2', leading_digits_pattern=['202', '2024'], national_prefix_formatting_rule='0\\1')])
