"""Auto-generated file, do not edit by hand. BO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BO = PhoneMetadata(id='BO', country_code=591, international_prefix='00(1\\d)?',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[2-467]\\d{3}|80017)\\d{4}', possible_length=(8, 9), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:2\\d{2}|5(?:11|[258]\\d|9[67])|6(?:12|2\\d|9[34])|8(?:2[34]|39|62))|3(?:3\\d{2}|4(?:6\\d|8[24])|8(?:25|42|5[257]|86|9[25])|9(?:2\\d|3[234]|4[248]|5[24]|6[2-6]|7\\d))|4(?:4\\d{2}|6(?:11|[24689]\\d|72)))\\d{4}', example_number='22123456', possible_length=(8,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='[67]\\d{7}', example_number='71234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80017\\d{4}', example_number='800171234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0(1\\d)?',
    number_format=[NumberFormat(pattern='([234])(\\d{7})', format='\\1 \\2', leading_digits_pattern=['[2-4]'], domestic_carrier_code_formatting_rule='0$CC \\1'),
        NumberFormat(pattern='([67]\\d{7})', format='\\1', leading_digits_pattern=['[67]'], domestic_carrier_code_formatting_rule='0$CC \\1'),
        NumberFormat(pattern='(800)(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['800'], domestic_carrier_code_formatting_rule='0$CC \\1')])
