"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=98, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[14-8]\\d{6,9}|[23]\\d{4,9}|9(?:[1-4]\\d{8}|9\\d{2,8})', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1(?:[13-589][12]|[27][1-4])\\d{7}|2(?:1\\d{3,8}|3[12]\\d{7}|4(?:1\\d{4,7}|2\\d{7})|5(?:1\\d{3,7}|[2356]\\d{7})|6\\d{8}|7[34]\\d{7}|[89][12]\\d{7})|3(?:1(?:1\\d{4,7}|2\\d{7})|2[1-4]\\d{7}|3(?:[125]\\d{7}|4\\d{6,7})|4(?:1\\d{6,7}[24-9]\\d{7})|5(?:1\\d{4,7}|[23]\\d{7})|[6-9][12]\\d{7})|4(?:[135-9][12]\\d{7}|2[1-467]\\d{7}|4(?:1\\d{4,7}|[2-4]\\d{7}))|5(?:1(?:1\\d{4,7}|2\\d{7})|2[89]\\d{7}|3[1-5]\\d{7}|4(?:1\\d{4,7}|[2-8]\\d{7})|[5-7][12]\\d{7}|8[1245]\\d{7})|6(?:1(?:1\\d{6,7}|2\\d{7})|[347-9][12]\\d{7}|5(?:1\\d{7}|2\\d{6,7})|6[1-6]\\d{7})|7(?:[13589][12]|2[1289]|4[1-4]|6[1-6]|7[1-3])\\d{7}|8(?:[145][12]|3[124578]|6[1256]|7[1245])\\d{7}', possible_number_pattern='\\d{5,10}', example_number='2123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='9[1-3]\\d{8}', possible_number_pattern='\\d{10}', example_number='9123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='(?:[2-6]0\\d|993)\\d{7}', possible_number_pattern='\\d{10}', example_number='9932123456'),
    pager=PhoneNumberDesc(national_number_pattern='943\\d{7}', possible_number_pattern='\\d{10}', example_number='9432123456'),
    uan=PhoneNumberDesc(national_number_pattern='9990\\d{0,6}', possible_number_pattern='\\d{4,10}', example_number='9990123456'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2[15])(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['2(?:1|5[0-47-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(2[15])(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['2(?:1|5[0-47-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(2\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['2(?:[16]|5[0-47-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[13-9]|2[02-57-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[13-9]|2[02-57-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['[13-9]|2[02-57-9]'], national_prefix_formatting_rule='0\\1')])
