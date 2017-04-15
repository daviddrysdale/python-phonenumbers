"""Auto-generated file, do not edit by hand. MF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MF = PhoneMetadata(id='MF', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[56]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='590(?:[02][79]|13|5[0-268]|[78]7)\\d{4}', example_number='590271234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='690(?:0[0-7]|[1-9]\\d)\\d{4}', example_number='690301234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0')
