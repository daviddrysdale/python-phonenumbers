"""Auto-generated file, do not edit by hand. GA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GA = PhoneMetadata(id='GA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,3}', possible_number_pattern='\\d{2,4}', possible_length=(2, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:730|8|3\\d{2})', possible_number_pattern='\\d{2,4}', example_number='1730', possible_length=(2, 4)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:730|8|3\\d{2})', possible_number_pattern='\\d{2,4}', example_number='1730', possible_length=(2, 4)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
