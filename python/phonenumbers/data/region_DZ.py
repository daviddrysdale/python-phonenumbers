"""Auto-generated file, do not edit by hand. DZ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DZ = PhoneMetadata(id='DZ', country_code=213, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'(?:[1-4]|[5-9]\d)\d{7}', possible_number_pattern=u'\d{8,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1\d|2[014-79]|3[0-8]|4[0135689])\d{6}|9619\d{5}', possible_number_pattern=u'\d{8,9}', example_number=u'12345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[56]|6[69]|7[79])\d{7}', possible_number_pattern=u'\d{9}', example_number=u'551234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{6}', possible_number_pattern=u'\d{9}', example_number=u'800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'80[3-689]1\d{5}', possible_number_pattern=u'\d{9}', example_number=u'808123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'80[12]1\d{5}', possible_number_pattern=u'\d{9}', example_number=u'801123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'98[23]\d{6}', possible_number_pattern=u'\d{9}', example_number=u'983123456'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([1-4]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[1-4]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([5-8]\d{2})(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[5-8]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9\d)(\d{3})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1')])
