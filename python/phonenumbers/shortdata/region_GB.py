"""Auto-generated file, do not edit by hand. GB metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GB = PhoneMetadata(id='GB', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-4679]\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-4679]\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    mobile=PhoneNumberDesc(national_number_pattern='[1-4679]\\d{2,5}', possible_number_pattern='\\d{3,6}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[01]|1(?:1|[68]\\d{3})|2[123]|33|4(?:1|7\\d)|5\\d|70\\d|800\\d|9[15])|2(?:02|2(?:02|11|2)|3(?:02|45)|425)|3[13]3|4(?:0[02]|35[01]|44[45]|5\\d)|650|789|901', possible_number_pattern='\\d{3,6}', example_number='150'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
