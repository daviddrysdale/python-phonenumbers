"""Auto-generated file, do not edit by hand. SJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SJ = PhoneMetadata(id='SJ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[023]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[023]', example_number='112', possible_length=(3,)),
    short_data=True)
