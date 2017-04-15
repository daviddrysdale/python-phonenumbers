"""Auto-generated file, do not edit by hand. DE metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DE = PhoneMetadata(id='DE', country_code=49, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{4,14}', possible_length=(4, 5, 6, 7, 8, 9, 10, 11), possible_length_local_only=(2, 3)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[24-6]\\d{2}|3[03-9]\\d|[789](?:0[2-9]|[1-9]\\d))\\d{1,8}', example_number='30123456', possible_length=(4, 5, 6, 7, 8, 9, 10, 11), possible_length_local_only=(2, 3)),
    mobile=PhoneNumberDesc(national_number_pattern='1(5\\d{9}|7\\d{8}|6[02]\\d{8}|63\\d{7})', example_number='15123456789', possible_length=(10, 11)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', example_number='8001234567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900([135]\\d{6}|9\\d{7})', example_number='9001234567', possible_length=(10, 11)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3,8})', format='\\1 \\2', leading_digits_pattern=['2|3[3-9]|906|[4-9][1-9]1'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{4,11})', format='\\1/\\2', leading_digits_pattern=['[34]0|[68]9'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([4-9]\\d)(\\d{2})', format='\\1 \\2', leading_digits_pattern=['[4-9]', '[4-6]|[7-9](?:\\d[1-9]|[1-9]\\d)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([4-9]\\d{3})(\\d{2,7})', format='\\1 \\2', leading_digits_pattern=['[4-9]', '[4-6]|[7-9](?:\\d[1-9]|[1-9]\\d)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{1})(\\d{6})', format='\\1 \\2 \\3', leading_digits_pattern=['800'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['900'], national_prefix_formatting_rule='0\\1')])
