"""Auto-generated file, do not edit by hand. SG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SG = PhoneMetadata(id='SG', country_code=65, international_prefix='0[0-3][0-9]',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[36]\d{7}|[17-9]\d{7,10}', possible_number_pattern=u'\d{8,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'6[1-8]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'61234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:8[1-5]|9[0-8])\d{6}', possible_number_pattern=u'\d{8}', example_number=u'81234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'1?800\d{7}', possible_number_pattern=u'\d{10,11}', example_number=u'18001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'1900\d{7}', possible_number_pattern=u'\d{11}', example_number=u'19001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'3[0-2]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'31234567'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'7000\d{7}', possible_number_pattern=u'\d{11}', example_number=u'70001234567'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([3689]\d{3})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[369]|8[1-9]']),
        NumberFormat(pattern='(1[89]00)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[89]']),
        NumberFormat(pattern='(7000)(\d{4})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['70']),
        NumberFormat(pattern='(800)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['80'])])
