"""Auto-generated file, do not edit by hand. IT metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IT = PhoneMetadata(id='IT', country_code=39, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[0389]\\d{5,10}', possible_length=(6, 9, 10, 11)),
    fixed_line=PhoneNumberDesc(national_number_pattern='0\\d{9,10}', example_number='0123456789', possible_length=(10, 11)),
    mobile=PhoneNumberDesc(national_number_pattern='3\\d{8,9}', example_number='3123456789', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:0\\d{6}|3\\d{3})', example_number='800123456', possible_length=(6, 9)),
    premium_rate=PhoneNumberDesc(national_number_pattern='89(?:2\\d{3}|9\\d{6})', example_number='892123', possible_length=(6, 9)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['0[26]']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['0[13-57-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['3']),
        NumberFormat(pattern='(\\d{3})(\\d{3,6})', format='\\1 \\2', leading_digits_pattern=['8'])])
