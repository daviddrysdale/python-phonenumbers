"""Auto-generated file, do not edit by hand. IM metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IM = PhoneMetadata(id='IM', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[135789]\d{6,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'1624\d{6}', possible_number_pattern=u'\d{6,10}', example_number=u'1624456789'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[569]24\d{6}', possible_number_pattern=u'\d{10}', example_number=u'7924123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'808162\d{4}', possible_number_pattern=u'\d{10}', example_number=u'8081624567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'(?:872299|90[0167]624)\d{4}', possible_number_pattern=u'\d{10}', example_number=u'9016247890'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:4(?:40[49]06|5624\d)|70624\d)\d{3}', possible_number_pattern=u'\d{10}', example_number=u'8456247890'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{8}', possible_number_pattern=u'\d{10}', example_number=u'7012345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'56\d{8}', possible_number_pattern=u'\d{10}', example_number=u'5612345678'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'3(?:08162\d|3\d{5}|4(?:40[49]06|5624\d)|7(?:0624\d|2299\d))\d{3}|55\d{8}', possible_number_pattern=u'\d{10}', example_number=u'5512345678'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    preferred_extn_prefix=u' x',
    national_prefix_for_parsing=u'0')
