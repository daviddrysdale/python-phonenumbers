"""Auto-generated file, do not edit by hand. BA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BA = PhoneMetadata(id='BA', country_code=387, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[3-689]\d{7}', possible_number_pattern=u'\d{6,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:[35]\d|49)\d{6}', possible_number_pattern=u'\d{6,8}', example_number=u'30123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6[1-356]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'61123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8[08]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9[0246]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'82\d{6}', possible_number_pattern=u'\d{8}', example_number=u'82123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'81\d{6}', possible_number_pattern=u'\d{8}', example_number=u'81123456'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([3-689]\d)(\d{3})(\d{3})', format=u'\\1 \\2-\\3', national_prefix_formatting_rule=u'0\\1')])
