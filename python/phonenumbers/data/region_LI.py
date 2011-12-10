"""Auto-generated file, do not edit by hand. LI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LI = PhoneMetadata(id='LI', country_code=423, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:66|80|90)\\d{7}|[237-9]\\d{6}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:17|3\\d|6[02-58]|96)|3(?:02|7[01357]|8[048]|9[0269])|870)\\d{4}', possible_number_pattern='\\d{7}', example_number='2345678'),
    mobile=PhoneNumberDesc(national_number_pattern='66(?:[0178][0-4]|2[025-9]|[36]\\d|4[129]|5[45]|9[019])\\d{5}|7(?:4[2-59]|56|[6-9]\\d)\\d{4}', possible_number_pattern='\\d{7,9}', example_number='661234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:0(?:07|2[238]|79|\\d{4})|9\\d{2})\\d{2}', possible_number_pattern='\\d{7,9}', example_number='8002222'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='90(?:0(?:2[278]|79|\\d{4})|1(?:23|\\d{4})|6(?:66|\\d{4}))\\d{2}', possible_number_pattern='\\d{7,9}', example_number='9002222'),
    personal_number=PhoneNumberDesc(national_number_pattern='701\\d{4}', possible_number_pattern='\\d{7}', example_number='7011234'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[278]|44)', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23]|7[4-9]|87']),
        NumberFormat(pattern='(6\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['6']),
        NumberFormat(pattern='([7-9]0\\d)(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[7-9]0']),
        NumberFormat(pattern='([89]0\\d)(\\d{2})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[89]0'], national_prefix_formatting_rule=u'0\\1')])
