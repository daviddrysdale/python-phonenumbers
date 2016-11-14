"""Auto-generated file, do not edit by hand. LV metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LV = PhoneMetadata(id='LV', country_code=371, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2689]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='6\\d{7}', example_number='63123456', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='2\\d{7}', example_number='21234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{6}', possible_number_pattern='\\d{8}', example_number='80123456', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{6}', possible_number_pattern='\\d{8}', example_number='90123456', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='81\\d{6}', possible_number_pattern='\\d{8}', example_number='81123456', possible_length=(8,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='([2689]\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3')],
    mobile_number_portable_region=True)
