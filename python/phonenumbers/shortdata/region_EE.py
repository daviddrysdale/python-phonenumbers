"""Auto-generated file, do not edit by hand. EE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EE = PhoneMetadata(id='EE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116(?:000|111)', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[02]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:\\d{2}|16(?:000|111))', example_number='116', possible_length=(3, 6)),
    short_data=True)
