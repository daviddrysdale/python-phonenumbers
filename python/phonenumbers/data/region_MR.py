"""Auto-generated file, do not edit by hand. MR metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MR = PhoneMetadata(id='MR', country_code=222, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-48]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'25[08]\d{5}|35\d{6}|45[1-7]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'35123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:2(?:2\d|70)|3(?:3\d|6[1-36]|7[1-3])|4(?:4\d|6[0457-9]|7[4-9]))\d{5}', possible_number_pattern=u'\d{8}', example_number=u'22123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([2-48]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
