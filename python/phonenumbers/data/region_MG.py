"""Auto-generated file, do not edit by hand. MG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MG = PhoneMetadata(id='MG', country_code=261, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[23]\\d{8}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:0(?:(?:2\\d|4[47]|5[3467]|6[279]|8[268]|9[245])\\d|7(?:2[29]|[35]\\d))|210\\d)\\d{4}', possible_number_pattern='\\d{7,9}', example_number='202123456'),
    mobile=PhoneNumberDesc(national_number_pattern='3[02-4]\\d{7}', possible_number_pattern='\\d{9}', example_number='301234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11?[78]', possible_number_pattern='\\d{2,3}', example_number='117'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([23]\\d)(\\d{2})(\\d{3})(\\d{2})', format=u'\\1 \\2 \\3 \\4', national_prefix_formatting_rule=u'0\\1')])
