"""Auto-generated file, do not edit by hand. ES metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ES = PhoneMetadata(id='ES', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[0-379]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='0(?:16|6[57]|88)|1(?:006|16\\d{3}|[3-7]\\d{2})|20\\d{4}', example_number='116111', possible_length=(3, 4, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1(?:18\\d{2}|2\\d{1,4})|2(?:2\\d{1,4}|[3-9]\\d{3,4})|9(?:0(?:5[124578]|7)|\\d{4,5})|[37]\\d{4,5}', example_number='23456', possible_length=(3, 4, 5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='08[58]|112', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='0(?:1[0-26]|6[0-257]|8[058]|9[12])|1(?:0[03-57]\\d{1,3}|1(?:2|6(?:000|111)|8\\d{2})|2\\d{1,4}|3(?:[34]|\\d{2})|7(?:7|\\d{2})|[4-689]\\d{2})|2(?:[01]\\d{4}|2\\d{1,4}|[357]\\d{3}|80\\d{2})|3[357]\\d{3}|79[57]\\d{3}|9(?:0(?:5[124578]|7)|9[57]\\d{3})', example_number='010', possible_length=(3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='0(?:[16][0-2]|80|9[12])|21\\d{4}', example_number='211234', possible_length=(3, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:2\\d{1,4}|3[34]|77)|22\\d{1,4}', example_number='123', possible_length=(3, 4, 5, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='[2379]\\d{4,5}', example_number='23456', possible_length=(5, 6)),
    short_data=True)
