"""Auto-generated file, do not edit by hand. OM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_OM = PhoneMetadata(id='OM', country_code=968, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'(?:2[3-6]|5|9[2-9])\d{6}|800\d{5,6}', possible_number_pattern=u'\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[3-6]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'23123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9[2-9]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'92123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8007\d{4,5}|500\d{4}', possible_number_pattern=u'\d{7,9}', example_number=u'80071234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(2\d)(\d{6})', format=u'\\1 \\2', leading_digits_pattern=['2']),
        NumberFormat(pattern='(9\d{3})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['9']),
        NumberFormat(pattern='([58]00)(\d{4,6})', format=u'\\1 \\2', leading_digits_pattern=['[58]'])])
