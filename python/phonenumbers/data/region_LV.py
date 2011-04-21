"""Auto-generated file, do not edit by hand. LV metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LV = PhoneMetadata(id='LV', country_code=371, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2689]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'6\d{7}', possible_number_pattern=u'\d{8}', example_number=u'61234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'2\d{7}', possible_number_pattern=u'\d{8}', example_number=u'21234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([2689]\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3')])
