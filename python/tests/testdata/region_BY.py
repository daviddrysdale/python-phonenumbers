"""Auto-generated file, do not edit by hand. BY metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BY = PhoneMetadata(id='BY', country_code=375, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{5}', possible_length=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-9]\\d{5}', example_number='112345', possible_length=(6,)),
    national_prefix='8',
    national_prefix_for_parsing='80?|99999',
    number_format=[NumberFormat(pattern='(\\d{4})', format='\\1', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='8 \\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='8\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['[1-8]'], national_prefix_formatting_rule='8 \\1')])
