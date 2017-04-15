"""Auto-generated file, do not edit by hand. KZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KZ = PhoneMetadata(id='KZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[134]\\d{2,4}', possible_length=(3, 4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[123]|12)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[123]|12)|30400|4040', example_number='112', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='30400|4040', example_number='30400', possible_length=(4, 5)),
    short_data=True)
