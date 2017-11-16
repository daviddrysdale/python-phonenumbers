"""Auto-generated file, do not edit by hand. TJ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TJ = PhoneMetadata(id='TJ', country_code=992, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-57-9]\\d{8}', possible_length=(9,), possible_length_local_only=(3, 5, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:1[3-5]|2[245]|3[12]|4[24-7]|5[25]|72)|4(?:46|74|87))\\d{6}', example_number='372123456', possible_length=(9,), possible_length_local_only=(3, 5, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:41[18]|(?:5[05]|77|88|9[0-35-9])\\d)\\d{6}', example_number='917123456', possible_length=(9,)),
    preferred_international_prefix='8~10',
    national_prefix='8',
    national_prefix_for_parsing='8',
    number_format=[NumberFormat(pattern='([349]\\d{2})(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[34]7|91[78]'], national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='([457-9]\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['4[148]|[578]|9(?:[0235-9]|1[59])'], national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(331700)(\\d)(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['331', '3317', '33170', '331700'], national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{4})(\\d)(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3[1-5]', '3(?:[1245]|3(?:[02-9]|1[0-589]))'], national_prefix_optional_when_formatting=True)])
