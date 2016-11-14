"""Auto-generated file, do not edit by hand. MT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MT = PhoneMetadata(id='MT', country_code=356, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2357-9]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:0(?:1[0-6]|3[1-4]|[69]\\d)|[1-357]\\d{2})\\d{4}', example_number='21001234', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:210|[79]\\d{2})|9(?:2(?:1[01]|31)|696|8(?:1[1-3]|89|97)|9\\d{2}))\\d{4}', example_number='96961234', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800[3467]\\d{4}', possible_number_pattern='\\d{8}', example_number='80071234', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='5(?:0(?:0(?:37|43)|6\\d{2}|70\\d|9[0168]\\d)|[12]\\d0[1-5])\\d{3}', possible_number_pattern='\\d{8}', example_number='50037123', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(national_number_pattern='3550\\d{4}', possible_number_pattern='\\d{8}', example_number='35501234', possible_length=(8,)),
    pager=PhoneNumberDesc(national_number_pattern='7117\\d{4}', possible_number_pattern='\\d{8}', example_number='71171234', possible_length=(8,)),
    uan=PhoneNumberDesc(national_number_pattern='501\\d{5}', possible_number_pattern='\\d{8}', example_number='50112345', possible_length=(8,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1 \\2')],
    mobile_number_portable_region=True)
