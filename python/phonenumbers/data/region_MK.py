"""Auto-generated file, do not edit by hand. MK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MK = PhoneMetadata(id='MK', country_code=389, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-578]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:[23]\\d|5[125]|61)|3(?:1[3-6]|2[2-6]|3[2-5]|4[235])|4(?:[23][2-6]|4[3-6]|5[25]|6[25-8]|7[24-6]|8[4-6]))\\d{5}', possible_number_pattern='\\d{6,8}', example_number='22212345'),
    mobile=PhoneNumberDesc(national_number_pattern='7[0-25-8]\\d{6}', possible_number_pattern='\\d{8}', example_number='72345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', possible_number_pattern='\\d{8}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='5[02-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='50012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern='8(?:0[1-9]|[1-9]\\d)\\d{5}', possible_number_pattern='\\d{8}', example_number='80123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|9[234])', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([347]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[347]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([58]\\d{2})(\\d)(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[58]'], national_prefix_formatting_rule=u'0\\1')])
