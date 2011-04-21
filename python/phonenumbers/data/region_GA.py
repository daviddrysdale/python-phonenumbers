"""Auto-generated file, do not edit by hand. GA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GA = PhoneMetadata(id='GA', country_code=241, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[4-9]\d{5}|0\d{7}', possible_number_pattern=u'\d{6,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:4(?:[04-8]\d|2[04])|(?:5[04-689]|6[024-9]|7\d|8[236]|9[02368])\d)\d{3}', possible_number_pattern=u'\d{6}', example_number=u'441234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'0(?:5(?:0[89]|3[0-4]|8[0-26]|9[238])|6(?:0[3-7]|1[01]|2[0-7]|6[0-589]|71|83|9[57])|7(?:1[2-5]|2[89]|3[35-9]|4[01]|5[0-347-9]|[67]\d|8[457-9]|9[0146]))\d{4}', possible_number_pattern=u'\d{8}', example_number=u'06031234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[4-9]']),
        NumberFormat(pattern='(0\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['0'])],
    leading_zero_possible=True)
