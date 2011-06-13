"""Auto-generated file, do not edit by hand. JP metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JP = PhoneMetadata(id='JP', country_code=81, international_prefix='010',
    general_desc=PhoneNumberDesc(),
    fixed_line=PhoneNumberDesc(),
    mobile=PhoneNumberDesc(),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['222|333', '(?:222|333)1', '(?:222|333)11'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d)(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['222|333', '2221|3332', '22212|3332', '222120|3332'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})', format=u'*\\1', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'0\\1')])
