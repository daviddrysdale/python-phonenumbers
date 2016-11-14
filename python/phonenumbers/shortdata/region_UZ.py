"""Auto-generated file, do not edit by hand. UZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UZ = PhoneMetadata(id='UZ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[04]\\d{1,4}', possible_number_pattern='\\d{2,5}', possible_length=(2, 3, 5)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='0(?:0[123]|[123]|50)', possible_number_pattern='\\d{2,3}', example_number='01', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:0[123]|[123]|50)|45400', possible_number_pattern='\\d{2,5}', example_number='01', possible_length=(2, 3, 5)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='45400', possible_number_pattern='\\d{5}', example_number='45400', possible_length=(5,)),
    short_data=True)
