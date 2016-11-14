"""Auto-generated file, do not edit by hand. BZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BZ = PhoneMetadata(id='BZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='9\\d{1,2}', possible_number_pattern='\\d{2,3}', possible_length=(2, 3)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='9(?:0|11)', possible_number_pattern='\\d{2,3}', example_number='911', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='9(?:0|11)', possible_number_pattern='\\d{2,3}', example_number='911', possible_length=(2, 3)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
