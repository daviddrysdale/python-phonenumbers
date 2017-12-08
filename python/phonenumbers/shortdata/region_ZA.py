"""Auto-generated file, do not edit by hand. ZA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[134]\\d{2,4}', possible_length=(3, 4, 5)),
    premium_rate=PhoneNumberDesc(national_number_pattern='41(?:348|851)', example_number='41851', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0(?:1(?:11|77)|7)|12)', example_number='10111', possible_length=(3, 5)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:1(?:11|77)|20|7)|1[12]|77(?:3[237]|[45]7|6[279]|9[26]))|[34]\\d{4}', example_number='10111', possible_length=(3, 4, 5)),
    standard_rate=PhoneNumberDesc(national_number_pattern='3(?:078[23]|7(?:064|567)|8126)|4(?:3(?:699|946)|7751)', example_number='47751', possible_length=(5,)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:07|11)', example_number='111', possible_length=(3,)),
    sms_services=PhoneNumberDesc(national_number_pattern='[34]\\d{4}', example_number='47751', possible_length=(5,)),
    short_data=True)
