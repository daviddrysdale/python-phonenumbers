"""Auto-generated file, do not edit by hand. SG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SG = PhoneMetadata(id='SG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[179]\\d{2,4}', possible_length=(3, 4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='99[359]', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:[0136]\\d{2}|[89](?:[1-9]\\d|0[1-9])|[57]\\d{2,3})|77222|99[02-9]', example_number='1312', possible_length=(3, 4, 5)),
    short_data=True)
