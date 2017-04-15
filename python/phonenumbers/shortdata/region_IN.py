"""Auto-generated file, do not edit by hand. IN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IN = PhoneMetadata(id='IN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[125]\\d{2,6}', possible_length=(3, 4, 5, 6, 7)),
    toll_free=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', example_number='105010', possible_length=(3, 4, 5, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='11[67][0-2]\\d{3}', example_number='1160530', possible_length=(7,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[0128]|12|298)|2611', example_number='108', possible_length=(3, 4)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[01248]|5(?:010|6|902)|7(?:[07]|80)|9[0157])|1(?:[289]|[67][0-2]\\d{3})|2(?:1|98)|39|4[01]|55[23]\\d{2}|7000|9(?:0[019]|47|50|6[1347]|[89]))|2611|5(?:14(?:2[5-9]|[34]\\d)|3000|757555)', example_number='108', possible_length=(3, 4, 5, 6, 7)),
    standard_rate=PhoneNumberDesc(national_number_pattern='5(?:14(?:2[5-9]|[34]\\d)|757555)', example_number='5757555', possible_length=(5, 7)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:1(?:[67][0-2]\\d{3}|[89])|21|4[01]|55330|7\\d{3}|9(?:[89]|09))|53000', example_number='53000', possible_length=(3, 4, 5, 6, 7)),
    short_data=True)
