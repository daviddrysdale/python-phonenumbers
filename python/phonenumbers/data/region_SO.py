"""Auto-generated file, do not edit by hand. SO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SO = PhoneMetadata(id='SO', country_code=252, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13-59]\d{6,7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:5[57-9]|[134]\d)\d{5}', possible_number_pattern=u'\d{7}', example_number=u'5522010'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:9[01]|15)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90792024'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([13-5])(\d{6})', format=u'\\1 \\2', leading_digits_pattern=['[13-5]']),
        NumberFormat(pattern='([19]\d)(\d{6})', format=u'\\1 \\2', leading_digits_pattern=['15|9'])])
