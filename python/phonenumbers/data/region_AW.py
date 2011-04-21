"""Auto-generated file, do not edit by hand. AW metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AW = PhoneMetadata(id='AW', country_code=297, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[5-9]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'5(?:2\d{2}|8(?:[2-7]\d|8[0-79]|9[48]))\d{3}', possible_number_pattern=u'\d{7}', example_number=u'5212345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[69]\d|660|9(?:6\d|9[02-9])|7[34]\d)\d{4}', possible_number_pattern=u'\d{7}', example_number=u'5601234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{4}', possible_number_pattern=u'\d{7}', example_number=u'8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{4}', possible_number_pattern=u'\d{7}', example_number=u'9001234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([5-9]\d{2})(\d{4})', format=u'\\1 \\2')])
