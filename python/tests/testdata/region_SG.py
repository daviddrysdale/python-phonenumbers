"""Auto-generated file, do not edit by hand. SG metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SG = PhoneMetadata(id='SG', country_code=65, international_prefix='0[0-3][0-9]',
    general_desc=PhoneNumberDesc(national_number_pattern='[13689]\\d{7,10}', possible_number_pattern='\\d{8}|\\d{10,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[36]\\d{7}', possible_number_pattern='\\d{8}'),
    mobile=PhoneNumberDesc(national_number_pattern='[89]\\d{7}', possible_number_pattern='\\d{8}'),
    toll_free=PhoneNumberDesc(national_number_pattern='1?800\\d{7}', possible_number_pattern='\\d{10,11}'),
    premium_rate=PhoneNumberDesc(national_number_pattern='1900\\d{7}', possible_number_pattern='\\d{11}'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix_for_parsing='777777',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[369]|8[1-9]']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1[89]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['800'])])
