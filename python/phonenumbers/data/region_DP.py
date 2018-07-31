"""Auto-generated file, do not edit by hand. 800 metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DP = PhoneMetadata(id='DP', country_code=803, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{10}', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='\\d{10}', possible_length=(10,)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{7})', format='\\1\\2')],
    leading_zero_possible=False)
