"""Auto-generated file, do not edit by hand. AE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AE = PhoneMetadata(id='AE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[149]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112|99[789]', possible_number_pattern='\\d{3,4}', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='112|445[16]|99[789]', possible_number_pattern='\\d{3,4}', example_number='112', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
