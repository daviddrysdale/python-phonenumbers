"""Auto-generated file, do not edit by hand. VN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VN = PhoneMetadata(id='VN', country_code=84, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{6,9}|2\\d{9}|6\\d{6,7}|7\\d{6}|8\\d{6,8}|9\\d{8}', possible_length=(7, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:0[3-9]|1[0-689]|2[0-25-9]|3[2-9]|4[2-8]|5[124-9]|6[0-39]|7[0-7]|8[2-7]|9[0-4679])\\d{7}', example_number='2101234567', possible_length=(10,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:9\\d|1(?:2\\d|6[2-9]|8[68]|99))\\d{7}|8(?:6[89]|8\\d|9[89])\\d{6}', example_number='912345678', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{4,6}', example_number='1800123456', possible_length=(8, 9, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900\\d{4,6}', example_number='1900123456', possible_length=(8, 9, 10)),
    uan=PhoneNumberDesc(national_number_pattern='[17]99\\d{4}|69\\d{5,6}|80\\d{5}', example_number='1992000', possible_length=(7, 8)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='[17]99\\d{4}|69\\d{5,6}', example_number='1992000', possible_length=(7, 8)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([17]99)(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[17]99'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['2[48]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(80)(\\d{5})', format='\\1 \\2', leading_digits_pattern=['80'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(69\\d)(\\d{4,5})', format='\\1 \\2', leading_digits_pattern=['69'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['2[0-35-79]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='([89]\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['8(?:8|9[89])|9'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1[2689]\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:[26]|8[68]|99)'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(86[89])(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['86[89]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1[89]00)(\\d{4,6})', format='\\1 \\2', leading_digits_pattern=['1[89]0', '1[89]00'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True)])
