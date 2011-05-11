"""Auto-generated file, do not edit by hand. RS metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RS = PhoneMetadata(id='RS', country_code=381, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-46-9]\\d{4,11}', possible_number_pattern='\\d{5,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-3]\\d{6,9}', possible_number_pattern='\\d{5,10}', example_number='1012345'),
    mobile=PhoneNumberDesc(national_number_pattern='6[0-689]\\d{3,10}', possible_number_pattern='\\d{5,12}', example_number='6012345'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{3,6}', possible_number_pattern='\\d{6,9}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:9[0-2]|42)\\d{4,7}', possible_number_pattern='\\d{6,9}', example_number='90012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([23]\\d{2})(\\d{4,7})', format=u'\\1 \\2', leading_digits_pattern=['(?:2[389]|39)0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([1-4]\\d)(\\d{4,8})', format=u'\\1 \\2', leading_digits_pattern=['1|2(?:[0-24-7]|[389][1-9])|3(?:[0-8]|9[1-9])|42'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(6[0-689])(\\d{3,10})', format=u'\\1 \\2', leading_digits_pattern=['6'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{3,6})', format=u'\\1 \\2', leading_digits_pattern=['[89]'], national_prefix_formatting_rule=u'0\\1')])
