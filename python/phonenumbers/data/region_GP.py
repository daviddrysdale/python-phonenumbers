"""Auto-generated file, do not edit by hand. GP metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GP = PhoneMetadata(id='GP', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[56]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='590(?:0[13468]|1[012]|2[0-68]|3[28]|4[0-8]|5[579]|6[0189]|70|8[0-689]|9\\d)\\d{4}', example_number='590201234', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='690(?:0[0-7]|[1-9]\\d)\\d{4}', example_number='690301234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([56]90)(\\d{2})(\\d{4})', format='\\1 \\2-\\3', national_prefix_formatting_rule='0\\1')],
    main_country_for_code=True)
