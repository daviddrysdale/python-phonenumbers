"""Auto-generated file, do not edit by hand. AZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AZ = PhoneMetadata(id='AZ', country_code=994, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='365\\d{6}|(?:[124579]\\d|60|88)\\d{7}', possible_length=(9,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:222[0-79]\\d|365(?:[0-46-9]\\d|5[0-35-9]))\\d{4}|(?:(?:1[28]|46)\\d|2(?:[045]2|1[24]|2[34]|33|6[23]))\\d{6}', example_number='123123456', possible_length=(9,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='36554\\d{4}|(?:[16]0|4[04]|5[015]|7[07]|99)\\d{7}', example_number='401234567', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='88\\d{7}', example_number='881234567', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900200\\d{3}', example_number='900200123', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['90'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1[28]|2|365|46', '1[28]|2|365|46', '1[28]|2|365(?:[0-46-9]|5[0-35-9])|46'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[13-9]'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['90']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1[28]|2|365|46', '1[28]|2|365|46', '1[28]|2|365(?:[0-46-9]|5[0-35-9])|46']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[13-9]'])],
    mobile_number_portable_region=True)
