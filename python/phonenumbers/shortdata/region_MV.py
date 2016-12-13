"""Auto-generated file, do not edit by hand. MV metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MV = PhoneMetadata(id='MV', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[14]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:02|1[89])', possible_number_pattern='\\d{3}', example_number='102', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:[0-37-9]\\d|[45](?:1|\\d{2})|6\\d{2})|4040', possible_number_pattern='\\d{3,4}', example_number='123', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1[45]1', possible_number_pattern='\\d{3,4}', example_number='141', possible_length=(3,)),
    short_data=True)
