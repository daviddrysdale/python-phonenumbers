"""Auto-generated file, do not edit by hand. ML metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ML = PhoneMetadata(id='ML', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[136-8]\\d{1,4}', possible_length=(2, 3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='1[578]|35200|67(?:00|7\\d)|74(?:02|4\\d)|8000\\d', example_number='15', possible_length=(2, 4, 5)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:12|800)2\\d|3(?:52(?:11|2[02]|3[04-6]|99)|7574)', example_number='1220', possible_length=(4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='1[578]', example_number='15', possible_length=(2,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:[013-9]\\d|2)|2(?:1[02-469]|2[13])|[578])|3(?:5(?:0(?:35|57)|2\\d\\d)|[67]\\d{3})|67(?:0[09]|[59]9|77|8[89])|74(?:0[02]|44|55)|800[0-2][12]', example_number='15', possible_length=(2, 3, 4, 5)),
    standard_rate=PhoneNumberDesc(national_number_pattern='37(?:433|575)|7400|8001\\d', example_number='7400', possible_length=(4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='(?:3(?:503|[67]\\d\\d)|800\\d)\\d', example_number='35030', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='3(?:6\\d{3}|7(?:4(?:0[24-9]|[1-9]\\d)|5\\d\\d))|7400', example_number='7400', possible_length=(4, 5)),
    short_data=True)
