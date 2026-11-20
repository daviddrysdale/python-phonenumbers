"""Auto-generated file, do not edit by hand. CR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CR = PhoneMetadata(id='CR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,3}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:02|1)2|911', example_number='112', possible_length=(3, 4)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:02|1)2|911', example_number='112', possible_length=(3, 4)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:0[0-2]|1[015]|2[0-46-8]|4[08])|1(?:0[015]|1[135-9]|2[125]?|3[2-4]|4[6-9]|55|6[1569]|7[67]|8[07]|9[0-49])|2(?:00|1[235]|2[12]|34)|3(?:11|2[12]|33)|4(?:1[14-6]|21)|5(?:15|20|5[05])|693|7(?:00|1[79]|2[02]|34|67)|818|975)|911', example_number='112', possible_length=(3, 4)),
    short_data=True)
