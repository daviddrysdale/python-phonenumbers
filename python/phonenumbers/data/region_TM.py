"""Auto-generated file, do not edit by hand. TM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TM = PhoneMetadata(id='TM', country_code=993, international_prefix='8~10',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-6]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:12\\d|243|[3-5]22)\\d{5}', possible_number_pattern='\\d{8}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='6[6-8]\\d{6}', possible_number_pattern='\\d{8}', example_number='66123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='([1-6]\\d)(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', national_prefix_formatting_rule=u'8 \\1')])
