"""Auto-generated file, do not edit by hand. NF metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NF = PhoneMetadata(id='NF', country_code=672, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13]\d{5}', possible_number_pattern=u'\d{5,6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1(?:06|17|28|39)|3[012]\d)\d{3}', possible_number_pattern=u'\d{5,6}', example_number=u'106609'),
    mobile=PhoneNumberDesc(national_number_pattern=u'38\d{4}', possible_number_pattern=u'\d{5,6}', example_number=u'381234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\d)(\d{5})', format=u'\\1 \\2', leading_digits_pattern=['3'])])
