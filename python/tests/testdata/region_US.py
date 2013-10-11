"""Auto-generated file, do not edit by hand. US metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_US = PhoneMetadata(id='US', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='1234567890'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='1234567890'),
    mobile=PhoneNumberDesc(national_number_pattern='[13-689]\\d{9}|2[0-35-9]\\d{8}', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='1234567890'),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|66|77|88)\\d{7}', possible_number_pattern='\\d{10}', example_number='1234567890'),
    premium_rate=PhoneNumberDesc(national_number_pattern='900\\d{7}', possible_number_pattern='\\d{10}', example_number='1234567890'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='1234567890'),
    national_prefix='1',
    preferred_extn_prefix=' extn. ',
    national_prefix_for_parsing='1',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', national_prefix_optional_when_formatting=True)],
    intl_number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3')],
    main_country_for_code=True,
    mobile_number_portable_region=True)
