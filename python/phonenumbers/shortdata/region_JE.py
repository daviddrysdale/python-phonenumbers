"""Auto-generated file, do not edit by hand. JE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JE = PhoneMetadata(id='JE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[129]\\d{2,5}', possible_length=(3, 4, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:00|1(?:2|8\\d{3})|23|4(?:[14]|28|7\\d)|5\\d|7(?:0[12]|[128]|35?)|808|9[135])|23[234]|999', example_number='150', possible_length=(3, 4, 6)),
    short_data=True)
