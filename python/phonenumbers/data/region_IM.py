"""Auto-generated file, do not edit by hand. IM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IM = PhoneMetadata(id='IM', country_code=44, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:1624|(?:[3578]\\d|90)\\d\\d)\\d{6}', possible_length=(10,), possible_length_local_only=(6,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1624[5-8]\\d{5}', example_number='1624756789', possible_length=(10,), possible_length_local_only=(6,)),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:4576|[59]24\\d|624[0-4689])\\d{5}', example_number='7924123456', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='808162\\d{4}', example_number='8081624567', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:872299|90[0167]624)\\d{4}', example_number='9016247890', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8(?:4(?:40[49]06|5624\\d)|70624\\d)\\d{3}', example_number='8456247890', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{8}', example_number='7012345678', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='56\\d{8}', example_number='5612345678', possible_length=(10,)),
    uan=PhoneNumberDesc(national_number_pattern='3(?:08162\\d|3\\d{5}|4(?:40[49]06|5624\\d)|7(?:0624\\d|2299\\d))\\d{3}|55\\d{8}', example_number='5512345678', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0')
