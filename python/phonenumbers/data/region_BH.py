"""Auto-generated file, do not edit by hand. BH metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BH = PhoneMetadata(id='BH', country_code=973, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[136-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1(?:3[3-6]|6[0156]|7\d)|6(?:1[16]|6[03469]|9[69])|77\d)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'17001234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:3(?:[369]\d|77|8[38])|6(?:1[16]|6[03469]|9[69])|77\d)\d{5}', possible_number_pattern=u'\d{8}', example_number=u'36001234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'(?:87|9[014578])\d{6}', possible_number_pattern=u'\d{8}', example_number=u'90123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'84\d{6}', possible_number_pattern=u'\d{8}', example_number=u'84123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{4})(\d{4})', format=u'\\1 \\2')])
