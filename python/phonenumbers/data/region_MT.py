"""Auto-generated file, do not edit by hand. MT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MT = PhoneMetadata(id='MT', country_code=356, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2579]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:0(?:1[0-6]|[69]\d)|[1-357]\d{2})\d{4}', possible_number_pattern=u'\d{8}', example_number=u'21001234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:7(?:210|[79]\d{2}|)|9(?:2[13]\d|696|8(?:1[1-3]|89|97)|9\d{2}))\d{4}', possible_number_pattern=u'\d{8}', example_number=u'96961234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'50(?:0(?:3[1679]|4\d)|[169]\d{2}|7[06]\d)\d{3}', possible_number_pattern=u'\d{8}', example_number=u'50031234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'7117\d{4}', possible_number_pattern=u'\d{8}', example_number=u'71171234'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2')])
