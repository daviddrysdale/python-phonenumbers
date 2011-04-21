"""Auto-generated file, do not edit by hand. FR metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FR = PhoneMetadata(id='FR', country_code=33, international_prefix='[04579]0',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[1-5]\d{8}', possible_number_pattern=u'\d{9}', example_number=u'123456789'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6\d{8}|7[5-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{7}', possible_number_pattern=u'\d{9}', example_number=u'801234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'89[1-37-9]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'891123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:1[019]|2[0156]|84|90)\d{6}', possible_number_pattern=u'\d{9}', example_number=u'810123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'9\d{8}', possible_number_pattern=u'\d{9}', example_number=u'912345678'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'00',
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([1-79])(\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4 \\5', leading_digits_pattern=['[1-79]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(8\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'0 \\1')])
