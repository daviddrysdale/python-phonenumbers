"""Auto-generated file, do not edit by hand. CM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CM = PhoneMetadata(id='CM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[18]\\d{1,3}', possible_length=(2, 3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1?1[37]', example_number='113', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1?1[37]|8711', example_number='113', possible_length=(2, 3, 4)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='8711', example_number='8711', possible_length=(4,)),
    sms_services=PhoneNumberDesc(national_number_pattern='8711', example_number='8711', possible_length=(4,)),
    short_data=True)
