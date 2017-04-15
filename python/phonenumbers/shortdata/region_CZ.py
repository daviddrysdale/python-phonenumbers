"""Auto-generated file, do not edit by hand. CZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CZ = PhoneMetadata(id='CZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116(?:00[06]|111|123)', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|5[0568])', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:2|6\\d{3}|8\\d)|2\\d{2,3}|3\\d{3,4}|4\\d{3}|5[0568]|99)', example_number='116123', possible_length=(3, 4, 5, 6)),
    short_data=True)
