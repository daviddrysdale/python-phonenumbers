"""Auto-generated file, do not edit by hand. UA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UA = PhoneMetadata(id='UA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[189]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116(?:000|1(?:11|23))', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[1-3]|12)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[1-49]|6\\d{2})|1(?:2|6(?:000|1(?:11|23))|8\\d{1,2})|[278]\\d|4\\d{3}|5(?:1|\\d{2})|6\\d{2})|[89]00\\d{1,2}', example_number='112', possible_length=(3, 4, 5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='(?:118|[89]00)\\d{1,2}', example_number='11812', possible_length=(4, 5)),
    short_data=True)
