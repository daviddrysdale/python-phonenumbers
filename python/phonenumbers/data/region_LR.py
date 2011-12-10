"""Auto-generated file, do not edit by hand. LR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LR = PhoneMetadata(id='LR', country_code=231, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[29]\\d|[4-6]|7\\d{1,2}|[38]\\d{2})\\d{6}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2\\d{7}', possible_number_pattern='\\d{8}', example_number='21234567'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:4[67]|5\\d|6[4-8]|7(?:7[67]\\d|\\d{2})|880\\d)\\d{5}', possible_number_pattern='\\d{7,9}', example_number='4612345'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{6}', possible_number_pattern='\\d{8}', example_number='90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='33200\\d{4}', possible_number_pattern='\\d{9}', example_number='332001234'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='355|911', possible_number_pattern='\\d{3}', example_number='911'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([279]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[279]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(7\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([4-6])(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[4-6]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[38]'], national_prefix_formatting_rule=u'0\\1')])
