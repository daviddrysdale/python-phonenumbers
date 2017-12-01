"""Auto-generated file, do not edit by hand. AX metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AX = PhoneMetadata(id='AX', country_code=358, international_prefix='00|99(?:[02469]|5(?:11|33|5[59]|88|9[09]))',
    general_desc=PhoneNumberDesc(national_number_pattern='[13]\\d{5,9}|2\\d{4,9}|4\\d{6,10}|5\\d{6,9}|[67]\\d{7,9}|8\\d{7,8}', possible_length=(5, 6, 7, 8, 9, 10)),
    fixed_line=PhoneNumberDesc(national_number_pattern='18[1-8]\\d{4,6}', example_number='181234567', possible_length=(7, 8, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[0-8]\\d{5,8}|9\\d{9})|50\\d{6,8}', example_number='412345678', possible_length=(7, 8, 9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5,6}', example_number='800123456', possible_length=(8, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='[67]00\\d{5,6}', example_number='600123456', possible_length=(8, 9)),
    uan=PhoneNumberDesc(national_number_pattern='10(?:0\\d{4,6}|[1-37-9]\\d{5,7}|[46]\\d{3,7}|5\\d{4,7})|2(?:0(?:0\\d{4,6}|[1346-8]\\d{5,7}|2(?:[023]\\d{4,5}|[14-9]\\d{4,6})|5(?:\\d{3}|\\d{5,7})|9(?:[0-7]\\d{4,6}|[89]\\d{1,6}))|9\\d{5,8})|3(?:0(?:0\\d{3,7}|[1-57-9]\\d{5,7}|6(?:\\d{3}|\\d{5,7}))|44\\d{3}|93\\d{5,7})|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{5,6})', example_number='10112345', possible_length=(5, 6, 7, 8, 9, 10)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='100\\d{4,6}|20(?:0\\d{4,6}|2[023]\\d{4,5}|9[89]\\d{1,6})|300\\d{3,7}|60(?:[12]\\d{5,6}|6\\d{7})|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{5,6})', example_number='1001234', possible_length=(5, 6, 7, 8, 9, 10)),
    preferred_international_prefix='00',
    national_prefix='0',
    national_prefix_for_parsing='0')
