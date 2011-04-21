"""Auto-generated file, do not edit by hand. GL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GL = PhoneMetadata(id='GL', country_code=299, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-689]\d{5}', possible_number_pattern=u'\d{6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:19|3[1-6]|6[14689]|8[14-79]|9\d)\d{4}', possible_number_pattern=u'\d{6}', example_number=u'321000'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[245][2-9]\d{4}', possible_number_pattern=u'\d{6}', example_number=u'221234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{4}', possible_number_pattern=u'\d{6}', example_number=u'801234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'3[89]\d{4}', possible_number_pattern=u'\d{6}', example_number=u'381234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3')])
