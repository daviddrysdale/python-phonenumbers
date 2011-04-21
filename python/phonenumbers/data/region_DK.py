"""Auto-generated file, do not edit by hand. DK metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DK = PhoneMetadata(id='DK', country_code=45, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3[2-9]|4[3-9]|5[4-9]|6[2-9]|7[02-9]|8[26-9]|9[6-9])\d{6}', possible_number_pattern=u'\d{8}', example_number=u'32123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:2[0-9]|3[0-2]|4[0-2]|5[0-3]|6[01]|7[12]|81|99)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'20123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([1-9]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
