"""Auto-generated file, do not edit by hand. CN metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CN = PhoneMetadata(id='CN', country_code=86, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{6,11}|8[0-357-9]\\d{6,9}|9\\d{7,10}', possible_number_pattern='\\d{4,12}', possible_length=(11,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-9]\\d{10}', possible_number_pattern='\\d{11}', example_number='91234567', possible_length=(11,)),
    mobile=PhoneNumberDesc(national_number_pattern='1(?:[38]\\d|4[57]|5[0-35-9]|7[0136-8])\\d{8}', possible_number_pattern='\\d{11}', example_number='13123456789', possible_length=(11,)),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['[3-9]', '[3-9]\\d{2}[19]', '[3-9]\\d{2}(?:10|95)'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{8})', format='\\1 \\2', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1')])
