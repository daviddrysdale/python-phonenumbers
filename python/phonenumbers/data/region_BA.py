"""Auto-generated file, do not edit by hand. BA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BA = PhoneMetadata(id='BA', country_code=387, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-689]\\d{7}', possible_number_pattern='\\d{6,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[35]\\d|49)\\d{6}', possible_number_pattern='\\d{6,8}', example_number='30123456'),
    mobile=PhoneNumberDesc(national_number_pattern='6[1-356]\\d{6}', possible_number_pattern='\\d{8}', example_number='61123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='8[08]\\d{6}', possible_number_pattern='\\d{8}', example_number='80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9[0246]\\d{6}', possible_number_pattern='\\d{8}', example_number='90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='82\\d{6}', possible_number_pattern='\\d{8}', example_number='82123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='81\\d{6}', possible_number_pattern='\\d{8}', example_number='81123456'),
    emergency=PhoneNumberDesc(national_number_pattern='12[234]', possible_number_pattern='\\d{3}', example_number='122'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([3-689]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2-\\3', national_prefix_formatting_rule=u'0\\1')])
