"""Auto-generated file, do not edit by hand. 883 metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_883 = PhoneMetadata(id='001', country_code=883, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='(?:210|370\\d\\d)\\d{7}|51\\d{7}(?:\\d{3})?', possible_length=(9, 10, 12)),
    voip=PhoneNumberDesc(national_number_pattern='(?:210|(?:370[1-9]|51[013]0)\\d)\\d{7}|5100\\d{5}', example_number='510012345', possible_length=(9, 10, 12)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['510']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['2']),
        NumberFormat(pattern='(\\d{4})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['51[13]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[35]'])])
