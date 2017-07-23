"""Auto-generated file, do not edit by hand. ID metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ID = PhoneMetadata(id='ID', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[178]\\d{2,4}', possible_length=(3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='11[02389]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[02389]|40\\d{2})|71400|89887', example_number='112', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='71400|89887', example_number='71400', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='71400', example_number='71400', possible_length=(5,)),
    short_data=True)
