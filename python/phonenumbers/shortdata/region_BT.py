"""Auto-generated file, do not edit by hand. BT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BT = PhoneMetadata(id='BT', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='11[023]', example_number='113', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[0-6]|40404', example_number='113', possible_length=(3, 5)),
    short_data=True)
