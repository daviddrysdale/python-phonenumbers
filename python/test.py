import phonenumbers

# Fixed by Phonenumbers Cases
valid_strings = ['+6323168971',
                 '+442083661177',
                 '+658003211137',
                 '+20573925008',
                 '+2057392500',
                 '+20225777444',
                 '+84384813220',
                 '+84357659677',
                 '+56232512653',  # https://switchcomm.atlassian.net/browse/TEL-9285
                 '+525547808256']

print '######### - VALID BY LIBRARY - ################'
for l in valid_strings:
  x = phonenumbers.parse(l, None)
  print (x), '%10s' % phonenumbers.is_valid_number(x)


# To be fixed by Dialpad Changes
dialpad_cases = ['+6278033212174',  # https://switchcomm.atlassian.net/browse/DP-13742
                 '+63283168971',  # Philipines
                 '+8031000000141',  # Dialpadistan
                 ]

print '######### - VALID BY DIALPAD - ################'
for l in dialpad_cases:
  try:
    x = phonenumbers.parse(l, None)
    print (x), '%10s' % phonenumbers.is_valid_number(x)
  except Exception as e:
    print (l), '%10s' % (e)

# Invalid Strings
invalid_strings = ['+4916190899790',  # https://switchcomm.atlassian.net/browse/TEL-8824  Not Fixed
                   '+2022577744',
                   '+205739250',
                   '+8412032453',  # https://switchcomm.atlassian.net/browse/DP-13742
                   ]

print '######### - INVALID NUMBERS - ################'
for l in invalid_strings:
  x = phonenumbers.parse(l, None)
  print (x), '%10s' % phonenumbers.is_valid_number(x)

# National Format match
national_format_match = {'+525547808256': '55 4780 8256'}

print '######### - NUMBER FORMAT VALIDITY - ################'
for l in national_format_match:
  x = phonenumbers.parse(l, None)
  y = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
  if national_format_match[l] == y:
    status = 'Success'
  else:
    status = 'Failed'
  print (l), '-> %10s : %s' % (y, status)

# Number validity check
number_validity_check = {'1932621160': 'BR'}
print '######### - REGION NUMBER VALIDITY - ###############'
for l in number_validity_check:
  region = number_validity_check[l]
  x = phonenumbers.parse(l, region)
  print (x), 'Region : %s -> %10s' % (region, phonenumbers.is_valid_number(x))
