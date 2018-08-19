"""Auto-generated file, do not edit by hand. JE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JE = PhoneMetadata(id='JE', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:1534|(?:[3578]\\d|90)\\d\\d)\\d{6}', possible_length=(10,), possible_length_local_only=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1534[0-24-8]\\d{5}', example_number='1534456789', possible_length=(10,), possible_length_local_only=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:509\\d|7(?:00[378]|97[7-9])|829\\d|937\\d)\\d{5}', example_number='7797712345', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80(?:07(?:35|81)|8901)\\d{4}', example_number='8007354567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:871206|90(?:066[59]|1810|71(?:07|55)))\\d{4}', example_number='9018105678', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8(?:4(?:4(?:4(?:05|42|69)|703)|5(?:041|800))|70002)\\d{4}', example_number='8447034567', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='701511\\d{4}', example_number='7015115678', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='56\\d{8}', example_number='5612345678', possible_length=(10,)),
    pager=PhoneNumberDesc(national_number_pattern='76(?:0[012]|2[356]|4[0134]|5[49]|6[0-369]|77|81|9[39])\\d{6}', example_number='7640123456', possible_length=(10,)),
    uan=PhoneNumberDesc(national_number_pattern='3(?:0(?:07(?:35|81)|8901)|3\\d{4}|4(?:4(?:4(?:05|42|69)|703)|5(?:041|800))|7(?:0002|1206))\\d{4}|55\\d{8}', example_number='5512345678', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0')
