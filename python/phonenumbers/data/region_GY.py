"""Auto-generated file, do not edit by hand. GY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GY = PhoneMetadata(id='GY', country_code=592, international_prefix='001',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-4679]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:1[6-9]|2[0-35-9]|3[1-4]|5[3-9]|6\d|7[0-24-79])|3(?:2[25-9]|3\d)|4(?:4[0-24]|5[56])|77[1-57])\d{4}', possible_number_pattern=u'\d{7}', example_number=u'2201234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6\d{6}', possible_number_pattern=u'\d{7}', example_number=u'6091234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'(?:289|862)\d{4}', possible_number_pattern=u'\d{7}', example_number=u'2891234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9008\d{3}', possible_number_pattern=u'\d{7}', example_number=u'9008123'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2')])
