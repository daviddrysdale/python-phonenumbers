"""Auto-generated file, do not edit by hand. CK metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CK = PhoneMetadata(id='CK', country_code=682, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-57]\d{4}', possible_number_pattern=u'\d{5}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2\d|3[13-7]|4[1-5])\d{3}', possible_number_pattern=u'\d{5}', example_number=u'21234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[0-68]|7\d)\d{3}', possible_number_pattern=u'\d{5}', example_number=u'71234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})', format=u'\\1 \\2')])
