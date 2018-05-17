"""Auto-generated file, do not edit by hand. TR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TR = PhoneMetadata(id='TR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{2,4}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:22|3[126]|4[04]|5[16-9]|6[18]|77|83)', example_number='183', possible_length=(3,)),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:1[02]|55)', example_number='112', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1(?:[0239]|811)|2[126]|3(?:[126]|37?|[58]6|65)|4(?:[014]|71)|5(?:[135-9]|07|78)|6(?:[02]6|[1389]|99)|7[0-79]|8(?:\\d|63|95))|2(?:077|268|4(?:17|23)|5(?:7[26]|82)|6[14]4|8\\d{2}|9(?:30|89))|3(?:0(?:05|72)|353|4(?:06|30|64)|502|674|747|851|9(?:1[29]|60))|4(?:0(?:25|3[12]|[47]2)|3(?:3[13]|[89]1)|439|5(?:43|55)|717|832)|5(?:145|290|[4-6]\\d{2}|772|833|9(?:[06]1|92))|6(?:236|6(?:12|39|8[59])|769)|7890|8(?:688|7(?:28|65)|85[06])|9(?:159|290)', example_number='112', possible_length=(3, 4, 5)),
    standard_rate=PhoneNumberDesc(national_number_pattern='2850|5420', example_number='5420', possible_length=(4,)),
    sms_services=PhoneNumberDesc(national_number_pattern='1(?:3(?:37|[58]6|65)|4(?:4|71)|5(?:07|78)|6(?:[02]6|99)|8(?:3|63|95))|2(?:077|268|4(?:17|23)|5(?:7[26]|82)|6[14]4|8\\d{2}|9(?:30|89))|3(?:0(?:05|72)|353|4(?:06|30|64)|502|674|747|851|9(?:1[29]|60))|4(?:0(?:25|3[12]|[47]2)|3(?:3[13]|[89]1)|439|5(?:43|55)|717|832)|5(?:145|290|[4-6]\\d{2}|772|833|9(?:[06]1|92))|6(?:236|6(?:12|39|8[59])|769)|7890|8(?:688|7(?:28|65)|85[06])|9(?:159|290)', example_number='5420', possible_length=(3, 4)),
    short_data=True)
