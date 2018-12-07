"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=263, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='2(?:[0-57-9]\\d{6,8}|6[0-24-9]\\d{6,7})|[38]\\d{9}|[35-8]\\d{8}|[3-6]\\d{7}|[1-689]\\d{6}|[1-3569]\\d{5}|[1356]\\d{4}', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(3, 4)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:(?:3\\d|9)\\d|[4-8])|2(?:(?:(?:0(?:2[014]|5)|(?:2[0157]|31|84|9)\\d\\d|[56](?:[14]\\d\\d|20)|7(?:[089]|2[03]|[35]\\d\\d))\\d|4(?:2\\d\\d|8))\\d|1(?:2|[39]\\d{4}))|3(?:(?:123|(?:29\\d|92)\\d)\\d\\d|7(?:[19]|[56]\\d))|(?:4\\d\\d|9[2-9])\\d\\d?|5(?:0|1[2-478]|26|[37]2|4(?:2\\d{3}|83)|5(?:25\\d\\d|[78])|[689]\\d)|6(?:(?:[16-8]21|28|52[013])\\d\\d|[39])|8(?:[1349]28|523)\\d\\d)\\d{3}|(?:(?:2(?:(?:(?:0|8[146])\\d|7[1-7])\\d|2(?:[278]\\d|92)|58(?:2\\d|3))|3(?:[26]|9\\d{3})|5(?:4\\d|5)\\d\\d)\\d|6(?:(?:(?:[0-246]|[78]\\d)\\d|37)\\d|5[2-8]))\\d\\d|(?:2(?:[569]\\d|8[2-57-9])|3(?:[013-59]\\d|8[37])|6[89]8)\\d{3}', example_number='1312345', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(3, 4)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:1\\d|3[2-9]|7[1-9]|8[2-5])|8644)\\d{6}', example_number='712345678', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:[01]\\d|20|8[0-8])\\d{3}', example_number='8001234', possible_length=(7,)),
    voip=PhoneNumberDesc(national_number_pattern='86(?:1[12]|30|55|77|8[368])\\d{6}', example_number='8686123456', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[49]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['2(?:0[45]|2[278]|[49]8|[78])|3(?:[09]8|17|3[78]|[78])|5[15][78]|6(?:[29]8|37|[68][78]|75)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['80'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['2(?:[05-79]2|4)|(?:39|5[45]|6[15-8])2|8[13-59]', '2(?:02[014]|4|[56]20|[79]2)|392|5(?:42|525)|6(?:[16-8]21|52[013])|8[13-59]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['2(?:1[39]|2[0157]|[378]|[56][14])|3(?:12|29)', '2(?:1[39]|2[0157]|[378]|[56][14])|3(?:123|29)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['[16]|2(?:[0-256]|9[0-79])|3(?:[09][0-79]|1[0-689]|[24-6]|3[0-69])|5[0-35-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['29|3|54'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['[25]'], national_prefix_formatting_rule='0\\1')])
