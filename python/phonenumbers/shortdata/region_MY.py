"""Auto-generated file, do not edit by hand. MY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MY = PhoneMetadata(id='MY', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[139]\\d{2,4}', possible_length=(3, 4, 5)),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[01348]|[569]\\d)|1(?:[02]|1[128]|311)|2(?:0[125]|[13-6]|2\\d{0,2})|3(?:09\\d|[1-39]\\d{1,2}|6|[5-7]\\d{0,2})|5(?:[12]\\d|454|5\\d{1,2}|77|888|999?)|7(?:[136-9]\\d|[45]\\d{1,2})|8(?:18?|2|8[18])|9(?:[03]\\d|[124]\\d?|68|71|9[0679]))|3[23679]\\d{3}|99[1-469]', example_number='999', possible_length=(3, 4, 5)),
    short_data=True)
