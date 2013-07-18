"""Auto-generated file, do not edit by hand. FR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FR = PhoneMetadata(id='FR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{1,5}|3\\d{3,4}|[4-8]\\d{4}', possible_number_pattern='\\d{2,6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{1,5}|3\\d{3,4}|[4-8]\\d{4}', possible_number_pattern='\\d{2,6}'),
    mobile=PhoneNumberDesc(national_number_pattern='1\\d{1,5}|3\\d{3,4}|[4-8]\\d{4}', possible_number_pattern='\\d{2,6}'),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1(?:[02459]|6\\d{3}|8710)|[578])|3[01]\\d{2}', possible_number_pattern='\\d{2,6}', example_number='3010'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:1(?:0|18([0-68]\\d{3}|7(?:0\\d|1[1-9]|[2-9]\\d)))|3[2-9]|[4-8]\\d{2})\\d{2}', possible_number_pattern='\\d{4,6}', example_number='3200'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0\\d{2}|1(?:[02459]|6000|8\\d{3})|[578])|3\\d{3}', possible_number_pattern='\\d{2,6}', example_number='1010'),
    standard_rate=PhoneNumberDesc(national_number_pattern='118777', possible_number_pattern='\\d{6}', example_number='118777'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
