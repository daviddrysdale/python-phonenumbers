"""Auto-generated file, do not edit by hand. BE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BE = PhoneMetadata(id='BE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d\\d(?:\\d(?:\\d{2})?)?', possible_length=(3, 4, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:0[0-25-8]|1(?:[02]|6\\d{3})|7(?:12|77)|813)|8\\d{3}', example_number='100', possible_length=(3, 4, 6)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1(?:2(?:[03]4|1\\d)|3[01]\\d|4(?:04|1\\d))|[2-79]\\d{3}', example_number='1204', possible_length=(4,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[01]|12)', example_number='100', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[0-8]|1(?:[027]|6(?:000|117))|2(?:0[47]|12|3[0-24]|99)|3(?:0[47]|13|99)|4(?:0[47]|14|50|99)|5(?:1[05]|5[15]|66|95)|6(?:1[167]|36|6[16])|7(?:0[07]|1[27-9]|22|33|65|7[017]|89)|81[39])|[2-9]\\d{3}', example_number='100', possible_length=(3, 4, 6)),
    sms_services=PhoneNumberDesc(national_number_pattern='[2-9]\\d{3}', example_number='2000', possible_length=(4,)),
    short_data=True)
