"""Auto-generated file, do not edit by hand. IS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IS = PhoneMetadata(id='IS', country_code=354, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[4-9]\\d{6}|38\\d{7}', possible_number_pattern='\\d{7,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:4(?:1[0-245]|2[0-7]|[37][0-8]|4[0245]|5[0-356]|6\\d|8[0-46-8]|9[013-79])|5(?:05|[156]\\d|2[02578]|3[013-6]|4[03-6]|7[0-2578]|8[0-25-9]|9[013-689])|87[23])\\d{4}', possible_number_pattern='\\d{7}', example_number='4101234'),
    mobile=PhoneNumberDesc(national_number_pattern='38[59]\\d{6}|(?:6(?:1[0-8]|3[0-27-9]|4[0-27]|5[0-29]|[67][0-69]|9\\d)|7(?:5[057]|7[0-7])|8(?:2[0-5]|[469]\\d|5[1-9]))\\d{4}', possible_number_pattern='\\d{7,9}', example_number='6101234'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4}', possible_number_pattern='\\d{7}', example_number='8001234'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{5}', possible_number_pattern='\\d{7}', example_number='9011234'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='49[013-79]\\d{4}', possible_number_pattern='\\d{7}', example_number='4931234'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='112', possible_number_pattern='\\d{3}', example_number='112'),
    voicemail=PhoneNumberDesc(national_number_pattern='388\\d{6}|(?:6(?:2[0-8]|49|8\\d)|8(?:2[6-9]|[38]\\d|50|7[014-9])|95[48])\\d{4}', possible_number_pattern='\\d{7,9}', example_number='388123456'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['[4-9]']),
        NumberFormat(pattern='(3\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3'])])
