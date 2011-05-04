"""Auto-generated file, do not edit by hand. HK metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HK = PhoneMetadata(id='HK', country_code=852, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[235-7]\d{7}|8\d{7,8}|9\d{7,10}', possible_number_pattern=u'\d{8,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[23]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'21234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[5-79]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'51234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{8}', possible_number_pattern=u'\d{11}', example_number=u'90012345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'8[1-3]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'81123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[235-7]|[89](?:0[1-9]|[1-9])']),
        NumberFormat(pattern='(800)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['800']),
        NumberFormat(pattern='(900)(\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['900'])])
