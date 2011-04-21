"""Auto-generated file, do not edit by hand. IT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IT = PhoneMetadata(id='IT', country_code=39, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[0389]\d{5,10}', possible_number_pattern=u'\d{6,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'0\d{9,10}', possible_number_pattern=u'\d{10,11}'),
    mobile=PhoneNumberDesc(national_number_pattern=u'3\d{8,9}', possible_number_pattern=u'\d{9,10}'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80(?:0\d{6}|3\d{3})', possible_number_pattern=u'\d{6,9}'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'89(?:2\d{3}|9\d{6})', possible_number_pattern=u'\d{6,9}'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['0[26]']),
        NumberFormat(pattern='(\d{3})(\d{4})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['0[13-57-9]']),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3']),
        NumberFormat(pattern='(\d{3})(\d{3,6})', format=u'\\1 \\2', leading_digits_pattern=['8'])],
    leading_zero_possible=True)
