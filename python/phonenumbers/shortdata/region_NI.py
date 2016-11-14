"""Auto-generated file, do not edit by hand. NI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NI = PhoneMetadata(id='NI', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[12467]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(national_number_pattern='7373', possible_number_pattern='\\d{4}', example_number='7373', possible_length=(4,)),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[58]|2[08])', possible_number_pattern='\\d{3}', example_number='118', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[58]|2(?:[158]|00?)|900)|2100|4878|6100|7(?:010|100|373)', possible_number_pattern='\\d{3,4}', example_number='118', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
