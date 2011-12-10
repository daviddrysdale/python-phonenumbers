"""Auto-generated file, do not edit by hand. MU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MU = PhoneMetadata(id='MU', country_code=230, international_prefix='0(?:[2-7]0|33)',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{6}', possible_number_pattern='\\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:[034789]\\d|1[0-7])|4(?:[013-8]\\d|2[4-7])|[56]\\d{2}|8(?:14|3[129]))\\d{4}', possible_number_pattern='\\d{7}', example_number='2012345'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:25\\d|4(?:2[12389]|9\\d)|7\\d{2}|87[15-8]|9[1-8]\\d)\\d{4}', possible_number_pattern='\\d{7}', example_number='2512345'),
    toll_free=PhoneNumberDesc(national_number_pattern='80[012]\\d{4}', possible_number_pattern='\\d{7}', example_number='8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='30\\d{5}', possible_number_pattern='\\d{7}', example_number='3012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='3(?:20|9\\d)\\d{4}', possible_number_pattern='\\d{7}', example_number='3201234'),
    pager=PhoneNumberDesc(national_number_pattern='2(?:1[89]|2\\d)\\d{4}', possible_number_pattern='\\d{7}', example_number='2181234'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[45]|99\\d', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    preferred_international_prefix='020',
    number_format=[NumberFormat(pattern='([2-9]\\d{2})(\\d{4})', format=u'\\1 \\2')])
