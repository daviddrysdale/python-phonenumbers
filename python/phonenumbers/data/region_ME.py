"""Auto-generated file, do not edit by hand. ME metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ME = PhoneMetadata(id='ME', country_code=382, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{7,8}', possible_number_pattern=u'\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:20[2-8]|3(?:0[2-7]|1[35-7]|2[367]|3[4-7])|4(?:0[237]|1[2467])|5(?:0[47]|1[27]|2[378]))\d{5}', possible_number_pattern=u'\d{6,8}', example_number=u'30234567'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6(?:32\d|[89]\d{2}|7(?:[0-8]\d|9(?:[3-9]|[0-2]\d)))\d{4}', possible_number_pattern=u'\d{8,9}', example_number=u'67622901'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800[28]\d{4}', possible_number_pattern=u'\d{8}', example_number=u'80080002'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'(?:88\d|9(?:4[13-8]|5[16-8]))\d{5}', possible_number_pattern=u'\d{8}', example_number=u'94515151'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'78[134579]\d{5}', possible_number_pattern=u'\d{8}', example_number=u'78108780'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'77\d{6}', possible_number_pattern=u'\d{8}', example_number=u'77273012'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-57-9]|6[3789]', '[2-57-9]|6(?:[389]|7(?:[0-8]|9[3-9]))'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(67)(9)(\d{3})(\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['679', '679[0-2]'], national_prefix_formatting_rule=u'0\\1')])
