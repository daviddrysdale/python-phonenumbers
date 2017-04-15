"""Auto-generated file, do not edit by hand. AL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AL = PhoneMetadata(id='AL', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[15]\\d{2,5}', possible_length=(3, 5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|2[789])', example_number='129', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:2|6(?:000|1(?:06|11|23)))|2[5-9])|5\\d{4}', example_number='129', possible_length=(3, 5, 6)),
    short_data=True)
