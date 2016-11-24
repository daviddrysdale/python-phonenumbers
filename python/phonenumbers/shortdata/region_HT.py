"""Auto-generated file, do not edit by hand. HT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HT = PhoneMetadata(id='HT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,4}', possible_number_pattern='\\d{3,5}', possible_length=(3, 5)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='11[48]', possible_number_pattern='\\d{3}', example_number='118', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[48]|40404', possible_number_pattern='\\d{3,5}', example_number='114', possible_length=(3, 5)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='40404', possible_number_pattern='\\d{5}', example_number='40404', possible_length=(5,)),
    short_data=True)
