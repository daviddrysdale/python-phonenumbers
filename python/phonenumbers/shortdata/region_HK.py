"""Auto-generated file, do not edit by hand. HK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HK = PhoneMetadata(id='HK', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,6}', possible_length=(3, 4, 5, 6, 7)),
    emergency=PhoneNumberDesc(national_number_pattern='112|99[29]', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[0136]\\d{0,4}|2[14]\\d{0,3}|8[138]|9)|12|2(?:[0-3]\\d{0,4}|58\\d{0,3}|8[13]\\d{0,3})|7(?:[135-9]\\d{0,4}|21[89]\\d{0,2}|421\\d{0,2})|8(?:0(?:[13]\\d|60\\d{2}|8)|1(?:0\\d|[2-8])|2(?:0[5-9]|182|22|3|8[128])|3\\d{4}|4(?:1[1-5]|[23]1|6[12])|50[138]|6(?:000|1(?:[13]1|86)|8)|7(?:13|2[1-389]|8[0235-9]|93)\\d{2}|8\\d))|99[29]', example_number='999', possible_length=(3, 4, 5, 6, 7)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:0(?:8\\d|9)|850\\d)', example_number='1088', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='992', example_number='992', possible_length=(3,)),
    short_data=True)
