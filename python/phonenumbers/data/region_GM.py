"""Auto-generated file, do not edit by hand. GM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GM = PhoneMetadata(id='GM', country_code=220, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[3-9]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:4(?:[23]\d{2}|4(?:1[024679]|[6-9]\d))|5(?:54[0-7]|6(?:[67]\d)|7(?:1[04]|2[035]|3[58]|48))|8\d{3})\d{3}', possible_number_pattern=u'\d{7}', example_number=u'5661234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[3679]\d{6}', possible_number_pattern=u'\d{7}', example_number=u'3012345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2')])
