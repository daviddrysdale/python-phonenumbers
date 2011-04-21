"""Auto-generated file, do not edit by hand. BW metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BW = PhoneMetadata(id='BW', country_code=267, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-9]\d{6,7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2(?:4[0-48]|6[0-24]|9[0578])|3(?:1[0235-9]|55|6\d|7[01]|9[0-57])|4(?:6[03]|7[1267]|9[0-5])|5(?:3[0389]|4[0489]|7[1-47]|88|9[0-49])|6(?:2[1-35]|5[149]|8[067]))\d{4}', possible_number_pattern=u'\d{7}', example_number=u'2401234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7(?:[1-3]\d{6}|4[0-7]\d{5})', possible_number_pattern=u'\d{8}', example_number=u'71123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8\d{6}', possible_number_pattern=u'\d{7}', example_number=u'8123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{5}', possible_number_pattern=u'\d{7}', example_number=u'9012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(7[1-4])(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7']),
        NumberFormat(pattern='(90)(\d{5})', format=u'\\1 \\2', leading_digits_pattern=['9'])])
