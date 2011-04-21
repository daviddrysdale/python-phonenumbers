"""Auto-generated file, do not edit by hand. RO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RO = PhoneMetadata(id='RO', country_code=40, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[237-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[23][13-6]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'211234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[1-8]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'712345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90[036]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'801\d{6}', possible_number_pattern=u'\d{9}', example_number=u'801123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'802\d{6}', possible_number_pattern=u'\d{9}', example_number=u'802123456'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    preferred_extn_prefix=u' int ',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([237]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23]1|7'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23][02-9]|[89]'], national_prefix_formatting_rule=u'0\\1')])
