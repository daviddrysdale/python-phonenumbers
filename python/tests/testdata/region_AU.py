"""Auto-generated file, do not edit by hand. AU metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='001[12]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-578]\\d{4,14}', possible_number_pattern='\\d{5,15}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2378]\\d{8}', possible_number_pattern='\\d{9}'),
    mobile=PhoneNumberDesc(national_number_pattern='4\\d{8}', possible_number_pattern='\\d{9}'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}'),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0126]\\d{6}', possible_number_pattern='\\d{10}'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    preferred_international_prefix=u'0011',
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(\\d{1})(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-478]'], national_prefix_formatting_rule=u'0\\1')])
