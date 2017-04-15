"""Auto-generated file, do not edit by hand. VG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VG = PhoneMetadata(id='VG', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[2589]\\d{9}', possible_length=(10,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='284(?:(?:229|4(?:22|9[45])|774|8(?:52|6[459]))\\d{4}|496[0-5]\\d{3})', example_number='2842291234', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='284(?:(?:3(?:0[0-3]|4[0-7]|68|9[34])|4(?:4[0-6]|68|99)|54[0-57])\\d{4}|496[6-9]\\d{3})', example_number='2843001234', possible_length=(10,), possible_length_local_only=(7,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|33|44|55|66|77|88)[2-9]\\d{6}', example_number='8002345678', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[2-9]\\d{6}', example_number='9002345678', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='5(?:00|22|33|44|66|77|88)[2-9]\\d{6}', example_number='5002345678', possible_length=(10,)),
    national_prefix='1',
    national_prefix_for_parsing='1',
    leading_digits='284')
