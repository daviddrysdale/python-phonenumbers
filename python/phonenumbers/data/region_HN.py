"""Auto-generated file, do not edit by hand. HN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HN = PhoneMetadata(id='HN', country_code=504, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[237-9]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:2(?:0[019]|1[1-36]|[23]\\d|4[04-6]|5[57]|7[01389]|8[0146-9]|9[012])|4(?:07|2[3-59]|3[13-689]|4[0-68]|5[1-35])|5(?:16|4[03-5]|5\\d|6[4-6]|74)|6(?:[056]\\d|17|3[04]|4[0-378]|[78][0-8]|9[01])|7(?:6[46-9]|7[02-9]|8[034])|8(?:79|8[0-35789]|9[1-57-9]))\\d{4}', example_number='22123456', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='[37-9]\\d{7}', example_number='91234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2')])
