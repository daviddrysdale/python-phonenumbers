"""Auto-generated file, do not edit by hand. CY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CY = PhoneMetadata(id='CY', country_code=357, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[27-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[2-6]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'22345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7777\d{4}|9(?:[69]\d|7[67])\d{5}', possible_number_pattern=u'\d{8}', example_number=u'96123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8000\d{4}', possible_number_pattern=u'\d{8}', example_number=u'80001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9009\d{4}', possible_number_pattern=u'\d{8}', example_number=u'90091234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'700\d{5}', possible_number_pattern=u'\d{8}', example_number=u'70012345'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([27-9]\d)(\d{6})', format=u'\\1 \\2')])
