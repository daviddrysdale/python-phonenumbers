"""Auto-generated file, do not edit by hand. BA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BA = PhoneMetadata(id='BA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116\\d{3}', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='12[2-4]', example_number='122', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:6(?:00[06]|1(?:1[17]|23))|8\\d{1,2})|2(?:0[0-7]|[2-5]|6[0-26]|[78]\\d{1,2})|[3-5]\\d{2}|7\\d{3})', example_number='122', possible_length=(3, 4, 5, 6)),
    short_data=True)
