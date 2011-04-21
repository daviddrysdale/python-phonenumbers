"""Auto-generated file, do not edit by hand. PG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PG = PhoneMetadata(id='PG', country_code=675, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-9]\d{6,7}', possible_number_pattern=u'\d{7,8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3\d{2}|4[257]\d|5[34]\d|6(?:29|4[1-9])|85[02-46-9]|9[78]\d)\d{4}', possible_number_pattern=u'\d{7}', example_number=u'3123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:68|7(?:[126]\d|3[1-9]))\d{5}', possible_number_pattern=u'\d{7,8}', example_number=u'6812345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'180\d{4}', possible_number_pattern=u'\d{7}', example_number=u'1801234'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'275\d{4}', possible_number_pattern=u'\d{7}', example_number=u'2751234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[1-689]']),
        NumberFormat(pattern='(7[1-36]\d)(\d{2})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7[1-36]'])])
