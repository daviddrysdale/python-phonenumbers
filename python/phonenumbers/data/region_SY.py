"""Auto-generated file, do not edit by hand. SY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SY = PhoneMetadata(id='SY', country_code=963, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-59]\\d{7,8}', possible_number_pattern='\\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:1\\d?|4\\d|[2356])|2[1-35]|3(?:[13]\\d|4)|4[13]|5[1-3])\\d{6}', possible_number_pattern='\\d{6,9}', example_number='112345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:3[23]|4[457]|55|6[67]|88|9[1-49])\\d{6}', possible_number_pattern='\\d{9}', example_number='944567890'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[023]', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-5]'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(9[3-689])(\\d{4})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True)])
