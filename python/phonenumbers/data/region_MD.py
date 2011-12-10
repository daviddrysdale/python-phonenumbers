"""Auto-generated file, do not edit by hand. MD metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MD = PhoneMetadata(id='MD', country_code=373, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[256-9]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:1[0569]|2\\d|3[015-7]|4[1-46-9]|5[0-24689]|6[2-589]|7[1-37]|9[1347-9])|5(?:33|5[257]))\\d{5}', possible_number_pattern='\\d{5,8}', example_number='22212345'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:562|6(?:50|7[1-4]|[089]\\d)|7(?:7[47-9]|[89]\\d))\\d{5}', possible_number_pattern='\\d{8}', example_number='65012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', possible_number_pattern='\\d{8}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[056]\\d{5}', possible_number_pattern='\\d{8}', example_number='90012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern='808\\d{5}', possible_number_pattern='\\d{8}', example_number='80812345'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='8(?:03|14)\\d{5}', possible_number_pattern='\\d{8}', example_number='80312345'),
    emergency=PhoneNumberDesc(national_number_pattern='112|90[123]', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(22)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['22'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([25-7]\\d{2})(\\d{2})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2[13-79]|[5-7]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1')])
