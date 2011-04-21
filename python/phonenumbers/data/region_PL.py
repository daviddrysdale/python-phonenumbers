"""Auto-generated file, do not edit by hand. PL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PL = PhoneMetadata(id='PL', country_code=48, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1[2-8]|2[2-59]|3[2-4]|4[1-468]|5[24-689]|6[1-3578]|7[14-7]|8[1-79]|9[145])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'123456789'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[013]|6[069]|7[289]|88)\d{7}', possible_number_pattern=u'\d{9}', example_number=u'512345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'70\d{7}', possible_number_pattern=u'\d{9}', example_number=u'701234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'801\d{6}', possible_number_pattern=u'\d{9}', example_number=u'801234567'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'39\d{7}', possible_number_pattern=u'\d{9}', example_number=u'391234567'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[124]|3[2-4]|5[24-689]|6[1-3578]|7[14-7]|8[1-79]|9[145]']),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['39|5[013]|6[069]|7[0289]|8[08]'])])
