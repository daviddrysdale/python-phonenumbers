"""Auto-generated file, do not edit by hand. TC metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TC = PhoneMetadata(id='TC', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[5689]\d{9}', possible_number_pattern=u'\d{7}(?:\d{3})?'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'649(?:712|9(?:4\d|50))\d{4}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'6497121234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'649(?:2(?:3[12]|4[1-5])|3(?:3[1-39]|4[1-57])|4[34][12])\d{4}', possible_number_pattern=u'\d{10}', example_number=u'6492311234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|55|66|77|88)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'8002345678'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'9002345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'5(?:00|33|44)[2-9]\d{6}', possible_number_pattern=u'\d{10}', example_number=u'5002345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'64971[01]\d{4}', possible_number_pattern=u'\d{10}', example_number=u'6497101234'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'1',
    national_prefix_for_parsing=u'1',
    leading_digits='649')
