"""Auto-generated file, do not edit by hand. MO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MO = PhoneMetadata(id='MO', country_code=853, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[268]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:28[2-57-9]|8[2-57-9]\d)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'28212345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6[26]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'66123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([268]\d{3})(\d{4})', format=u'\\1 \\2')])
