"""Auto-generated file, do not edit by hand. SO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SO = PhoneMetadata(id='SO', country_code=252, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-79]\\d{6,8}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:5[57-9]|[1-4]\\d)\\d{5}', possible_number_pattern='\\d{7}', example_number='5522010'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:15|24|6[179]?\\d|7\\d|9[01])\\d{6}', possible_number_pattern='\\d{8,9}', example_number='90792024'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['[1-5]']),
        NumberFormat(pattern='(\\d)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['[267]']),
        NumberFormat(pattern='([19]\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['15|9']),
        NumberFormat(pattern='(6\\d)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['6[17]']),
        NumberFormat(pattern='(69\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['69'])])
