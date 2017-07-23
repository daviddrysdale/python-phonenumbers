"""Auto-generated file, do not edit by hand. BW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BW = PhoneMetadata(id='BW', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='99[789]', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='13123|99[789]', example_number='999', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='13123', example_number='13123', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='13123', example_number='13123', possible_length=(5,)),
    short_data=True)
