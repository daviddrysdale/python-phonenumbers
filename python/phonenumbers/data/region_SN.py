"""Auto-generated file, do not edit by hand. SN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SN = PhoneMetadata(id='SN', country_code=221, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[37]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'3(?:010|3(?:8[1-9]|9[2-9]))\d{5}', possible_number_pattern=u'\d{9}', example_number=u'301012345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7(?:0[1256]0|6(?:1[23]|2[89]|3[3489]|4[6-9]|5[1-389]|6[6-9]|7[45]|8[3-8])|7(?:1[014-8]|2[0-7]|3[0-35-8]|4[0-6]|[56]\d|7[0-589]|8[01]|9[0-6]))\d{5}', possible_number_pattern=u'\d{9}', example_number=u'701012345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'33301\d{4}', possible_number_pattern=u'\d{9}', example_number=u'333011234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
