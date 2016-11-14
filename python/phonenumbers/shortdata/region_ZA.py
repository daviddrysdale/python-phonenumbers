"""Auto-generated file, do not edit by hand. ZA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[134]\\d{2,4}', possible_number_pattern='\\d{3,5}', possible_length=(3, 5)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:01(?:11|77)|12)', possible_number_pattern='\\d{3,5}', example_number='10111', possible_length=(3, 5)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:01(?:11|77)|12)|37567|47751', possible_number_pattern='\\d{3,5}', example_number='10111', possible_length=(3, 5)),
    standard_rate=PhoneNumberDesc(national_number_pattern='37567|47751', possible_number_pattern='\\d{5}', example_number='47751', possible_length=(5,)),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
