"""Auto-generated file, do not edit by hand. RS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RS = PhoneMetadata(id='RS', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{1,5}', possible_number_pattern='\\d{2,6}', possible_length=(2, 3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='112|9[234]', possible_number_pattern='\\d{2,3}', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1[189]\\d{1,4}|9[234]', possible_number_pattern='\\d{2,6}', example_number='112', possible_length=(2, 3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
