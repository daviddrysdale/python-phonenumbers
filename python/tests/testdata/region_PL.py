"""Auto-generated file, do not edit by hand. PL metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PL = PhoneMetadata(id='PL', country_code=48, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{8}', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:5[01]|6[069]|7[289]|88)\\d{7}', example_number='501234567', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='70\\d{7}', example_number='701234567', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', national_prefix_formatting_rule='0\\1')])
