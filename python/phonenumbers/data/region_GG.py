"""Auto-generated file, do not edit by hand. GG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GG = PhoneMetadata(id='GG', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[135789]\\d{6,9}', possible_length=(7, 9, 10), possible_length_local_only=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1481[25-9]\\d{5}', example_number='1481256789', possible_length=(10,), possible_length_local_only=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:781\\d|839\\d|911[17])\\d{5}', example_number='7781123456', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:0(?:1111|\\d{6,7})|8\\d{7})', example_number='8001234567', possible_length=(7, 9, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:87[123]|9(?:[01]\\d|8[0-3]))\\d{7}', example_number='9012345678', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8(?:4(?:5464\\d|[2-5]\\d{7})|70\\d{7})', example_number='8431234567', possible_length=(7, 10)),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{8}', example_number='7012345678', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='56\\d{8}', example_number='5612345678', possible_length=(10,)),
    pager=PhoneNumberDesc(national_number_pattern='76(?:0[012]|2[356]|4[0134]|5[49]|6[0-369]|77|81|9[39])\\d{6}', example_number='7640123456', possible_length=(10,)),
    uan=PhoneNumberDesc(national_number_pattern='(?:3[0347]|55)\\d{8}', example_number='5512345678', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0')
