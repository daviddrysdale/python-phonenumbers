"""Auto-generated file, do not edit by hand. IQ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IQ = PhoneMetadata(id='IQ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1479]\\d{2,4}', possible_number_pattern='\\d{3,5}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[04]|15|22)', possible_number_pattern='\\d{3}', example_number='122', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[04]|15|22)|4432|71117|9988', possible_number_pattern='\\d{3,5}', example_number='4432', possible_length=(3, 4, 5)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='4432|71117|9988', possible_number_pattern='\\d{3,5}', example_number='4432', possible_length=(4, 5)),
    short_data=True)
