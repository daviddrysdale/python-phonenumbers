"""Auto-generated file, do not edit by hand. ES metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ES = PhoneMetadata(id='ES', country_code=34, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[5-9]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[89][1-8]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'812345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6\d{8}', possible_number_pattern=u'\d{9}', example_number=u'612345678'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'[89]00\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'80[367]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'803123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'90[12]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'901123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{7}', possible_number_pattern=u'\d{9}', example_number=u'701234567'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'51\d{7}', possible_number_pattern=u'\d{9}', example_number=u'511234567'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([5-9]\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4')])
