"""Auto-generated file, do not edit by hand. MG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MG = PhoneMetadata(id='MG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,2}', possible_number_pattern='\\d{2,3}', possible_length=(2, 3)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='11?[78]', possible_number_pattern='\\d{2,3}', example_number='117', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='11?[78]', possible_number_pattern='\\d{2,3}', example_number='117', possible_length=(2, 3)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
