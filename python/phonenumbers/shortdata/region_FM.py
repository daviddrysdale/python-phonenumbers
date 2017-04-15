"""Auto-generated file, do not edit by hand. FM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FM = PhoneMetadata(id='FM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='3\\d{5}|9\\d{2}', possible_length=(3, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='320221|911', example_number='911', possible_length=(3, 6)),
    short_code=PhoneNumberDesc(national_number_pattern='320221|911', example_number='911', possible_length=(3, 6)),
    short_data=True)
