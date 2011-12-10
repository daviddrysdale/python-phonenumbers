"""Auto-generated file, do not edit by hand. ZA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZA = PhoneMetadata(id='ZA', country_code=27, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-5]\\d{8}|(?:7\\d{4,8}|8[1-5789]\\d{3,7})|8[06]\\d{7}', possible_number_pattern='\\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[0-8]|2[1-478]|3[1-69]|4\\d|5[1346-8])\\d{7}', possible_number_pattern='\\d{8,9}', example_number='101234567'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7[1-4689]|8[1-5789])\\d{3,7}', possible_number_pattern='\\d{5,9}', example_number='711234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', possible_number_pattern='\\d{9}', example_number='801234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='86[1-9]\\d{6}', possible_number_pattern='\\d{9}', example_number='861234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='860\\d{6}', possible_number_pattern='\\d{9}', example_number='860123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='87\\d{7}', possible_number_pattern='\\d{9}', example_number='871234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:01(?:11|77)|12)', possible_number_pattern='\\d{3,5}', example_number='10111'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(860)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['860'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([1-578]\\d)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-57]|8(?:[0-57-9]|6[1-9])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})', format=u'\\1 \\2', leading_digits_pattern=['7|8[1-5789]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7|8[1-5789]'], national_prefix_formatting_rule=u'0\\1')])
