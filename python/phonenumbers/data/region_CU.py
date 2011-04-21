"""Auto-generated file, do not edit by hand. CU metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CU = PhoneMetadata(id='CU', country_code=53, international_prefix='119',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-57]\d{5,7}', possible_number_pattern=u'\d{4,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2[1-4]\d{5,6}|3(?:1\d{6}|[23]\d{4,6})|4(?:[125]\d{5,6}|[36]\d{6}|[78]\d{4,6})|7\d{6,7}', possible_number_pattern=u'\d{4,8}', example_number=u'71234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'5\d{7}', possible_number_pattern=u'\d{8}', example_number=u'51234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d)(\d{6,7})', format=u'\\1 \\2', leading_digits_pattern=['7'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d{2})(\d{4,6})', format=u'\\1 \\2', leading_digits_pattern=['[2-4]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\d)(\d{7})', format=u'\\1 \\2', leading_digits_pattern=['5'], national_prefix_formatting_rule=u'0\\1')])
