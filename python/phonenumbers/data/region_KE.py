"""Auto-generated file, do not edit by hand. KE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KE = PhoneMetadata(id='KE', country_code=254, international_prefix='000',
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{6,10}', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:20|4[0-6]|5\\d|6[0-24-9])\\d{4,7}', possible_number_pattern='\\d{4,9}', example_number='202012345'),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:0[0-3]|[123]\\d|5[0-3]|7[0-4])\\d{6}', possible_number_pattern='\\d{9}', example_number='712123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|88)\\d{6,7}', possible_number_pattern='\\d{9,10}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:00|1)\\d{6,7}', possible_number_pattern='\\d{8,10}', example_number='900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4,7})', format=u'\\1 \\2', leading_digits_pattern=['[2-6]|91'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{6,7})', format=u'\\1 \\2', leading_digits_pattern=['[78]|90'], national_prefix_formatting_rule=u'0\\1')])
