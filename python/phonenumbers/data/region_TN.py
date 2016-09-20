"""Auto-generated file, do not edit by hand. TN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TN = PhoneMetadata(id='TN', country_code=216, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-57-9]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='3(?:[012]\\d|6[0-4]|91)\\d{5}|7\\d{7}|81200\\d{3}', possible_number_pattern='\\d{8}', example_number='71234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[259]\\d|4[0-6])\\d{6}', possible_number_pattern='\\d{8}', example_number='20123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8010\\d{4}', possible_number_pattern='\\d{8}', example_number='80101234', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='88\\d{6}', possible_number_pattern='\\d{8}', example_number='88123456', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8[12]10\\d{4}', possible_number_pattern='\\d{8}', example_number='81101234', possible_length=(8,)),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3')])
