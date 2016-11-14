"""Auto-generated file, do not edit by hand. LR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LR = PhoneMetadata(id='LR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[3489]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='355|911', possible_number_pattern='\\d{3}', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='355|4040|8(?:400|933)|911', possible_number_pattern='\\d{3,4}', example_number='911', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='4040|8(?:400|933)', possible_number_pattern='\\d{4}', example_number='8400', possible_length=(4,)),
    short_data=True)
