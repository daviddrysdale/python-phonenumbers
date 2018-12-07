"""Auto-generated file, do not edit by hand. SI metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SI = PhoneMetadata(id='SI', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2,5}', possible_length=(3, 4, 5, 6)),
    toll_free=PhoneNumberDesc(national_number_pattern='11(?:(?:[08]|6\\d)\\d\\d|[23])|118\\d', example_number='112', possible_length=(3, 4, 5, 6)),
    emergency=PhoneNumberDesc(national_number_pattern='11[23]', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:00[146]|[23]|6(?:000|1(?:11|23))|8(?:[08]|99))|9(?:0(?:59|8[09])|1(?:0[12]|16)|5|70|8(?:1[09]|7)|9(?:00|[149])))', example_number='112', possible_length=(3, 4, 5, 6)),
    short_data=True)
