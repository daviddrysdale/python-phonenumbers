"""Auto-generated file, do not edit by hand. FI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FI = PhoneMetadata(id='FI', country_code=358, international_prefix='00|99(?:[01469]|5(?:11|3[23]|41|5[59]|77|88|9[09]))',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[124-7]\\d|3[0-46-9])\\d{8}|[1-9]\\d{5,8}|[1-35689]\\d{4}', possible_length=(5, 6, 7, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[3-79][1-8]|[235689][1-8]\\d)\\d{2,6}', example_number='131234567', possible_length=(5, 6, 7, 8, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:4[0-8]|50)\\d{4,8}', example_number='412345678', possible_length=(6, 7, 8, 9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4,6}', example_number='800123456', possible_length=(7, 8, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='[67]00\\d{5,6}', example_number='600123456', possible_length=(8, 9)),
    uan=PhoneNumberDesc(national_number_pattern='10\\d{4,8}|2(?:0(?:[016-8]\\d{3,7}|[2-59]\\d{2,7})|9\\d{4,8})|3[09]\\d{4,8}|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{3,7})', example_number='10112345', possible_length=(5, 6, 7, 8, 9, 10)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='[13]00\\d{3,7}|2(?:0(?:0\\d{3,7}|2[023]\\d{1,6}|9[89]\\d{1,6}))|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{3,7})', possible_length=(5, 6, 7, 8, 9, 10)),
    preferred_international_prefix='00',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3,7})', format='\\1 \\2', leading_digits_pattern=['(?:[1-3]0|[6-8])0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(75\\d{3})', format='\\1', leading_digits_pattern=['75[12]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(116\\d{3})', format='\\1', leading_digits_pattern=['116'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{4,10})', format='\\1 \\2', leading_digits_pattern=['[14]|2[09]|50|7[135]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{4,11})', format='\\1 \\2', leading_digits_pattern=['[25689][1-8]|3'], national_prefix_formatting_rule='0\\1')],
    main_country_for_code=True,
    mobile_number_portable_region=True)
