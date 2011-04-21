"""Auto-generated file, do not edit by hand. JO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JO = PhoneMetadata(id='JO', country_code=962, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[235-9]\d{7,8}', possible_number_pattern=u'\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[2356][2-8]\d{6}', possible_number_pattern=u'\d{7,8}', example_number=u'62001234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7(?:[1-8]\d|9[02-9])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'790123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{5}', possible_number_pattern=u'\d{8}', example_number=u'90012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'85\d{6}', possible_number_pattern=u'\d{8}', example_number=u'85012345'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{7}', possible_number_pattern=u'\d{9}', example_number=u'700123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'8(?:10|[78]\d)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'87101234'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2356]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(7)(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4 \\5', leading_digits_pattern=['7[457-9]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{5,6})', format=u'\\1 \\2', leading_digits_pattern=['70|[89]'], national_prefix_formatting_rule=u'0\\1')])
