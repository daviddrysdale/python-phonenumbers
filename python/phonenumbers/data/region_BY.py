"""Auto-generated file, do not edit by hand. BY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BY = PhoneMetadata(id='BY', country_code=375, international_prefix='810',
    general_desc=PhoneNumberDesc(national_number_pattern='[12-4]\\d{8}|[89]\\d{9,10}', possible_number_pattern='\\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1(?:5(?:1[1-5]|2\\d|6[1-4]|9[1-7])|6(?:[235]\\d|4[1-7])|7\\d{2})|2(?:1(?:[246]\\d|3[0-35-9]|5[1-9])|2(?:[235]\\d|4[0-8])|3(?:2\\d|3[02-79]|4[024-7]|5[0-7])))\\d{5}', possible_number_pattern='\\d{7,9}', example_number='152450911'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:2(?:5[5679]|9[1-9])|33\\d|44\\d)\\d{6}', possible_number_pattern='\\d{9}', example_number='294911911'),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:0[13]|20\\d)\\d{7}', possible_number_pattern='\\d{10,11}', example_number='8011234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:810|902)\\d{7}', possible_number_pattern='\\d{10}', example_number='9021234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[123]|12)', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='8(?:[01]|20)\\d{8}|902\\d{7}', possible_number_pattern='\\d{10,11}', example_number='82012345678'),
    preferred_international_prefix='8~10',
    national_prefix='8',
    national_prefix_for_parsing='80?',
    number_format=[NumberFormat(pattern='([1-4]\\d)(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-4]'], national_prefix_formatting_rule=u'8 0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8[01]|9'], national_prefix_formatting_rule=u'8 \\1'),
        NumberFormat(pattern='(8\\d{2})(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['82'], national_prefix_formatting_rule=u'8 \\1')])
