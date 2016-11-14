"""Auto-generated file, do not edit by hand. OM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_OM = PhoneMetadata(id='OM', country_code=968, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:5|[279]\\d)\\d{6}|800\\d{5,6}', possible_number_pattern='\\d{7,9}', possible_length=(7, 8, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[2-6]\\d{6}', possible_number_pattern='\\d{8}', example_number='23123456', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='7[19]\\d{6}|9(?:0[1-9]|[1-9]\\d)\\d{5}', possible_number_pattern='\\d{8}', example_number='92123456', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8007\\d{4,5}|500\\d{4}', possible_number_pattern='\\d{7,9}', example_number='80071234', possible_length=(7, 8, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{5}', possible_number_pattern='\\d{8}', example_number='90012345', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(2\\d)(\\d{6})', format='\\1 \\2', leading_digits_pattern=['2']),
        NumberFormat(pattern='([79]\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[79]']),
        NumberFormat(pattern='([58]00)(\\d{4,6})', format='\\1 \\2', leading_digits_pattern=['[58]'])],
    mobile_number_portable_region=True)
