"""Auto-generated file, do not edit by hand. SB metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SB = PhoneMetadata(id='SB', country_code=677, international_prefix='0[01]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-8]\\d{4,6}', possible_number_pattern='\\d{5,7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[4-79]|[23]\\d|4[01]|5[03]|6[0-37])\\d{3}', possible_number_pattern='\\d{5}', example_number='40123'),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:4\\d|5[025-8]|6[01])\\d{4}|8[4-8]\\d{5}', possible_number_pattern='\\d{7}', example_number='7421234'),
    toll_free=PhoneNumberDesc(national_number_pattern='1[38]\\d{3}', possible_number_pattern='\\d{5}', example_number='18123'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='5[12]\\d{3}', possible_number_pattern='\\d{5}', example_number='51123'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='999', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[78]'])])
