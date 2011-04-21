"""Auto-generated file, do not edit by hand. GB metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GB = PhoneMetadata(id='GB', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{10}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[1-6]\d{9}', possible_number_pattern=u'\d{6,10}'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[1-57-9]\d{8}', possible_number_pattern=u'\d{10}'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{8}', possible_number_pattern=u'\d{10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'9[018]\d{8}', possible_number_pattern=u'\d{10}'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:4[3-5]|7[0-2])\d{7}', possible_number_pattern=u'\d{10}'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{8}', possible_number_pattern=u'\d{10}'),
    voip=PhoneNumberDesc(national_number_pattern=u'56\d{8}', possible_number_pattern=u'\d{10}'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{2})(\d{4})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-59]|[78]0'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d)(\d{3})(\d{3})(\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['6'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{4})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7[1-57-9]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8[47]'], national_prefix_formatting_rule=u'(0\\1)')])
