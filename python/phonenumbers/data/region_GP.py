"""Auto-generated file, do not edit by hand. GP metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GP = PhoneMetadata(id='GP', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[56]\\d{8}', possible_number_pattern='\\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='590(?:1[12]|2[0-68]|3[28]|4[126-8]|5[067]|6[018]|[89]\\d)\\d{4}', possible_number_pattern='\\d{9}', example_number='590201234'),
    mobile=PhoneNumberDesc(national_number_pattern='690(?:00|1[1-9]|2[013-5]|[3-5]\\d|6[0-57-9]|7[1-6]|8[0-6]|9[09])\\d{4}', possible_number_pattern='\\d{9}', example_number='690301234'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1[578]', possible_number_pattern='\\d{2}', example_number='18'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([56]90)(\\d{2})(\\d{4})', format=u'\\1 \\2-\\3', national_prefix_formatting_rule=u'0\\1')],
    main_country_for_code=True)
