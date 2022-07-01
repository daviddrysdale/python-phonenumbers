"""Auto-generated file, do not edit by hand. CO metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CO = PhoneMetadata(id='CO', country_code=57, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='(?:60|3\\d)\\d{8}', possible_length=(10,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='60\\d{8}', example_number='6012345678', possible_length=(10,)),
    mobile=PhoneNumberDesc(national_number_pattern='3(?:0[0-5]|1\\d|2[0-3]|5[01]|70)\\d{7}', example_number='3211234567', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0(4(?:[14]4|56)|[579])?',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['6'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='0$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['3'], domestic_carrier_code_formatting_rule='0$CC \\1')],
    mobile_number_portable_region=True)
