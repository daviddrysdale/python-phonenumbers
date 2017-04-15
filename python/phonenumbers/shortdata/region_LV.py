"""Auto-generated file, do not edit by hand. LV metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LV = PhoneMetadata(id='LV', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='0\\d|1\\d{2,6}|8\\d{3,4}', possible_length=(2, 3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116\\d{3}', example_number='116000', possible_length=(6,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1180|8(?:2\\d{3}|[89]\\d{2})', example_number='1180', possible_length=(4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='0[123]|11[023]', example_number='112', possible_length=(2, 3)),
    short_code=PhoneNumberDesc(national_number_pattern='0[1-4]|1(?:1(?:[02-4]|6(?:000|111)|8[0189])|55|655|77)|821[57]4', example_number='112', possible_length=(2, 3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='1181', example_number='1181', possible_length=(4,)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='16\\d{2}', example_number='1655', possible_length=(4,)),
    short_data=True)
