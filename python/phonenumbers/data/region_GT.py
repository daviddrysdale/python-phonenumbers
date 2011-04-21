"""Auto-generated file, do not edit by hand. GT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GT = PhoneMetadata(id='GT', country_code=502, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-7]\d{7}|1[89]\d{9}', possible_number_pattern=u'\d{8}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[267][2-9]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'22456789'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[345]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'51234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'18[01]\d{8}', possible_number_pattern=u'\d{11}', example_number=u'18001112222'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'19\d{9}', possible_number_pattern=u'\d{11}', example_number=u'19001112222'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[2-7]']),
        NumberFormat(pattern='(\d{4})(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'])])
