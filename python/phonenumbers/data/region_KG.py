"""Auto-generated file, do not edit by hand. KG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KG = PhoneMetadata(id='KG', country_code=996, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[356-8]\\d{8}', possible_number_pattern='\\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:1(?:2\\d|3[1-9]|52|6[1-8])|2(?:22|3[0-479]|6[0-7])|4(?:22|5[6-9]|6[0-4])|5(?:22|3[4-7]|59|6[0-5])|6(?:22|5[35-7]|6[0-3])|7(?:22|3[468]|4[1-8]|59|6\\d|7[5-7])|9(?:22|4[1-7]|6[0-8]))|6(?:09|12|2[2-4])\\d)\\d{5}', possible_number_pattern='\\d{5,9}', example_number='312123456'),
    mobile=PhoneNumberDesc(national_number_pattern='5[124-7]\\d{7}|7(?:0[05]|7\\d)\\d{6}', possible_number_pattern='\\d{9}', example_number='700123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['31[25]|[5-8]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['3(?:1[36]|[2-9])'], national_prefix_formatting_rule=u'0\\1')])
