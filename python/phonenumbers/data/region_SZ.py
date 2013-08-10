"""Auto-generated file, do not edit by hand. SZ metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SZ = PhoneMetadata(id='SZ', country_code=268, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[027]\\d{7}', possible_number_pattern='\\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:2(?:0[07]|[13]7|2[57])|3(?:0[34]|[1278]3|3[23]|[46][34])|(?:40[4-69]|67)|5(?:0[5-7]|1[6-9]|[23][78]|48|5[01]))\\d{4}', possible_number_pattern='\\d{8}', example_number='22171234'),
    mobile=PhoneNumberDesc(national_number_pattern='7[6-8]\\d{6}', possible_number_pattern='\\d{8}', example_number='76123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='0800\\d{4}', possible_number_pattern='\\d{8}', example_number='08001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='999', possible_number_pattern='\\d{3}', example_number='999'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='0800\\d{4}', possible_number_pattern='\\d{8}', example_number='08001234'),
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[027]'])],
    leading_zero_possible=True)
