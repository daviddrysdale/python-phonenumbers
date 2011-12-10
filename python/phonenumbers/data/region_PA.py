"""Auto-generated file, do not edit by hand. PA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PA = PhoneMetadata(id='PA', country_code=507, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{6,7}', possible_number_pattern='\\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:0[02-579]|19|23|3[03]|4[479]|5[57]|65|7[016-8]|8[58]|9[1-49])|2(?:[0235679]\\d|1[0-7]|4[04-9]|8[028])|3(?:0[0-7]|1[14-7]|2[0-3]|3[03]|4[0457]|5[56]|6[068]|7[078]|80|9[0-79])|4(?:3[013-59]|4\\d|7[0-689])|5(?:[01]\\d|2[0-7]|[56]0|79)|7(?:09|2[0-267]|[34]0|5[6-9]|7[0-24-7]|8[89]|99)|8(?:[34]\\d|5[0-5]|8[02])|9(?:0[78]|1[0178]|2[0378]|3[379]|40|5[0489]|6[06-9]|7[046-9]|8[36-8]|9[1-9]))\\d{4}', possible_number_pattern='\\d{7}', example_number='2001234'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:161|21[89]|8(?:1[01]|7[23]))\\d{4}|6(?:[04-8]\\d|1[0-5]|2[0-4]|3[7-9]|9[0-8])\\d{5}', possible_number_pattern='\\d{7,8}', example_number='60012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='80[09]\\d{4}', possible_number_pattern='\\d{7}', example_number='8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:779|8(?:2[235]|60|7[578]|86|95)|9(?:0[0-2]|81))\\d{4}', possible_number_pattern='\\d{7}', example_number='8601234'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='911', possible_number_pattern='\\d{3}', example_number='911'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1-\\2', leading_digits_pattern=['[1-57-9]']),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format=u'\\1-\\2', leading_digits_pattern=['6'])])
