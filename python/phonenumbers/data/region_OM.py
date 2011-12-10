"""Auto-generated file, do not edit by hand. OM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_OM = PhoneMetadata(id='OM', country_code=968, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:2[3-6]|5|9[2-9])\\d{6}|800\\d{5,6}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[3-6]\\d{6}', possible_number_pattern='\\d{8}', example_number='23123456'),
    mobile=PhoneNumberDesc(national_number_pattern='9[2-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='92123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='8007\\d{4,5}|500\\d{4}', possible_number_pattern='\\d{7,9}', example_number='80071234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='9999', possible_number_pattern='\\d{4}', example_number='9999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(2\\d)(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['2']),
        NumberFormat(pattern='(9\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['9']),
        NumberFormat(pattern='([58]00)(\\d{4,6})', format=u'\\1 \\2', leading_digits_pattern=['[58]'])])
