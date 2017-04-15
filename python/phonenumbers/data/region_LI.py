"""Auto-generated file, do not edit by hand. LI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LI = PhoneMetadata(id='LI', country_code=423, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='6\\d{8}|[23789]\\d{6}', possible_length=(7, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:01|1[27]|3\\d|6[02-578]|96)|3(?:7[0135-7]|8[048]|9[0269]))\\d{4}', example_number='2345678', possible_length=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:5(?:09|1\\d|20)|6(?:0[0-6]|10|2[06-9]|39))\\d{5}|7(?:[37-9]\\d|42|56)\\d{4}', example_number='660234567', possible_length=(7, 9)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:02[28]|9\\d{2})\\d{2}', example_number='8002222', possible_length=(7,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90(?:02[258]|1(?:23|3[14])|66[136])\\d{2}', example_number='9002222', possible_length=(7,)),
    uan=PhoneNumberDesc(national_number_pattern='870(?:28|87)\\d{2}', example_number='8702812', possible_length=(7,)),
    voicemail=PhoneNumberDesc(national_number_pattern='697(?:42|56|[78]\\d)\\d{4}', example_number='697861234', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0|10(?:01|20|66)',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['[23789]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['6[56]']),
        NumberFormat(pattern='(69)(7\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['697'])])
