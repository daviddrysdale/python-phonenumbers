"""Auto-generated file, do not edit by hand. JP metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JP = PhoneMetadata(id='JP', country_code=81, international_prefix='010',
    general_desc=PhoneNumberDesc(national_number_pattern='07\\d{5}|[1-357-9]\\d{3,10}', possible_length=(4, 5, 6, 7, 8, 9, 10, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='07\\d{5}|[1-357-9]\\d{3,10}', example_number='0712345', possible_length=(4, 5, 6, 7, 8, 9, 10, 11)),
    toll_free=PhoneNumberDesc(national_number_pattern='0777[01]\\d{2}', example_number='0777012', possible_length=(7,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='[23]\\d{3}', possible_length=(4,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['111|222|333', '(?:111|222|333)1', '(?:111|222|333)11'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d)(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['222|333', '2221|3332', '22212|3332', '222120|3332'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[23]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['077'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})', format='*\\1', leading_digits_pattern=['[23]'], national_prefix_formatting_rule='\\1')])
