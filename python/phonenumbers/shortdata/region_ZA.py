"""Auto-generated file, do not edit by hand. ZA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[134]\\d{2,4}', possible_length=(3, 4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:01(?:11|77)|12)', example_number='10111', possible_length=(3, 5)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:1(?:11|77)|20)|12|3[24-7]|77(?:3[237]|[45]7|6[279]|9[26]))|37567|47751', example_number='10111', possible_length=(3, 4, 5)),
    standard_rate=PhoneNumberDesc(national_number_pattern='37567|47751', example_number='47751', possible_length=(5,)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='13[24-7]', example_number='132', possible_length=(3,)),
    short_data=True)
