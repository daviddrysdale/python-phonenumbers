"""Auto-generated file, do not edit by hand. GP metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GP = PhoneMetadata(id='GP', country_code=590, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[56]\d{8}', possible_number_pattern=u'\d{9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'590(?:1[12]|2[0-68]|3[28]|4[126-8]|5[067]|6[018]|[89]\d)\d{4}', possible_number_pattern=u'\d{9}', example_number=u'590201234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'690(?:00|1[1-9]|2[013-5]|[3-5]\d|6[0-57-9]|7[1-6]|8[0-6]|9[09])\d{4}', possible_number_pattern=u'\d{9}', example_number=u'690301234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='([56]90)(\d{2})(\d{4})', format=u'\\1 \\2-\\3', national_prefix_formatting_rule=u'0\\1')],
    main_country_for_code=True)
