"""Auto-generated file, do not edit by hand. HT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HT = PhoneMetadata(id='HT', country_code=509, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-489]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:[24]\d|5[1-5]|94)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'22453300'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:3[4-9]|4\d)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'34101234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8\d{7}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'98[89]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'98901234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{4})', format=u'\\1 \\2 \\3')])
