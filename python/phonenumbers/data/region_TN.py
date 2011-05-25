"""Auto-generated file, do not edit by hand. TN metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TN = PhoneMetadata(id='TN', country_code=216, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[247-9]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='7\\d{7}', possible_number_pattern='\\d{8}', example_number='71234567'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[29]\\d|4[01])\\d{6}', possible_number_pattern='\\d{8}', example_number='20123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='8[028]\\d{6}', possible_number_pattern='\\d{8}', example_number='80123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='([247-9]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3')])
