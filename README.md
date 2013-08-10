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

```pycon
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
```

The `PhoneNumber` object that `parse` produces typically still needs to be validated, to check whether
it's a *possible* number (e.g. it has the right number of digits) or a *valid* number (e.g. it's
in an assigned exchange).

```pycon
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
```

The `parse` function will also fail completely (with a `NumberParseException`) on inputs that cannot
be uniquely parsed, or that  can't possibly be phone numbers.

```pycon
>>> z = phonenumbers.parse("02081234567", None)  # no region, no + => unparseable
Traceback (most recent call last):
  File "phonenumbers/phonenumberutil.py", line 2350, in parse
    "Missing or invalid default region.")
phonenumbers.phonenumberutil.NumberParseException: (0) Missing or invalid default region.
>>> z = phonenumbers.parse("gibberish", None)
Traceback (most recent call last):
  File "phonenumbers/phonenumberutil.py", line 2344, in parse
    "The string supplied did not seem to be a phone number.")
phonenumbers.phonenumberutil.NumberParseException: (1) The string supplied did not seem to be a phone number.
```

Once you've got a phone number, a common task is to format it in a standardized format.  There are a few
formats available (under `PhoneNumberFormat`), and the `format_number` function does the formatting.

```pycon
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
u'020 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
u'+44 20 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
u'+442083661177'
```

If your application has a UI that allows the user to type in a phone number, it's nice to get the formatting
applied as the user types.   The `AsYouTypeFormatter` object allows this.

```pycon
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
```

Sometimes, you've got a larger block of text that may or may not have some phone numbers inside it.  For this,
the `PhoneNumberMatcher` object provides the relevant functionality; you can iterate over it to retrieve a
sequence of `PhoneNumberMatch` objects.  Each of these match objects holds a `PhoneNumber` object together
with information about where the match occurred in the original string.

```pycon
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
```

Finally, you might want to get some information about the location that corresponds to a phone number.  The
`geocoder.area_description_for_number` does this, when possible.

```pycon
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
```

For more information about the other functionality available from the library, look in the unit tests or in the original
[libphonenumber project](http://code.google.com/p/libphonenumber/).

Memory Usage
------------

The library includes a lot of metadata, giving a significant memory overhead.  This metadata is loaded on-demand so that
the memory footprint of applications that only use a subset of the library functionality is not adversely affected.

In particular:

* The geocoding metadata (which makes up around 75% of the total memory footprint) is only loaded on the first use of
  one of the geocoding functions (`description_for_number`, `description_for_valid_number`,
  `area_description_for_number` and `country_name_for_number`).
* The normal metadata for each region is only loaded on the first time that metadata for that region is needed.

If you need to ensure that the metadata memory use is accounted for at start of day (i.e. that a subsequent on-demand
load of metadata will not cause memory exhaustion):

* Force-load the geocoding metadata by invoking `import phonenumbers.geocoder`.
* Force-load the normal metadata by calling `phonenumbers.PhoneMetadata.load_all()`.

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

Python 3.x Support
------------------

There are currently two ways to get a Python 3 version of the library.

* Check out the main branch, and run `make python3` from the `tools/python` directory.  This will produce a new
  top-level `python3/` directory containing the Python 3 version of the library, as produced by
  [2to3](http://docs.python.org/2/library/2to3.html).
* Check out the (somewhat experimental) `python3` branch, which holds a unified version of the library that runs
  under both Python 2.x (x >= 5) and Python 3.x.

At some point the `python3` branch will probably become the main branch, but at the moment it sometimes lags behind the
main branch.  Please let me know if you're using the `python3` branch in anger, so that I can know to keep it more
up-to-date (and possibly accelerate the plans to make it the mainline version).
