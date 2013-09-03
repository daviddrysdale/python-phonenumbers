"""Auto-generated file, do not edit by hand. ML metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ML = PhoneMetadata(id='ML', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1367]\\d{1,4}', possible_number_pattern='\\d{2,5}'),
    toll_free=PhoneNumberDesc(national_number_pattern='35200|67(?:00|77)|74(?:02|44)', possible_number_pattern='\\d{4,5}', example_number='35200'),
    premium_rate=PhoneNumberDesc(national_number_pattern='122[13]|3(?:52(?:11|2[02]|3[04-6]|99)|7574)', possible_number_pattern='\\d{4,5}', example_number='35211'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:12|[578])', possible_number_pattern='\\d{2,3}', example_number='17'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:2|[013-9]\\d)|2(?:1[02-469]|2[13])|[578])|3(?:5(?:0(?:35|57)|2(?:00|11|2[02]|3[04-6]5[0-25-8]|6[0-69]|7[0-47]|80|99))|6(?:666|777)|7(?:4\\d{2}|5(?:05|1[59]|25|5[57]|7[45])))|67(?:0[09]|59|77|8[89]|99)|74(?:0[02]|44|55)', possible_number_pattern='\\d{2,5}', example_number='1210'),
    standard_rate=PhoneNumberDesc(national_number_pattern='37(?:433|575)|7400', possible_number_pattern='\\d{4,5}', example_number='7400'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='3(?:5035|6\\d{3})', possible_number_pattern='\\d{5}', example_number='35035'),
    short_data=True)
