"""Auto-generated file, do not edit by hand. UZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UZ = PhoneMetadata(id='UZ', country_code=998, international_prefix='8~10',
    general_desc=PhoneNumberDesc(national_number_pattern='[679]\\d{8}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:6[125679]|7[0-69])\\d{7}', possible_number_pattern='\\d{7,9}', example_number='612345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9[0-57-9]\\d{7}', possible_number_pattern='\\d{7,9}', example_number='912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='([679]\\d)(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3 \\4', national_prefix_formatting_rule=u'8\\1')])
