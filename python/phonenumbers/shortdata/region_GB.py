"""Auto-generated file, do not edit by hand. GB metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GB = PhoneMetadata(id='GB', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-46-9]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:05|16\\d{3}|7[56]0|8000)|2(?:202|48)|4444', example_number='116000', possible_length=(3, 4, 5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[015]|1(?:[12]|6(?:000|1(?:11|23))|8\\d{3})|2(?:[123]|50)|33|4(?:1|7\\d)|5(?:\\d|71)|7(?:0\\d|[56]0)|800\\d|9[15])|2(?:02(?:02)?|1300|2(?:02|11|2)|3(?:02|336|45)|4(?:25|8))|3[13]3|4(?:0[02]|35[01]|44[45]|5\\d)|6(?:50|\\d{4})|7(?:0\\d{3}|8(?:9|\\d{3})|9\\d{3})|8\\d{4}|9(?:01|99)', example_number='150', possible_length=(3, 4, 5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:250|571|7[56]0)|2(?:02(?:02)?|1300|3336|48)|4444|901', example_number='1571', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='1250|2(?:0202|1300)|7\\d{4}|8[01]\\d{3}', example_number='20202', possible_length=(4, 5)),
    short_data=True)
