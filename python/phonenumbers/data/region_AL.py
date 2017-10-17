"""Auto-generated file, do not edit by hand. AL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AL = PhoneMetadata(id='AL', country_code=355, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-57]\\d{7}|6\\d{8}|8\\d{5,7}|9\\d{5}', possible_length=(6, 7, 8, 9), possible_length_local_only=(5, 6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[2358](?:[16-9]\\d[2-9]|[2-5][2-9]\\d)|4(?:[2-57-9][2-9]\\d|6\\d{2}))\\d{4}', example_number='22345678', possible_length=(8,), possible_length_local_only=(5, 6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:[689][2-9]|7[2-6])\\d{6}', example_number='662123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4}', example_number='8001234', possible_length=(7,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[1-9]\\d{2}', example_number='900123', possible_length=(6,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='808[1-9]\\d{2}', example_number='808123', possible_length=(6,)),
    personal_number=PhoneNumberDesc(national_number_pattern='700[2-9]\\d{4}', example_number='70021234', possible_length=(8,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(4)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['4[0-6]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(6\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['6'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[2358][2-5]|4[7-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3,5})', format='\\1 \\2', leading_digits_pattern=['[235][16-9]|[79]|8[016-9]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
