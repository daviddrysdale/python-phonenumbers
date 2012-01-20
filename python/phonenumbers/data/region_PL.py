"""Auto-generated file, do not edit by hand. PL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PL = PhoneMetadata(id='PL', country_code=48, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-58]\\d{6,8}|9\\d{8}|[67]\\d{5,8}', possible_number_pattern='\\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[2-8]|2[2-59]|3[2-4]|4[1-468]|5[24-689]|6[1-3578]|7[14-6]|8[1-7])\\d{5,7}|77\\d{4,7}|(?:89|9[145])\\d{7}', possible_number_pattern='\\d{6,9}', example_number='123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[013]|6[069]|7[289]|88)\\d{7}', possible_number_pattern='\\d{9}', example_number='512345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='70\\d{7}', possible_number_pattern='\\d{9}', example_number='701234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='801\\d{6}', possible_number_pattern='\\d{9}', example_number='801234567'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='39\\d{7}', possible_number_pattern='\\d{9}', example_number='391234567'),
    pager=PhoneNumberDesc(national_number_pattern='642\\d{3,6}', possible_number_pattern='\\d{6,9}', example_number='642123456'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|99[789]', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[124]|3[2-4]|5[24-689]|6[1-3578]|7[14-7]|8[1-79]|9[145]']),
        NumberFormat(pattern='(\\d{2})(\\d{4,6})', format=u'\\1 \\2', leading_digits_pattern=['[124]|3[2-4]|5[24-689]|6[1-3578]|7[14-7]|8[1-7]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['39|5[013]|6[0469]|7[0289]|8[08]']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2,3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['64']),
        NumberFormat(pattern='(\\d{3})(\\d{3})', format=u'\\1 \\2', leading_digits_pattern=['64'])])
