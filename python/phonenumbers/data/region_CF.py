"""Auto-generated file, do not edit by hand. CF metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CF = PhoneMetadata(id='CF', country_code=236, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[278]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[12]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'21612345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[0257]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'70012345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'8776\d{4}', possible_number_pattern=u'\d{8}', example_number=u'87761234'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
