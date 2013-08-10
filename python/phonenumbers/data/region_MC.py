"""Auto-generated file, do not edit by hand. MC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MC = PhoneMetadata(id='MC', country_code=377, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[4689]\\d{7,8}', possible_number_pattern='\\d{8,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='9[2-47-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='99123456'),
    mobile=PhoneNumberDesc(national_number_pattern='6\\d{8}|4\\d{7}', possible_number_pattern='\\d{8,9}', example_number='612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='(?:8\\d|90)\\d{6}', possible_number_pattern='\\d{8}', example_number='90123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|[578])', possible_number_pattern='\\d{2,3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='8\\d{7}', possible_number_pattern='\\d{8}'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['4'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(6)(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4 \\5', leading_digits_pattern=['6'], national_prefix_formatting_rule=u'0\\1')])
