"""Auto-generated file, do not edit by hand. IR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IR = PhoneMetadata(id='IR', country_code=98, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-6]\\d{4,9}|9(?:[134]\\d{8}|9\\d{2,8})|[178]\\d{9}', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:1[2-9]\\d{2,7}|51\\d{3,7})|(?:241|3(?:11|51)|441|5[14]1)\\d{4,7}|(?:3(?:34|41)|6(?:11|52))\\d{6,7}|(?:1(?:[134589][12]|[27][1-4])|2(?:2[189]|[3689][12]|42|5[256]|7[34])|3(?:12|2[1-4]|3[125]|4[24-9]|5[23]|[6-9][12])|4(?:[135-9][12]|2[1-467]|4[2-4])|5(?:12|2[89]|3[1-5]|4[2-8]|[5-7][12]|8[1245])|6(?:12|[347-9][12]|51|6[1-6])|7(?:[13589][12]|2[1289]|4[1-4]|6[1-6]|7[1-3])|8(?:[145][12]|3[124578]|6[1256]|7[1245]))\\d{7}', possible_number_pattern='\\d{5,10}', example_number='2123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:1\\d|3[124-9])\\d{7}', possible_number_pattern='\\d{10}', example_number='9123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='993[12]\\d{6}', possible_number_pattern='\\d{10}', example_number='9932123456'),
    pager=PhoneNumberDesc(national_number_pattern='943[24678]\\d{6}', possible_number_pattern='\\d{10}', example_number='9432123456'),
    uan=PhoneNumberDesc(national_number_pattern='9990\\d{0,6}', possible_number_pattern='\\d{4,10}', example_number='9990123456'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[025]|25)', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(21)(\\d{3,5})', format=u'\\1 \\2', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(21)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(21)(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[13-9]|2[02-9]'], national_prefix_formatting_rule=u'0\\1')])
