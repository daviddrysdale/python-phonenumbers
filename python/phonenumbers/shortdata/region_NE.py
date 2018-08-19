"""Auto-generated file, do not edit by hand. NE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NE = PhoneMetadata(id='NE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-3578]\\d(?:\\d(?:\\d{3})?)?', possible_length=(2, 3, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='1[578]|723141', example_number='17', possible_length=(2, 6)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[01]|1[12]|2[034]|3[013]|40|55?|60|7|8)|222|333|555|723141|888', example_number='112', possible_length=(2, 3, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:0[01]|1[12]|2[034]|3[013]|40|55|60)|222|333|555|888', example_number='100', possible_length=(3,)),
    short_data=True)
