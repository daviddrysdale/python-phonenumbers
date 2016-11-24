"""Auto-generated file, do not edit by hand. CM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CM = PhoneMetadata(id='CM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[18]\\d{1,3}', possible_number_pattern='\\d{2,4}', possible_length=(2, 3, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1?1[37]', possible_number_pattern='\\d{2,4}', example_number='113', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1?1[37]|8711', possible_number_pattern='\\d{2,4}', example_number='113', possible_length=(2, 3, 4)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='8711', possible_number_pattern='\\d{4}', example_number='8711', possible_length=(4,)),
    short_data=True)
