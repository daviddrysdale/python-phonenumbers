"""Auto-generated file, do not edit by hand. MW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MW = PhoneMetadata(id='MW', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[189]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='199|99[789]', example_number='997', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='199|80400|99[789]', example_number='997', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='80400', example_number='80400', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='80400', example_number='80400', possible_length=(5,)),
    short_data=True)
