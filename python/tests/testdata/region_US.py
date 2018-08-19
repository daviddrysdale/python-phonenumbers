"""Auto-generated file, do not edit by hand. US metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_US = PhoneMetadata(id='US', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', possible_length=(10,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', example_number='1234567890', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', example_number='1234567890', possible_length=(10,), possible_length_local_only=(7,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|66|77|88)\\d{7}', example_number='8004567890', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', example_number='9004567890', possible_length=(10,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_length=(10,)),
    national_prefix='1',
    preferred_extn_prefix=' extn. ',
    national_prefix_for_parsing='1',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', national_prefix_optional_when_formatting=True)],
    intl_number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3')],
    main_country_for_code=True,
    mobile_number_portable_region=True)
