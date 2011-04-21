"""Auto-generated file, do not edit by hand. BT metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BT = PhoneMetadata(id='BT', country_code=975, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'(?:17|[2-8])\d{6}', possible_number_pattern=u'\d{6,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2[3-6]|[34][5-7]|5[236]|6[2-46]|7[246]|8[2-4])\d{5}', possible_number_pattern=u'\d{6,7}', example_number=u'2345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'17\d{6}', possible_number_pattern=u'\d{8}', example_number=u'17123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(17)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['1']),
        NumberFormat(pattern='([2-8])(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-8]'])])
