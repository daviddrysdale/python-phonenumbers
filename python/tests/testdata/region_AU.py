"""Auto-generated file, do not edit by hand. AU metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='001[12]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-578]\\d{4,14}', possible_length=(9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2378]\\d{8}', example_number='212345678', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='4\\d{8}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', example_number='1800123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0126]\\d{6}', example_number='1900123456', possible_length=(10,)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2-478]'], national_prefix_formatting_rule='0\\1')])
