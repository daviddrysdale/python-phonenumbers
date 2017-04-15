"""Auto-generated file, do not edit by hand. UZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UZ = PhoneMetadata(id='UZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[04]\\d{1,4}', possible_length=(2, 3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:0[123]|[123]|50)', example_number='01', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:0[123]|[123]|50)|45400', example_number='01', possible_length=(2, 3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='45400', example_number='45400', possible_length=(5,)),
    short_data=True)
