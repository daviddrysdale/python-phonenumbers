"""Auto-generated file, do not edit by hand. US metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_US = PhoneMetadata(id='US', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='112|[69]11', example_number='112', possible_length=(3,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='2(?:4280|5209|7(?:449|663))|3(?:2340|3786|5564|8(?:135|254))|4(?:1(?:366|463)|3355|6(?:15|32)7|7553|82(?:21|77))|5(?:2944|4892|5928|9(?:187|342))|69388|7(?:20(?:78|87)|3(?:288|909)|6426)|8(?:6234|9616)|9(?:5297|6(?:040|835)|7(?:294|688)|9(?:689|796))', example_number='24280', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='112|911', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11(?:2|5[1-47]|[68]\\d|7[0-57]|98)|[2-9]\\d{3,5}|[2-9]11', example_number='112', possible_length=(3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='2(?:3333|(?:4224|7562|900)2|56447|6688)|3(?:1010|2665|7404)|40404|560560|6(?:0060|22639|5246|7622)|7(?:0701|3822|4666)|8(?:(?:3825|7226)5|4816)|99099', example_number='23333', possible_length=(5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='336\\d\\d|[2-9]\\d{3}|[2356]11', example_number='211', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='[2-9]\\d{4,5}', example_number='20000', possible_length=(5, 6)),
    short_data=True)
