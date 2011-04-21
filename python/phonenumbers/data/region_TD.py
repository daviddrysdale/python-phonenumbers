"""Auto-generated file, do not edit by hand. TD metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TD = PhoneMetadata(id='TD', country_code=235, international_prefix='00|16',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2679]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'22(?:[3789]0|5[0-5]|6[89])\d{4}', possible_number_pattern=u'\d{8}', example_number=u'22501234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:6(?:3[0-7]|6\d)|77\d|9(?:5[0-4]|9\d))\d{5}', possible_number_pattern=u'\d{8}', example_number=u'63012345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'00',
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
