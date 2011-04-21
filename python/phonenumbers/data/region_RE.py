"""Auto-generated file, do not edit by hand. RE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RE = PhoneMetadata(id='RE', country_code=262, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[268]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'262\d{6}', possible_number_pattern=u'\d{9}', example_number=u'262161234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6(?:9[23]|47)\d{6}', possible_number_pattern=u'\d{9}', example_number=u'692123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{7}', possible_number_pattern=u'\d{9}', example_number=u'801234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'89[1-37-9]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'891123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:1[019]|2[0156]|84|90)\d{6}', possible_number_pattern=u'\d{9}', example_number=u'810123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([268]\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', national_prefix_formatting_rule=u'0\\1')],
    main_country_for_code=True,
    leading_digits='262|6[49]|8')
