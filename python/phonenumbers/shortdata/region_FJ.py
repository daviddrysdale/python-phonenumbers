"""Auto-generated file, do not edit by hand. FJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FJ = PhoneMetadata(id='FJ', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[0-579]\\d{1,4}', possible_length=(2, 3, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='91[17]', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:1[34]|8[1-4])|1(?:0[1-3]|[25]9)|2[289]|30|4(?:0404|4)|54|75|91[137]', example_number='22', possible_length=(2, 3, 5)),
    short_data=True)
