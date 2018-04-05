"""Auto-generated file, do not edit by hand. MA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MA = PhoneMetadata(id='MA', country_code=212, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[5-9]\\d{8}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='5(?:2(?:[015-79]\\d|2[02-9]|3[2-57]|4[2-8]|8[235-7])\\d|3(?:[0-48]\\d|[57][2-9]|6[2-8]|9[3-9])\\d|4[067]\\d{2}|5[03]\\d{2})\\d{4}', example_number='520123456', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:6(?:[0-79]\\d|8[0-247-9])|7(?:0[067]|6[1267]|7[017]))\\d{6}', example_number='650123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', example_number='801234567', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='89\\d{7}', example_number='891234567', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='5924[01]\\d{4}', example_number='592401234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([5-7]\\d{2})(\\d{6})', format='\\1-\\2', leading_digits_pattern=['5(?:2[015-7]|3[0-4])|[67]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([58]\\d{3})(\\d{5})', format='\\1-\\2', leading_digits_pattern=['5(?:2[2-489]|3[5-9]|92)|892', '5(?:2(?:[2-48]|9[0-7])|3(?:[5-79]|8[0-7])|924)|892'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(5\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['5(?:29|38)', '5(?:29|38)[89]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([5]\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['5(?:4[067]|5[03])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(8[09])(\\d{7})', format='\\1-\\2', leading_digits_pattern=['8(?:0|9[013-9])'], national_prefix_formatting_rule='0\\1')],
    main_country_for_code=True,
    mobile_number_portable_region=True)
