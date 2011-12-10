"""Auto-generated file, do not edit by hand. SK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SK = PhoneMetadata(id='SK', country_code=421, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-689]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-5]\\d{8}', possible_number_pattern='\\d{9}', example_number='212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:0[1-8]|1[0-24-9]|4[0489])\\d{6}', possible_number_pattern='\\d{9}', example_number='912123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:[78]\\d{7}|00\\d{6})', possible_number_pattern='\\d{9}', example_number='900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='8[5-9]\\d{7}', possible_number_pattern='\\d{9}', example_number='850123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='6(?:5[0-4]|9[0-6])\\d{6}', possible_number_pattern='\\d{9}', example_number='690123456'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|5[058])', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2)(\\d{3})(\\d{3})(\\d{2})', format=u'\\1/\\2 \\3 \\4', leading_digits_pattern=['2'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([3-5]\\d)(\\d{3})(\\d{2})(\\d{2})', format=u'\\1/\\2 \\3 \\4', leading_digits_pattern=['[3-5]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([689]\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[689]'], national_prefix_formatting_rule=u'0\\1')])
