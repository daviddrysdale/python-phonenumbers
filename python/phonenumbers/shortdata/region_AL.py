"""Auto-generated file, do not edit by hand. AL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AL = PhoneMetadata(id='AL', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[15]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:3[15]|41|16\\d{3})', example_number='116000', possible_length=(3, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='5\\d{4}', example_number='50123', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|2[7-9])', example_number='129', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:\\d|6(?:000|1(?:06|11|23))|8\\d{2})|2[2-9]|[349]\\d|65\\d|89[12])|5\\d{4}', example_number='129', possible_length=(3, 4, 5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='123', example_number='123', possible_length=(3,)),
    sms_services=PhoneNumberDesc(national_number_pattern='131|5\\d{4}', example_number='51234', possible_length=(3, 5)),
    short_data=True)
