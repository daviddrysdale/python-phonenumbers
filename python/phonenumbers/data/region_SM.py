"""Auto-generated file, do not edit by hand. SM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SM = PhoneMetadata(id='SM', country_code=378, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[05-7]\d{7,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'0549(?:8[0157-9]|9\d)\d{4}', possible_number_pattern=u'\d{6,10}', example_number=u'0549886377'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6[16]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'66661212'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'7[178]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'71123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'5[158]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'58001110'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix_for_parsing=u'(?:0549)?([89]\d{5})',
    national_prefix_transform_rule=u'0549\\1',
    number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[5-7]']),
        NumberFormat(pattern='(0549)(\d{6})', format=u'\\1 \\2', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\d{6})', format=u'0549 \\1', leading_digits_pattern=['[89]'])],
    intl_number_format=[NumberFormat(pattern='(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[5-7]']),
        NumberFormat(pattern='(0549)(\d{6})', format=u'(\\1) \\2', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\d{6})', format=u'(0549) \\1', leading_digits_pattern=['[89]'])],
    leading_zero_possible=True)
