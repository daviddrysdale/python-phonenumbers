"""Auto-generated file, do not edit by hand. LA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LA = PhoneMetadata(id='LA', country_code=856, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-57]\\d{7,9}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[2-57]1|54)\\d{6}', possible_number_pattern='\\d{6,8}', example_number='21212862'),
    mobile=PhoneNumberDesc(national_number_pattern='20(?:2[23]|5[4-68]|7[78]|9[7-9])\\d{6}', possible_number_pattern='\\d{10}', example_number='2023123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='19[015]', possible_number_pattern='\\d{3}', example_number='190'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(20)(\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['20'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([2-57]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21|[3-57]'], national_prefix_formatting_rule=u'0\\1')])
