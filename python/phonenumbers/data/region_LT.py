"""Auto-generated file, do not edit by hand. LT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_LT = PhoneMetadata(id='LT', country_code=370, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[3-9]\\d{7}', possible_number_pattern='\\d{8}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3[1478]|4[124-6]|52)\\d{6}', example_number='31234567', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='6\\d{7}', example_number='61234567', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{5}', possible_number_pattern='\\d{8}', example_number='80012345', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:0[0239]|10)\\d{5}', possible_number_pattern='\\d{8}', example_number='90012345', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='808\\d{5}', possible_number_pattern='\\d{8}', example_number='80812345', possible_length=(8,)),
    personal_number=PhoneNumberDesc(national_number_pattern='700\\d{5}', possible_number_pattern='\\d{8}', example_number='70012345', possible_length=(8,)),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='70[67]\\d{5}', possible_number_pattern='\\d{8}', example_number='70712345', possible_length=(8,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='8',
    national_prefix_for_parsing='[08]',
    number_format=[NumberFormat(pattern='([34]\\d)(\\d{6})', format='\\1 \\2', leading_digits_pattern=['37|4(?:1|5[45]|6[2-4])'], national_prefix_formatting_rule='(8-\\1)', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='([3-6]\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['3[148]|4(?:[24]|6[09])|528|6'], national_prefix_formatting_rule='(8-\\1)', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='([7-9]\\d{2})(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[7-9]'], national_prefix_formatting_rule='8 \\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(5)(2\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['52[0-79]'], national_prefix_formatting_rule='(8-\\1)', national_prefix_optional_when_formatting=True)],
    mobile_number_portable_region=True)
