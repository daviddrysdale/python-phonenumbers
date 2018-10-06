"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=263, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='2(?:[0-57-9]\\d{6,8}|6[0-24-9]\\d{6,7})|[38]\\d{9}|[35-8]\\d{8}|[3-6]\\d{7}|[1-689]\\d{6}|[1-3569]\\d{5}|[1356]\\d{4}', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(3, 4)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:02[014]|[49]2\\d|[56]20|72[03])|3(?:123|92\\d)|5(?:42\\d|525)|6(?:[16-8]21|52[013])|8(?:[1349]28|523))\\d{5}|(?:2(?:0(?:4\\d|5\\d{2})|2[278]\\d|48\\d|7(?:[1-7]\\d|[089]\\d{2})|8(?:[2-57-9]|[146]\\d{2})|98)|3(?:08|17|3[78]|7(?:[19]|[56]\\d)|8[37]|98)|5[15][78]|6(?:28\\d{2}|37|6[78]|75\\d|98|8(?:7\\d|8)))\\d{3}|(?:2(?:1[39]|2[0157]|31|[56][14]|7[35]|84)|329)\\d{7}|(?:1(?:3\\d{2}|[4-8]|9\\d)|2(?:0\\d{2}|12|292|[569]\\d)|3(?:[26]|[013459]\\d)|5(?:0|1[2-4]|26|[37]2|5\\d{2}|[689]\\d)|6(?:[39]|[01246]\\d|[78]\\d{2}))\\d{3}|(?:29\\d|39|54)\\d{6}|(?:(?:25|54)83\\d|2582\\d{2}|65[2-8])\\d{2}|(?:4\\d{6,7}|9[2-9]\\d{4,5})', example_number='1312345', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(3, 4)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:1\\d|3[2-9]|7[1-9]|8[2-5])|8644)\\d{6}', example_number='712345678', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:[01]\\d|20|8[0-8])\\d{3}', example_number='8001234', possible_length=(7,)),
    voip=PhoneNumberDesc(national_number_pattern='86(?:1[12]|30|55|77|8[368])\\d{6}', example_number='8686123456', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{7})', format='(\\1) \\2', leading_digits_pattern=['(?:2[04-79]|39|5[45]|6[15-8]|8[13-59])2', '2(?:02[014]|[49]2|[56]20|72[03])|392|5(?:42|525)|6(?:[16-8]21|52[013])|8(?:[1349]28|523)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([49])(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['4|9[2-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(7\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(86\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['86[24]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([2356]\\d{2})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['2(?:0[45]|2[278]|[49]8|[78])|3(?:[09]8|17|3[78]|7[1569]|8[37])|5[15][78]|6(?:[29]8|37|[68][78]|75)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['2(?:1[39]|2[0157]|31|[56][14]|7[35]|84)|329'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([1-356]\\d)(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['1[3-9]|2[02569]|3[0-69]|5[05689]|6'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([235]\\d)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[23]9|54'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([25]\\d{3})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['(?:25|54)8', '258[23]|5483'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(8\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['86'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(80\\d)(\\d{4})', format='\\1 \\2', leading_digits_pattern=['80'], national_prefix_formatting_rule='0\\1')])
