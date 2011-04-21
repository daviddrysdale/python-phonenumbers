"""Auto-generated file, do not edit by hand. VA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VA = PhoneMetadata(id='VA', country_code=379, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'06\d{8}', possible_number_pattern=u'\d{10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'06698\d{5}', possible_number_pattern=u'\d{10}', example_number=u'0669812345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'N/A', possible_number_pattern=u'N/A'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(06)(\d{4})(\d{4})', format=u'\\1 \\2 \\3')],
    leading_zero_possible=True)
