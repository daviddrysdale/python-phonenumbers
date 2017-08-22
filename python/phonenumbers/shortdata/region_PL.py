"""Auto-generated file, do not edit by hand. PL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PL = PhoneMetadata(id='PL', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}(?:\\d{2,3})?|9\\d{2}', possible_length=(3, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116\\d{3}', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='112|99[789]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:2|6(?:000|1(?:11|23))|8(?:000|91[23]))|9\\d{3})|9(?:8[4-7]|9[1-9])', example_number='112', possible_length=(3, 5, 6)),
    short_data=True)
