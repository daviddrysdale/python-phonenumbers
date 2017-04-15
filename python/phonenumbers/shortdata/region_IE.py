"""Auto-generated file, do not edit by hand. IE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IE = PhoneMetadata(id='IE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[159]\\d{2,5}', possible_length=(3, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='116\\d{3}', example_number='116000', possible_length=(6,)),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11(?:2|6(?:00[06]|1(?:11|23)))|51210|999', example_number='112', possible_length=(3, 5, 6)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='51210', example_number='51210', possible_length=(5,)),
    short_data=True)
