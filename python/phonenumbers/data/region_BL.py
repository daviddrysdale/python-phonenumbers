"""Auto-generated file, do not edit by hand. BL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BL = PhoneMetadata(id='BL', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[56]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='590(?:2[7-9]|5[12]|87)\\d{4}', example_number='590271234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='690(?:0[05-9]|[1-9]\\d)\\d{4}', example_number='690001234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0')
