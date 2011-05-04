"""Auto-generated file, do not edit by hand. BZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BZ = PhoneMetadata(id='BZ', country_code=501, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-8]\d{6}|0\d{10}', possible_number_pattern=u'\d{7}(?:\d{4})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[234578][02]\d{5}', possible_number_pattern=u'\d{7}', example_number=u'2221234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6(?:[0-2]\d|[67][01])\d{4}', possible_number_pattern=u'\d{7}', example_number=u'6221234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'0800\d{7}', possible_number_pattern=u'\d{11}', example_number=u'08001234123'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1-\\2', leading_digits_pattern=['[2-8]']),
        NumberFormat(pattern='(0)(800)(\d{4})(\d{3})', format=u'\\1-\\2-\\3-\\4', leading_digits_pattern=['0'])],
    leading_zero_possible=True)
