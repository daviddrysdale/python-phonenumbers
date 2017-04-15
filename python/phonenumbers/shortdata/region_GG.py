"""Auto-generated file, do not edit by hand. GG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GG = PhoneMetadata(id='GG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[01]|1(?:[12]|[68]\\d{3})|23|4(?:1|7\\d)|55|800\\d|95)|999', example_number='155', possible_length=(3, 4, 5, 6)),
    short_data=True)
