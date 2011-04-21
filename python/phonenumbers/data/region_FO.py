"""Auto-generated file, do not edit by hand. FO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FO = PhoneMetadata(id='FO', country_code=298, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{5}', possible_number_pattern=u'\d{6}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:20|[3-4]\d|8[19])\d{4}', possible_number_pattern=u'\d{6}', example_number=u'201234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:2[1-9]|5\d|7[1-79])\d{4}', possible_number_pattern=u'\d{6}', example_number=u'211234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80[257-9]\d{3}', possible_number_pattern=u'\d{6}', example_number=u'802123'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90(?:[1345][15-7]|2[125-7]|99)\d{2}', possible_number_pattern=u'\d{6}', example_number=u'901123'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'(?:6[0-36]|88)\d{4}', possible_number_pattern=u'\d{6}', example_number=u'601234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix_for_parsing=u'(10(?:01|[12]0|88))',
    number_format=[NumberFormat(pattern='(\d{6})', format=u'\\1', domestic_carrier_code_formatting_rule=u'$CC \\1')])
