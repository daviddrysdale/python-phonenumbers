"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[0-29]\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1[129]\\d', example_number='123', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[025]|25)|911', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='096(?:0[12]|2[16-8]|3(?:08|[14]5|[23]|66)|4(?:0|80)|5[01]|6[89]|86|9[19])|1(?:1[0-68]|2[0-59]|3[346-8]|4(?:[0147]|[289]0)|5(?:0[14]|1[02479]|2[0-3]|39|[49]0|65)|6(?:[16]6|[27]|90)|8(?:03|1[18]|22|3[37]|4[28]|88|99)|9[0-579])|20(?:00|1(?:[038]|1[079]|26|9[69])|2[01]|90)|9(?:11|9(?:90|0009))', example_number='112', possible_length=(3, 4, 5, 6)),
    standard_rate=PhoneNumberDesc(national_number_pattern='(?:096|1[58])\\d{2}', example_number='09612', possible_length=(4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1[58]\\d{2}|99(?:90|0009)', example_number='9990', possible_length=(4, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='990009', example_number='990009', possible_length=(6,)),
    short_data=True)
