"""Auto-generated file, do not edit by hand. HT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HT = PhoneMetadata(id='HT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='11[48]', example_number='118', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[48]|40404', example_number='114', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', example_number='40404', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='40404', example_number='40404', possible_length=(5,)),
    short_data=True)
