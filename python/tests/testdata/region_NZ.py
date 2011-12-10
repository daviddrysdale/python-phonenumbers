"""Auto-generated file, do not edit by hand. NZ metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NZ = PhoneMetadata(id='NZ', country_code=64, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[289]\\d{7,9}|[3-7]\\d{7}', possible_number_pattern='\\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='24099\\d{3}|(?:3[2-79]|[479][2-689]|6[235-9])\\d{6}', possible_number_pattern='\\d{7,8}'),
    mobile=PhoneNumberDesc(national_number_pattern='2(?:[027]\\d{7}|9\\d{6,7}|1(?:0\\d{5,7}|[12]\\d{5,6}|[3-9]\\d{5})|4[1-9]\\d{6}|8\\d{7,8})', possible_number_pattern='\\d{8,10}'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6,7}', possible_number_pattern='\\d{9,10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{6,7}', possible_number_pattern='\\d{9,10}'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{4})', format=u'\\1-\\2 \\3', leading_digits_pattern=['24|[34679]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3,5})', format=u'\\1-\\2 \\3', leading_digits_pattern=['2[179]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1')])
