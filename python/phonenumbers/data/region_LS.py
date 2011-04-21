"""Auto-generated file, do not edit by hand. LS metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LS = PhoneMetadata(id='LS', country_code=266, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2568]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2\d{7}', possible_number_pattern=u'\d{8}', example_number=u'22123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[56]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'50123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800[256]\d{4}', possible_number_pattern=u'\d{8}', example_number=u'80021234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2')])
