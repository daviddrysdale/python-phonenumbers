"""Auto-generated file, do not edit by hand. OM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_OM = PhoneMetadata(id='OM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='9\\d{3}', possible_number_pattern='\\d{4}', possible_length=(4,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='9999', possible_number_pattern='\\d{4}', example_number='9999', possible_length=(4,)),
    short_code=PhoneNumberDesc(national_number_pattern='9999', possible_number_pattern='\\d{4}', example_number='9999', possible_length=(4,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
