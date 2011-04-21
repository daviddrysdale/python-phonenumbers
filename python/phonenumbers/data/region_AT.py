"""Auto-generated file, do not edit by hand. AT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AT = PhoneMetadata(id='AT', country_code=43, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'\d{4,13}', possible_number_pattern=u'\d{3,13}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'1\d{3,12}|(?:2(?:1[467]|2[134-8]|5[2357]|6[1-46-8]|7[1-8]|8[124-7]|8[1458])|3(?:1[1-8]|3[23568]|4[5-7]|5[1378]|6[1-38]|8[3-68])|4(?:2[1-8]|35|63|7[1368]|8[2457])|5(?:1[27]|2[1-8]|3[357]|4[147]|5[12578]|6[37])|6(?:13|2[1-47]|4[1-35-8]|5[468]|62)|7(?:2[1-8]|3[25]|4[13478]|5[68]|6[16-8]|7[1-6]|9[45]))\d{3,10}|5(?:0[1-9]|[79]\d)\d{2,10}|720\d{6,10}', possible_number_pattern=u'\d{3,13}', example_number=u'1234567890'),
    mobile=PhoneNumberDesc(national_number_pattern=u'6(?:44|5[0-3579]|6[013-9]|[7-9]\d)\d{4,10}', possible_number_pattern=u'\d{7,13}', example_number=u'644123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80[02]\d{6,10}', possible_number_pattern=u'\d{9,13}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'(?:711|9(?:0[01]|3[019]))\d{6,10}', possible_number_pattern=u'\d{9,13}', example_number=u'900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:10|2[018])\d{6,10}', possible_number_pattern=u'\d{9,13}', example_number=u'810123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'780\d{6,10}', possible_number_pattern=u'\d{9,13}', example_number=u'780123456'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([15])(\d{3,12})', format=u'\\1 \\2', leading_digits_pattern=['1|5[079]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{3})(\d{3,10})', format=u'\\1 \\2', leading_digits_pattern=['316|46|51|732|6(?:44|5[0-3579]|[6-9])|7(?:1|[28]0)|[89]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\d{4})(\d{3,9})', format=u'\\1 \\2', leading_digits_pattern=['2|3(?:1[1-578]|[3-8])|4[2378]|5[2-6]|6(?:[12]|4[1-35-9]|5[468])|7(?:2[1-8]|35|4[1-8]|[57-9])'], national_prefix_formatting_rule=u'0\\1')])
