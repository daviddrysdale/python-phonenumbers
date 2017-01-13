"""Auto-generated file, do not edit by hand. SO metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SO = PhoneMetadata(id='SO', country_code=252, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{5,8}', possible_number_pattern='\\d{6,9}', possible_length=(6, 7, 8, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1\\d{1,2}|2[0-79]\\d|3[0-46-8]?\\d|4[0-7]?\\d|59\\d|8[125])\\d{4}', possible_number_pattern='\\d{6,7}', example_number='4012345', possible_length=(6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:15\\d|2(?:4\\d|8)|3[59]\\d{2}|4[89]\\d{2}|6[1-9]?\\d{2}|7(?:[1-8]\\d|9\\d{1,2})|8[08]\\d{2}|9(?:0[67]|[2-9])\\d)\\d{5}', example_number='71123456', possible_length=(7, 8, 9)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{6})', format='\\1', leading_digits_pattern=['[134]']),
        NumberFormat(pattern='(\\d)(\\d{6})', format='\\1 \\2', leading_digits_pattern=['2[0-79]|[13-5]']),
        NumberFormat(pattern='(\\d)(\\d{7})', format='\\1 \\2', leading_digits_pattern=['24|[67]']),
        NumberFormat(pattern='(\\d{2})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['8[125]']),
        NumberFormat(pattern='(\\d{2})(\\d{5,7})', format='\\1 \\2', leading_digits_pattern=['15|28|6[1-35-9]|799|9[2-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['3[59]|4[89]|6[24-6]|79|8[08]|90'])])
