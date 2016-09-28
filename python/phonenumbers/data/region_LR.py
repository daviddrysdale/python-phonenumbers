"""Auto-generated file, do not edit by hand. LR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LR = PhoneMetadata(id='LR', country_code=231, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='2\\d{7,8}|[378]\\d{8}|4\\d{6}|5\\d{6,8}', possible_number_pattern='\\d{7,9}', possible_length=(7, 8, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2\\d{7}', possible_number_pattern='\\d{8}', example_number='21234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:20\\d{3}|330\\d{2}|4[67]\\d|5(?:55)?\\d{2}|77\\d{3}|88\\d{3})\\d{4}', possible_number_pattern='\\d{7,9}', example_number='770123456', possible_length=(7, 9)),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='332(?:02|[25]\\d)\\d{4}', possible_number_pattern='\\d{9}', example_number='332021234', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['2'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([4-5])(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[45]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[23578]'], national_prefix_formatting_rule='0\\1')])
