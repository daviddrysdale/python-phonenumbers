"""Auto-generated file, do not edit by hand. CM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CM = PhoneMetadata(id='CM', country_code=237, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[237-9]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:22|33)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'22123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[79]\d{7}', possible_number_pattern=u'\d{8}', example_number=u'71234567'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{5}', possible_number_pattern=u'\d{8}', example_number=u'80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'88\d{6}', possible_number_pattern=u'\d{8}', example_number=u'88012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([237-9]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[2379]|88']),
        NumberFormat(pattern='(800)(\d{2})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['80'])])
