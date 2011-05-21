"""Auto-generated file, do not edit by hand. SC metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SC = PhoneMetadata(id='SC', country_code=248, international_prefix='0[0-2]',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-8]\\d{5,6}', possible_number_pattern='\\d{6,7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2?(?:55[0-5]|78[013])|4?(?:2(?:1[78]|2[14-69]|3[2-4]|4[1-36-8]|6[167]|[89]\\d)|3(?:0[34]|2[1-6]|4[4-6]|55|6[016]|7\\d|8[0-589]|9[0-5])|6(?:0[0-256]|1[0-478]|2[145]|3[02-4]|4[124]|6[015]|7\\d|8[1-3])))\\d{3}', possible_number_pattern='\\d{6,7}', example_number='4217123'),
    mobile=PhoneNumberDesc(national_number_pattern='2?(?:5(?:[0-46-9]\\d|5[6-9])|7(?:[0-79]\\d|8[24-9]))\\d{3}', possible_number_pattern='\\d{6,7}', example_number='2510123'),
    toll_free=PhoneNumberDesc(national_number_pattern='8000\\d{2}', possible_number_pattern='\\d{6}', example_number='800000'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='(?:44[1-3]|647)\\d{4}', possible_number_pattern='\\d{7}', example_number='4410123'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    preferred_international_prefix=u'00',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})', format=u'\\1 \\2', leading_digits_pattern=['[3578]|2[1-4689]|6(?:[0-35-9]|4[0-689])']),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['2[57]|4[2-46]|647'])])
