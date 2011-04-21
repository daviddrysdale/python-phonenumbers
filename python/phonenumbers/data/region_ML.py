"""Auto-generated file, do not edit by hand. ML metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ML = PhoneMetadata(id='ML', country_code=223, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[246-8]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:0(?:2[0-589]|7[027-9])|1(?:2[5-7]|[3-689]\d))|442\d)\d{4}', possible_number_pattern=u'\d{8}', example_number=u'20212345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:6(?:[569]\d)|7(?:[08][1-9]|[3579][0-4]|4[014-7]|6\d))\d{5}', possible_number_pattern=u'\d{8}', example_number=u'65012345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([246-8]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
