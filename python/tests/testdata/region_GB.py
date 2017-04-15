"""Auto-generated file, do not edit by hand. GB metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GB = PhoneMetadata(id='GB', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{10}', possible_length=(9, 10), possible_length_local_only=(6, 7, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-6]\\d{9}', example_number='3123456789', possible_length=(9, 10), possible_length_local_only=(6, 7, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='7[1-57-9]\\d{8}', example_number='7123456789', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{8}', example_number='8023456789', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='9[018]\\d{8}', example_number='9023456789', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8(?:4[3-5]|7[0-2])\\d{7}', example_number='8433456789', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{8}', example_number='7033456789', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='56\\d{8}', example_number='5633456789', possible_length=(10,)),
    pager=PhoneNumberDesc(national_number_pattern='76\\d{8}', example_number='7623456789', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-59]|[78]0'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['6'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['7[1-57-9]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['8[47]'], national_prefix_formatting_rule='(0\\1)')],
    mobile_number_portable_region=True)
