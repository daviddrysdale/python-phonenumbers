"""Auto-generated file, do not edit by hand. GM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GM = PhoneMetadata(id='GM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,2}', possible_length=(2, 3)),
    emergency=PhoneNumberDesc(national_number_pattern='1?1[678]', example_number='117', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='1?1[678]', example_number='117', possible_length=(2, 3)),
    short_data=True)
