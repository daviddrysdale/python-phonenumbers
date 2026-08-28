"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=263, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:13|8\\d{4})\\d{5}|[235-8]\\d{8}|[2-689]\\d{6}', possible_length=(7, 9, 10), possible_length_local_only=(3, 4, 5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:(?:(?:02[014]|72[03])\\d|48)\\d|2(?:[278]\\d|92)|583)|(?:37[56]|6[78]21\\d)\\d|5(?:483|525\\d\\d))\\d{3}|(?:2(?:0\\d|7[1-7])|(?:55|6[78])\\d)\\d{4}|(?:13|2(?:(?:42|9\\d)\\d|[56]20)|3(?:123|92\\d)|(?:4|542)\\d|6(?:[16]21|52[013])|8(?:[1349]28|523)|9[2-9])\\d{5}', example_number='1312345', possible_length=(7, 9), possible_length_local_only=(3, 4, 5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:[1278]\\d|3[1-9]|9[01])\\d{6}', example_number='712345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:[01]\\d|20|8[0-8])\\d{3}', example_number='8001234', possible_length=(7,)),
    voip=PhoneNumberDesc(national_number_pattern='86(?:1[12]|22|30|44|55|77|8[368])\\d{6}', example_number='8686123456', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['1|2(?:0[0-36-9]|29|58)|67[0-46-9]|(?:55|68)[0-69]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['2(?:0[45]|[27]|48)|37|675|(?:55|68)[78]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[49]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['80'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['548'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['29[013-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['[256]|39|8[13-59]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['3'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1')])
