"""Auto-generated file, do not edit by hand. RO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RO = PhoneMetadata(id='RO', country_code=40, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[237-9]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[23][13-6]\\d{7}', possible_number_pattern='\\d{9}', example_number='211234567'),
    mobile=PhoneNumberDesc(national_number_pattern='7[1-8]\\d{7}', possible_number_pattern='\\d{9}', example_number='712345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[036]\\d{6}', possible_number_pattern='\\d{9}', example_number='900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='801\\d{6}', possible_number_pattern='\\d{9}', example_number='801123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='802\\d{6}', possible_number_pattern='\\d{9}', example_number='802123456'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='37\\d{7}', possible_number_pattern='\\d{9}', example_number='372123456'),
    emergency=PhoneNumberDesc(national_number_pattern='112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    preferred_extn_prefix=' int ',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([237]\\d)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23]1|7'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23][02-9]|[89]'], national_prefix_formatting_rule=u'0\\1')])
