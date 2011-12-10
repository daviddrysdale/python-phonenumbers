"""Auto-generated file, do not edit by hand. KI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KI = PhoneMetadata(id='KI', country_code=686, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-689]\\d{4}', possible_number_pattern='\\d{5}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[234]\\d|50|8[1-5])\\d{3}', possible_number_pattern='\\d{5}', example_number='31234'),
    mobile=PhoneNumberDesc(national_number_pattern='6\\d{4}|9(?:[0-8]\\d|9[015-8])\\d{2}', possible_number_pattern='\\d{5}', example_number='61234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='99[2349]', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix_for_parsing='0')
