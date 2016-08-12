"""Auto-generated file, do not edit by hand. IN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IN = PhoneMetadata(id='IN', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[125]\\d{2,6}', possible_number_pattern='\\d{3,7}'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[0128]|12|298)|2611', possible_number_pattern='\\d{3,4}', example_number='108'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[0128]|12|298)|2611|5(?:14(?:2[5-9]|[34]\\d)|3000|757555)', possible_number_pattern='\\d{3,7}', example_number='108'),
    standard_rate=PhoneNumberDesc(national_number_pattern='5(?:14(?:2[5-9]|[34]\\d)|757555)', possible_number_pattern='\\d{5,7}', example_number='5757555'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='53000', possible_number_pattern='\\d{5}'),
    short_data=True)
