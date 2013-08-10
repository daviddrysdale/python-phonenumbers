"""Auto-generated file, do not edit by hand. FO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FO = PhoneMetadata(id='FO', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,3}', possible_number_pattern='\\d{3,4}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[48]|4[124]\\d|71\\d|8[7-9]\\d)', possible_number_pattern='\\d{3,4}', example_number='114'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
