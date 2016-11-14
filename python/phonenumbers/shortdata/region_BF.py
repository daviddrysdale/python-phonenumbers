"""Auto-generated file, do not edit by hand. BF metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BF = PhoneMetadata(id='BF', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d', possible_number_pattern='\\d{2}', possible_length=(2,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1[78]', possible_number_pattern='\\d{2}', example_number='17', possible_length=(2,)),
    short_code=PhoneNumberDesc(national_number_pattern='1[78]', possible_number_pattern='\\d{2}', example_number='17', possible_length=(2,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
