"""Auto-generated file, do not edit by hand. GH metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GH = PhoneMetadata(id='GH', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14589]\\d{2,4}', possible_length=(3, 4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='19[123]|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='19[123]|40404|(?:54|83)00|999', example_number='999', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404|(?:54|83)00', example_number='5400', possible_length=(4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='40404|(?:54|83)00', example_number='5400', possible_length=(4, 5)),
    short_data=True)
