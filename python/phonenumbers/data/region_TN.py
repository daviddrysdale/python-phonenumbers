"""Auto-generated file, do not edit by hand. TN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TN = PhoneMetadata(id='TN', country_code=216, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[247-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'7\d{7}', possible_number_pattern=u'\d{8}', example_number=u'71234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:2[0-7]|40|9\d)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'20123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'8[028]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([247-9]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3')])
