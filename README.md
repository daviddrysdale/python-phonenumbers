phonenumbers Python Library
===========================

This is a Python port of libphonenumber, originally from:
  [http://code.google.com/p/libphonenumber/](http://code.google.com/p/libphonenumber/).

Original Java code is Copyright (C) 2009-2011 The Libphonenumber Authors

Example Usage
-------------

The main object that the library deals with is a `PhoneNumber` object.  You can create this from a string
representing a phone number using the `parse` function, but you normally also need to specify the country
that the phone number is from (unless the number is in E.164 format).

    >>> import phonenumbers
    >>> x = phonenumbers.parse("+442083661177", None)
    >>> print x
    Country Code: 44 National Number: 2083661177 Leading Zero: False
    >>> type(x)
    <class 'phonenumbers.phonenumber.PhoneNumber'>
    >>> y = phonenumbers.parse("020 8366 1177", "GB")
    >>> print y
    Country Code: 44 National Number: 2083661177 Leading Zero: False
    >>> x == y
    True

The `PhoneNumber` object that `parse` produces typically still needs to be validated, to check whether
it's a *possible* number (e.g. it has the right number of digits) or a *valid* number (e.g. it's
in an assigned exchange).

    >>> z = phonenumbers.parse("+120012301", None)
    >>> print z
    Country Code: 1 National Number: 20012301 Leading Zero: False
    >>> phonenumbers.is_possible_number(z)  # too few digits for USA
    False
    >>> phonenumbers.is_valid_number(z)
    False
    >>> z = phonenumbers.parse("+12001230101", None)
    >>> print z
    Country Code: 1 National Number: 2001230101 Leading Zero: False
    >>> phonenumbers.is_possible_number(z)
    True
    >>> phonenumbers.is_valid_number(z)  # NPA 200 not used
    False

Once you've got a phone number, a common task is to format it in a standardized format.  There are a few
formats available (under `PhoneNumberFormat`), and the `format_number` function does the formatting.

    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
    u'020 8366 1177'
    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    u'+44 20 8366 1177'
    >>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
    u'+442083661177'

If your application has a UI that allows the user to type in a phone number, it's nice to get the formatting
applied as the user types.   The `AsYouTypeFormatter` object allows this.

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

Sometimes, you've got a larger block of text that may or may not have some phone numbers inside it.  For this,
the `PhoneNumberMatcher` object provides the relevant functionality; you can iterate over it to retrieve a
sequence of `PhoneNumberMatch` objects.  Each of these match objects holds a `PhoneNumber` object together
with information about where the match occurred in the original string.

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

Finally, you might want to get some information about the location that corresponds to a phone number.  The
`geocoder.area_description_for_number` does this, when possible.

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

For more information about the other functionality available from the library, look in the unit tests or in the original
[libphonenumber project](http://code.google.com/p/libphonenumber/).

Project Layout
--------------
* The `python/` directory holds the Python code.
* The `resources/` directory is a copy of the `resources/`
  directory from
  [libphonenumber](http://code.google.com/p/libphonenumber/source/browse/#svn%2Ftrunk%2Fresources).
  This is not needed to run the Python code, but is needed when upstream
  changes to the master metadata need to be incorporated.
* The `tools/` directory holds the tools that are used to process upstream
  changes to the master metadata.
