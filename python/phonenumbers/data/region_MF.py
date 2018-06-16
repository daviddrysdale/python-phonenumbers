"""Auto-generated file, do not edit by hand. MF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MF = PhoneMetadata(id='MF', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[56]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='590(?:0[079]|13|2[79]|30|43|5[0-268]|7[79]|87)\\d{4}', example_number='590271234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='69(?:0\\d{2}|1(?:2[29]|3[0-5]))\\d{4}', example_number='690001234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    mobile_number_portable_region=True)
