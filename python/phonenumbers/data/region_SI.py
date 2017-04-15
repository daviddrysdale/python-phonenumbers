"""Auto-generated file, do not edit by hand. SI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SI = PhoneMetadata(id='SI', country_code=386, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{6,7}|[89]\\d{4,7}', possible_length=(5, 6, 7, 8), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1\\d|[25][2-8]|3[24-8]|4[24-8]|7[3-8])\\d{6}', example_number='11234567', possible_length=(8,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[37][01]|4[0139]|51|6[48])\\d{6}', example_number='31234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{4,6}', example_number='80123456', possible_length=(6, 7, 8)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{4,6}|89[1-3]\\d{2,5}', example_number='90123456', possible_length=(5, 6, 7, 8)),
    voip=PhoneNumberDesc(national_number_pattern='(?:59|8[1-3])\\d{6}', example_number='59012345', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[12]|3[24-8]|4[24-8]|5[2-8]|7[3-8]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='([3-7]\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[37][01]|4[0139]|51|6'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([89][09])(\\d{3,6})', format='\\1 \\2', leading_digits_pattern=['[89][09]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([58]\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['59|8[1-3]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
