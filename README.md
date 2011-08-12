phonenumbers Python Library
===========================

This is a Python port of libphonenumber, originally from:
  http://code.google.com/p/libphonenumber/.

Original Java code is Copyright (C) 2009-2011 Google Inc.

Example Usage
-------------

    >>> import phonenumbers
    >>> x = phonenumbers.parse("+442083661177", None)
    >>> print x
    Country Code: 44 National Number: 2083661177 Leading Zero: False
    >>> type(x)
    <class 'phonenumbers.phonenumber.PhoneNumber'>
    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
    u'020 8366 1177'
    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    u'+44 20 8366 1177'
    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
    u'+442083661177'
    >>> y = phonenumbers.parse("020 8366 1177", "GB")
    >>> print y
    Country Code: 44 National Number: 2083661177 Leading Zero: False
    >>> x == y
    True
    >>>
    >>> formatter = phonenumbers.AsYouTypeFormatter("US")
    >>> print formatter.input_digit("6")
    6
    >>> print formatter.input_digit("5")
    65
    >>> print formatter.input_digit("0")
    (650
    >>> print formatter.input_digit("2")
    (650) 2
    >>> print formatter.input_digit("5")
    (650) 25
    >>> print formatter.input_digit("3")
    (650) 253
    >>> print formatter.input_digit("2")
    650-2532
    >>> print formatter.input_digit("2")
    (650) 253-22
    >>> print formatter.input_digit("2")
    (650) 253-222
    >>> print formatter.input_digit("2")
    (650) 253-2222
    >>>
    >>> text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
    >>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    ...     print match
    ... 
    PhoneNumberMatch [11,23) 510-748-8230
    PhoneNumberMatch [51,62) 703-4800500
    >>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    ...     print phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
    ... 
    +15107488230
    +17034800500
    >>> from phonenumbers.geocoder import area_description_for_number
    >>> ch_number = phonenumbers.parse("0431234567", "CH")
    >>> print repr(area_description_for_number(ch_number, "de"))
    u'Z\\xfcrich'
    >>> print repr(area_description_for_number(ch_number, "en"))
    u'Zurich'
    >>> print repr(area_description_for_number(ch_number, "fr"))
    u'Zurich'
    >>> print repr(area_description_for_number(ch_number, "it"))
    u'Zurigo'
    >>>

Project Layout
--------------
* The python/ directory holds the Python code.
* The resources/ directory is a copy of the resources/
  directory from libphonenumber.  This is not needed
  to run the Python code, but is needed when upstream
  changes to the master XML metadata need to be 
  incorporated.