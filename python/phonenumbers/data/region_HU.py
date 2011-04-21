"""Auto-generated file, do not edit by hand. HU metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HU = PhoneMetadata(id='HU', country_code=36, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{8,9}', possible_number_pattern=u'\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1\d|2(?:1\d|[2-9])|3[2-7]|4[24-9]|5[2-79]|6[23689]|7(?:1\d|[2-9])|8[2-57-9]|9[2-69])\d{6}', possible_number_pattern=u'\d{6,9}', example_number=u'12345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:[27]0|3[01])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'201234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9[01]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'40\d{6}', possible_number_pattern=u'\d{8}', example_number=u'40123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'06',
    national_prefix_for_parsing=u'06',
    number_format=[NumberFormat(pattern='(1)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'(\\1)'),
        NumberFormat(pattern='(\d{2})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-9]'], national_prefix_formatting_rule=u'(\\1)')])
