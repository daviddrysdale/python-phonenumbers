"""Auto-generated file, do not edit by hand. NI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NI = PhoneMetadata(id='NI', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[12467]\\d{2,3}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1[58]|2[08])|737\\d', example_number='115', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[58]|2[08])', example_number='115', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[58]|[29]00)|[26]100|4878|7(?:(?:01|10)0|373)|12[0158]', example_number='115', possible_length=(3, 4)),
    short_data=True)
