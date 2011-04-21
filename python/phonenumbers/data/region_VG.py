"""Auto-generated file, do not edit by hand. VG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VG = PhoneMetadata(id='VG', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2589]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'284(?:(?:229|4(?:46|9[45])|8(?:52|6[459]))\d{4}|496[0-5]\d{3})', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'2842291234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'284(?:(?:30[0-3]|4(?:4[0-5]|68|99)|54[0-4])\d{4}|496[6-9]\d{3})', possible_number_pattern=u'\d{10}', example_number=u'2843001234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002345678'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='284')
