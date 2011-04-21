"""Auto-generated file, do not edit by hand. SC metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SC = PhoneMetadata(id='SC', country_code=248, international_prefix='0[0-2]',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-8]\d{5,6}', possible_number_pattern=u'\d{6,7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:1[78]|2[14-69]|3[2-4]|4[1-36-8]|6[167]|[89]\d)|3(?:2[1-6]|4[4-6]|55|6[016]|7\d|8[0-589]|9[0-5])|5(?:5\d|6[0-2])|6(?:0[0-27-9]|1[0-478]|2[145]|3[02-4]|4[124]|6[015]|7\d|8[1-3])|78[0138])\d{3}', possible_number_pattern=u'\d{6}', example_number=u'217123'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5(?:[1247-9]\d|6[3-9])|7(?:[14679]\d|2[1-9]|8[24-79]))\d{3}', possible_number_pattern=u'\d{6}', example_number=u'510123'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8000\d{2}', possible_number_pattern=u'\d{6}', example_number=u'800000'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'(?:44[1-3]|647)\d{4}', possible_number_pattern=u'\d{7}', example_number=u'4410123'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'00',
    number_format=[NumberFormat(pattern='(\d{3})(\d{3})', format=u'\\1 \\2', leading_digits_pattern=['[23578]|[46][0-35-9]']),
        NumberFormat(pattern='(\d)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[46]4'])])
