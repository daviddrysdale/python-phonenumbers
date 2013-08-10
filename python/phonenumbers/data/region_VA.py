"""Auto-generated file, do not edit by hand. VA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VA = PhoneMetadata(id='VA', country_code=379, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='06\\d{8}', possible_number_pattern='\\d{10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='06698\\d{5}', possible_number_pattern='\\d{10}', example_number='0669812345'),
    mobile=PhoneNumberDesc(national_number_pattern='N/A', possible_number_pattern='N/A'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[2358]', possible_number_pattern='\\d{3}', example_number='113'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(06)(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3')],
    leading_zero_possible=True)
