"""Auto-generated file, do not edit by hand. BR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BR = PhoneMetadata(id='BR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[12469]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:00|[89]\\d)|4(?:57|828)', example_number='181', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|28|9[023])|911', example_number='190', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[02]|3(?:1[2-579]|2[13-9]|3[124-9]|4[1-3578]|5[1-468]|6[139]|8[149]|9[168])|5[0-35-9]|6(?:0|1[0-35-8]?|2[0145]|3[0137]?|4[37-9]?|5[0-35]|6[016]?|7[137]?|8[5-8]|9[1359]))|1[25-8]|2[35789]|3(?:[024568]|3[12])|4[12568]|5\\d|6[0-8]|8[015]|9[0-4789])|2(?:7(?:330|878)|85959?)|4(?:0404?|11[12]|57|828)|55555|6(?:0\\d{4}|10000)|911', example_number='168', possible_length=(3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='102|27330', example_number='27330', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='151|27878|4(?:0404?|11[12]|57)|55555', example_number='27878', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='2(?:7(?:330|878)|85959?)|4(?:0404|828)|6(?:0\\d{4}|10000)', example_number='27878', possible_length=(4, 5, 6)),
    short_data=True)
