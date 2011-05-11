"""Auto-generated file, do not edit by hand. GE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GE = PhoneMetadata(id='GE', country_code=995, international_prefix='8~10',
    general_desc=PhoneNumberDesc(national_number_pattern='[13-79]\\d{7}|8\\d{8}', possible_number_pattern='\\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:[256]\\d|4[124-9]|7[0-4])|4(?:1\\d|2[2-7]|3[1-79]|4[2-8]|7[239]|9[1-7]))\\d{5}', possible_number_pattern='\\d{5,8}', example_number='32123456'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:14|5[01578]|6[28]|7[0147-9]|9[0-35-9])\\d{6}', possible_number_pattern='\\d{8}', example_number='55123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[13-79]'], national_prefix_formatting_rule=u'8 \\1'),
        NumberFormat(pattern='(800)(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'8 \\1')])
