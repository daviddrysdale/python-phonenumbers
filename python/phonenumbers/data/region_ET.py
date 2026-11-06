"""Auto-generated file, do not edit by hand. ET metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ET = PhoneMetadata(id='ET', country_code=251, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:11|[2-57-9]\\d)\\d{7}', possible_length=(9,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:11(?:[124]\\d\\d|3(?:[0-79]\\d|8[0-7])|5(?:[02-9]\\d|1[0-57-9])|6(?:[02-79]\\d|1[0-57-9]|8[0-8]))|2(?:2(?:11[1-9]|22[0-7]|33\\d|44[1467]|66[1-68])|5(?:11[124-6]|33[2-8]|44[1467]|55[14]|66[1-3679]|77[124-79]|880))|3(?:3(?:11[0-46-8]|(?:22|55)[0-6]|33[0134689]|44[04]|66[01467])|4(?:44[0-8]|55[0-69]|66[0-3]|77[1-5]))|4(?:6(?:119|22[0-24-7]|33[1-5]|44[13-69]|55[14-689]|660|88[1-4])|7(?:(?:11|22)[1-9]|33[13-7]|44[13-6]|55[1-689]))|5(?:7(?:227|55[05]|(?:66|77)[14-8])|8(?:11[149]|22[013-79]|33[0-68]|44[013-8]|550|66[1-5]|77\\d)))\\d{4}', example_number='111112345', possible_length=(9,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:[03]\\d|1[0-8]|2[1-35-79]|77|86|99)|(?:8[01]|9\\d)\\d)\\d{6}', example_number='911234567', possible_length=(9,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[1-57-9]'], national_prefix_formatting_rule='0\\1')])
