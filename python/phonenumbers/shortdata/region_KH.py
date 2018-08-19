"""Auto-generated file, do not edit by hand. KH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KH = PhoneMetadata(id='KH', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[146]\\d\\d(?:\\d{2})?', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='11[789]|666', example_number='117', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[789]|40404|666', example_number='117', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', example_number='40404', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='40404', example_number='40404', possible_length=(5,)),
    short_data=True)
