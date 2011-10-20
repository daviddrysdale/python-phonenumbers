"""Auto-generated file, do not edit by hand. SO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SO = PhoneMetadata(id='SO', country_code=252, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-69]\\d{6,8}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:5[57-9]|6[19]\\d{2}|[134]\\d)\\d{5}', possible_number_pattern='\\d{7,9}', example_number='5522010'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:15|24|62|9[01])\\d{6}', possible_number_pattern='\\d{8}', example_number='90792024'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['[13-5]']),
        NumberFormat(pattern='(2)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['2']),
        NumberFormat(pattern='([169]\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['15|62|9']),
        NumberFormat(pattern='(61)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['61']),
        NumberFormat(pattern='(699)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['699'])])
