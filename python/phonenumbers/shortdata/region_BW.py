"""Auto-generated file, do not edit by hand. BW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BW = PhoneMetadata(id='BW', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,4}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='11[0-246]|9(?:1[0-4]|2[02-69]|9[06-9])', example_number='110', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='11[12]|9(?:11|9[7-9])', example_number='111', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:(?:[02]|[6-9]\\d\\d)\\d|1[0-2469]|3123)|9(?:1[0-4]|2[02-69]|9\\d)|1[0-28]\\d\\d', example_number='100', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:[0-2]|31)\\d\\d|9(?:1[02-4]|2[02-69]|9[0-3])|1(?:[02]\\d|1[49])', example_number='100', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='131\\d\\d', example_number='13100', possible_length=(5,)),
    short_data=True)
