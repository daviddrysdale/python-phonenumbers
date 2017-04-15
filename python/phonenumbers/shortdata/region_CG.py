"""Auto-generated file, do not edit by hand. CG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CG = PhoneMetadata(id='CG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='11\\d', possible_length=(3,)),
    toll_free=PhoneNumberDesc(national_number_pattern='111', example_number='111', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[78]', example_number='117', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[12678]', example_number='117', possible_length=(3,)),
    short_data=True)
