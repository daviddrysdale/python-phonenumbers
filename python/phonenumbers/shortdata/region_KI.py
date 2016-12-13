"""Auto-generated file, do not edit by hand. KI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KI = PhoneMetadata(id='KI', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[179]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='19[2-5]|99[2349]', possible_number_pattern='\\d{3}', example_number='192', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[0-8]|5[01259])|88|9[2-5])|777|99[2349]', possible_number_pattern='\\d{3,4}', example_number='100', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(national_number_pattern='103', possible_number_pattern='\\d{3}', example_number='103', possible_length=(3,)),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
