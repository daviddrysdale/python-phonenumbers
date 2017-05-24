"""Auto-generated file, do not edit by hand. BO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BO = PhoneMetadata(id='BO', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='11[089]', example_number='110', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[089]|40404', example_number='110', possible_length=(3, 5)),
    short_data=True)
