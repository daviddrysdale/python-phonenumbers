"""Auto-generated file, do not edit by hand. BQ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BQ = PhoneMetadata(id='BQ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2}', possible_number_pattern='\\d{3}', possible_length=(3,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='112|911', possible_number_pattern='\\d{3}', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:12|76)|911', possible_number_pattern='\\d{3}', example_number='112', possible_length=(3,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='176', possible_number_pattern='\\d{3}', example_number='176', possible_length=(3,)),
    short_data=True)
