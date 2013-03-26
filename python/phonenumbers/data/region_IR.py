"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=98, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[14-8]\\d{6,9}|[23]\\d{5,9}|9(?:[1-4]\\d{8}|9\\d{2,8})', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[145](?:1[1-9]|[2-9]\\d)\\d{0,3}|[23][1-9]\\d{0,4}|6[1-9]\\d{1,4}|[78]\\d{2,5})\\d{4}', possible_number_pattern='\\d{6,10}', example_number='2123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='9[1-3]\\d{8}', possible_number_pattern='\\d{10}', example_number='9123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='(?:[2-6]0\\d|993)\\d{7}', possible_number_pattern='\\d{10}', example_number='9932123456'),
    pager=PhoneNumberDesc(national_number_pattern='943\\d{7}', possible_number_pattern='\\d{10}', example_number='9432123456'),
    uan=PhoneNumberDesc(national_number_pattern='9990\\d{0,6}', possible_number_pattern='\\d{4,10}', example_number='9990123456'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[025]|25)', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(21)(\\d{3,5})', format=u'\\1 \\2', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(21)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(2[16])(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2[16]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[13-9]|2[02-9]'], national_prefix_formatting_rule=u'0\\1')])
