"""Auto-generated file, do not edit by hand. AE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AE = PhoneMetadata(id='AE', country_code=971, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-79]\\d{7,8}|800\\d{2,9}', possible_number_pattern='\\d{5,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[2-4679][2-8]\\d|600[25])\\d{5}', possible_number_pattern='\\d{7,9}', example_number='22345678'),
    mobile=PhoneNumberDesc(national_number_pattern='5[056]\\d{7}', possible_number_pattern='\\d{9}', example_number='501234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='400\\d{6}|800\\d{2,9}', possible_number_pattern='\\d{5,12}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[02]\\d{5}', possible_number_pattern='\\d{9}', example_number='900234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='700[05]\\d{5}', possible_number_pattern='\\d{9}', example_number='700012345'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|99[789]', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2-4679])(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-4679][2-8]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(5[056])(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['5'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([4679]00)(\\d)(\\d{5})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[4679]0'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(800)(\\d{2,9})', format=u'\\1 \\2', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'\\1')])
