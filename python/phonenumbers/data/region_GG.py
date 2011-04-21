"""Auto-generated file, do not edit by hand. GG metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GG = PhoneMetadata(id='GG', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[135789]\d{6,9}', possible_number_pattern=u'\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'1481\d{6}', possible_number_pattern=u'\d{6,10}', example_number=u'1481456789'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7(?:781|839|911)\d{6}', possible_number_pattern=u'\d{10}', example_number=u'7781123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80(?:0(?:1111|\d{6,7})|8\d{7})|500\d{6}', possible_number_pattern=u'\d{7}(?:\d{2,3})?', example_number=u'8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'(?:87[123]|9(?:[01]\d|8[0-3]))\d{7}', possible_number_pattern=u'\d{10}', example_number=u'9012345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'8(?:4(?:5464\d|[2-5]\d{7})|70\d{7})', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'8431234567'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{8}', possible_number_pattern=u'\d{10}', example_number=u'7012345678'),
    voip=PhoneNumberDesc(national_number_pattern=u'56\d{8}', possible_number_pattern=u'\d{10}', example_number=u'5612345678'),
    pager=PhoneNumberDesc(national_number_pattern=u'76(?:0[012]|2[356]|4[0134]|5[49]|6[0-369]|77|81|9[39])\d{6}', possible_number_pattern=u'\d{10}', example_number=u'7640123456'),
    uan=PhoneNumberDesc(national_number_pattern=u'(?:3[0347]|55)\d{8}', possible_number_pattern=u'\d{10}', example_number=u'5512345678'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    preferred_extn_prefix=u' x',
    national_prefix_for_parsing=u'0')
