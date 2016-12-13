"""Auto-generated file, do not edit by hand. KI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KI = PhoneMetadata(id='KI', country_code=686, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2458]\\d{4}|3\\d{4,7}|7\\d{7}', possible_number_pattern='\\d{5,8}', possible_length=(5, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[24]\\d|3[1-9]|50|8[0-5])\\d{3}|7(?:27|31|5[0-4])\\d{5}', possible_number_pattern='\\d{5}', example_number='31234', possible_length=(5, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='7[23]0\\d{5}', possible_number_pattern='\\d{8}', example_number='72012345', possible_length=(8,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='30(?:0[01]\\d{2}|12(?:11|20))\\d{2}', possible_number_pattern='\\d{5,8}', example_number='30010000', possible_length=(8,)),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix_for_parsing='0')
