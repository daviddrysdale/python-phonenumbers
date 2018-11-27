"""Auto-generated file, do not edit by hand. ER metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ER = PhoneMetadata(id='ER', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[12]\\d\\d(?:\\d{3})?', possible_length=(3, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1[2-46]|2[47]\\d{3})|20[12]\\d{3}', example_number='112', possible_length=(3, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[2-46]|2(?:4422|7799))|20(?:1(?:606|917)|2(?:099|914))', example_number='112', possible_length=(3, 6)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[2-6]|2(?:4422|7799))|20(?:1(?:606|917)|2(?:099|914))', example_number='112', possible_length=(3, 6)),
    short_data=True)
