"""Auto-generated file, do not edit by hand. DK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DK = PhoneMetadata(id='DK', country_code=45, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7}', possible_length=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:(?:2\\d|9[1-46-9])\\d|3(?:[0-37]\\d|4[013]|5[0-58]|6[01347-9]|8[0-8]|9[0-79])|4(?:[0-25]\\d|[34][02-9]|6[013-579]|7[013579]|8[0-47]|9[0-27])|5(?:[0-36]\\d|4[0146-9]|5[03-57-9]|7[0568]|8[0-358]|9[0-69])|6(?:[013578]\\d|2[0-68]|4[02-8]|6[01689]|9[015689])|7(?:[0-69]\\d|7[03-9]|8[0147])|8(?:[16-9]\\d|2[0-58]))\\d{5}', example_number='32123456', possible_length=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:[2-7]\\d|8[126-9]|9[1-46-9])\\d{6}', example_number='34412345', possible_length=(8,)),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{6}', example_number='80123456', possible_length=(8,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='90\\d{6}', example_number='90123456', possible_length=(8,)),
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[2-9]'])],
    mobile_number_portable_region=True)
