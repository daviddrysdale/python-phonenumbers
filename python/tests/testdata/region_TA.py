"""Auto-generated file, do not edit by hand. TA metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TA = PhoneMetadata(id='TA', country_code=290, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='8\\d{3,7}', possible_length=(4, 6, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='8\\d{5}', example_number='812345', possible_length=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='8\\d{3}', example_number='8123', possible_length=(4,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8\\d{7}', example_number='81234567', possible_length=(8,)))
