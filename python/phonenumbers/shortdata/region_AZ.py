"""Auto-generated file, do not edit by hand. AZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AZ = PhoneMetadata(id='AZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[148]\\d{2,3}', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[123]|12)', example_number='101', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[123]|12)|4040|8800', example_number='101', possible_length=(3, 4)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='4040|8800', example_number='4040', possible_length=(4,)),
    sms_services=PhoneNumberDesc(national_number_pattern='4040|8800', example_number='4040', possible_length=(4,)),
    short_data=True)
