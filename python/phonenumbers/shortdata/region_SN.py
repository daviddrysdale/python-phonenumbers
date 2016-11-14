"""Auto-generated file, do not edit by hand. SN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SN = PhoneMetadata(id='SN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[12]\\d{1,5}', possible_number_pattern='\\d{2,6}', possible_length=(2, 3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1515|2(?:00|1)\\d{3}', possible_number_pattern='\\d{4,6}', example_number='200133', possible_length=(4, 5, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='2(?:0[246]|[468])\\d{3}', possible_number_pattern='\\d{5,6}', example_number='202222', possible_length=(5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='1[78]', possible_number_pattern='\\d{2}', example_number='17', possible_length=(2,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[69]|2(?:\\d{2})?|[46]\\d{2}|51\\d|[78])|2(?:0[0-246]|[12468])\\d{3}', possible_number_pattern='\\d{2,6}', example_number='17', possible_length=(2, 3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='2(?:01|2)\\d{3}', possible_number_pattern='\\d{5,6}', example_number='201202', possible_length=(5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1[46]\\d{2}', possible_number_pattern='\\d{4}', example_number='1415', possible_length=(4,)),
    short_data=True)
