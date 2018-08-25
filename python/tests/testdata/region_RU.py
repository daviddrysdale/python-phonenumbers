"""Auto-generated file, do not edit by hand. RU metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RU = PhoneMetadata(id='RU', country_code=7, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='[347-9]\\d{9}', possible_length=(10,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[348]\\d{9}', example_number='3011234567', possible_length=(10,)),
    mobile=PhoneNumberDesc(national_number_pattern='9\\d{9}', example_number='9123456789', possible_length=(10,)),
    national_prefix='8',
    national_prefix_for_parsing='8')
