"""Auto-generated file, do not edit by hand. FR metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FR = PhoneMetadata(id='FR', country_code=33, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='3\\d{6}', possible_length=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='3\\d{6}', example_number='3123456', possible_length=(7,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['3'], national_prefix_formatting_rule='0\\1')])
