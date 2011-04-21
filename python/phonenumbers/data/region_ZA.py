"""Auto-generated file, do not edit by hand. ZA metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=27, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{9}', possible_number_pattern=u'\d{8,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1[0-8]|2[1-478]|3[1-69]|4\d|5[1346-8])\d{7}', possible_number_pattern=u'\d{8,9}', example_number=u'101234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:7[1-4689]|8[1-5789])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'711234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{7}', possible_number_pattern=u'\d{9}', example_number=u'801234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'86[1-9]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'861234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'860\d{6}', possible_number_pattern=u'\d{9}', example_number=u'860123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'87\d{7}', possible_number_pattern=u'\d{9}', example_number=u'871234567'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(860)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['860'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([1-578]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-57]|8(?:[0-57-9]|6[1-9])'], national_prefix_formatting_rule=u'0\\1')])
