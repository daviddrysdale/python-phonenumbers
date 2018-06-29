"""Auto-generated file, do not edit by hand. AR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AR = PhoneMetadata(id='AR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[01389]\\d{1,4}', possible_length=(2, 3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='[09]\\d{2}|1(?:[02-9]\\d?|1[0-24-9]?)', example_number='111', possible_length=(2, 3)),
    emergency=PhoneNumberDesc(national_number_pattern='10[017]|911', example_number='101', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='000|1(?:0[0-35-7]|1[02-5]|2[15]|9)|3372|89338|911', example_number='121', possible_length=(2, 3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='89338', example_number='89338', possible_length=(5,)),
    sms_services=PhoneNumberDesc(national_number_pattern='3372|89338', example_number='3372', possible_length=(4, 5)),
    short_data=True)
