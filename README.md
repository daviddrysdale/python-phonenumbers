phonenumbers Python Library
===========================

[![Coverage Status](https://coveralls.io/repos/daviddrysdale/python-phonenumbers/badge.svg?branch=dev&service=github)](https://coveralls.io/github/daviddrysdale/python-phonenumbers?branch=dev)

This is a Python port of [Google's libphonenumber library](https://github.com/google/libphonenumber)
It supports Python 2.5-2.7 and Python 3.x (in the same codebase, with no
[2to3](http://docs.python.org/2/library/2to3.html) conversion needed).

Original Java code is Copyright (C) 2009-2015 The Libphonenumber Authors.

Release [HISTORY](https://github.com/daviddrysdale/python-phonenumbers/blob/dev/python/HISTORY.md),
derived from [upstream release notes](https://github.com/google/libphonenumber/blob/master/release_notes.txt).

[Documentation](https://daviddrysdale.github.io/python-phonenumbers/)

Installation
------------

Install using [pip](https://pypi.org/project/phonenumbers/) with:
```
pip install phonenumbers
```

Example Usage
-------------

The main object that the library deals with is a `PhoneNumber` object.  You can create this from a string
representing a phone number using the `parse` function, but you also need to specify the country
that the phone number is being dialled from (unless the number is in E.164 format, which is globally
unique).

```pycon
>>> import phonenumbers
>>> x = phonenumbers.parse("+442083661177", None)
>>> print(x)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> type(x)
<class 'phonenumbers.phonenumber.PhoneNumber'>
>>> y = phonenumbers.parse("020 8366 1177", "GB")
>>> print(y)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> x == y
True
>>> z = phonenumbers.parse("00 1 650 253 2222", "GB")  # as dialled from GB, not a GB number
>>> print(z)
Country Code: 1 National Number: 6502532222 Leading Zero(s): False
```

The `PhoneNumber` object that `parse` produces typically still needs to be validated, to check whether
it's a *possible* number (e.g. it has the right number of digits) or a *valid* number (e.g. it's
in an assigned exchange).

```pycon
>>> z = phonenumbers.parse("+120012301", None)
>>> print(z)
Country Code: 1 National Number: 20012301 Leading Zero: False
>>> phonenumbers.is_possible_number(z)  # too few digits for USA
False
>>> phonenumbers.is_valid_number(z)
False
>>> z = phonenumbers.parse("+12001230101", None)
>>> print(z)
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
'020 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
'+44 20 8366 1177'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
'+442083661177'
```

If your application has a UI that allows the user to type in a phone number, it's nice to get the formatting
applied as the user types.   The `AsYouTypeFormatter` object allows this.

```pycon
>>> formatter = phonenumbers.AsYouTypeFormatter("US")
>>> formatter.input_digit("6")
'6'
>>> formatter.input_digit("5")
'65'
>>> formatter.input_digit("0")
'650'
>>> formatter.input_digit("2")
'650 2'
>>> formatter.input_digit("5")
'650 25'
>>> formatter.input_digit("3")
'650 253'
>>> formatter.input_digit("2")
'650-2532'
>>> formatter.input_digit("2")
'(650) 253-22'
>>> formatter.input_digit("2")
'(650) 253-222'
>>> formatter.input_digit("2")
'(650) 253-2222'
```

Sometimes, you've got a larger block of text that may or may not have some phone numbers inside it.  For this,
the `PhoneNumberMatcher` object provides the relevant functionality; you can iterate over it to retrieve a
sequence of `PhoneNumberMatch` objects.  Each of these match objects holds a `PhoneNumber` object together
with information about where the match occurred in the original string.

```pycon
>>> text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
>>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
...     print(match)
...
PhoneNumberMatch [11,23) 510-748-8230
PhoneNumberMatch [51,62) 703-4800500
>>> for match in phonenumbers.PhoneNumberMatcher(text, "US"):
...     print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
...
+15107488230
+17034800500
```

You might want to get some information about the location that corresponds to a phone number.  The
`geocoder.area_description_for_number` does this, when possible.

```pycon
>>> from phonenumbers import geocoder
>>> ch_number = phonenumbers.parse("0431234567", "CH")
>>> geocoder.description_for_number(ch_number, "de")
'Zürich'
>>> geocoder.description_for_number(ch_number, "en")
'Zurich'
>>> geocoder.description_for_number(ch_number, "fr")
'Zurich'
>>> geocoder.description_for_number(ch_number, "it")
'Zurigo'
```

For mobile numbers in some countries, you can also find out information about which carrier
originally owned a phone number.

```pycon
>>> from phonenumbers import carrier
>>> ro_number = phonenumbers.parse("+40721234567", "RO")
>>> carrier.name_for_number(ro_number, "en")
'Vodafone'
```

You might also be able to retrieve a list of time zone names that the number potentially
belongs to.

```pycon
>>> from phonenumbers import timezone
>>> gb_number = phonenumbers.parse("+447986123456", "GB")
>>> timezone.time_zones_for_number(gb_number)
('Atlantic/Reykjavik', 'Europe/London')
```

For more information about the other functionality available from the library, look in the unit tests or in the original
[libphonenumber project](https://github.com/google/libphonenumber).

Memory Usage
------------

The library includes a lot of metadata, potentially giving a significant memory overhead.  There are two mechanisms
for dealing with this.

* The normal metadata (just over 2 MiB of generated Python code) for the core functionality of the library is loaded
  on-demand, on a region-by-region basis (i.e. the metadata for a region is only loaded on the first time it is needed).
* Metadata for extended functionality is held in separate packages, which therefore need to be explicitly
  loaded separately.  This affects:
    * The geocoding metadata (~19 MiB), which is held in `phonenumbers.geocoder` and used by the geocoding functions
      (`geocoder.description_for_number`, `geocoder.description_for_valid_number` or
      `geocoder.country_name_for_number`).
    * The carrier metadata (~1 MiB), which is held in `phonenumbers.carrier` and used by the mapping functions
      (`carrier.name_for_number` or `carrier.name_for_valid_number`).
    * The timezone metadata (~100 KiB), which is held in `phonenumbers.timezone` and used by the timezone functions
      (`time_zones_for_number` or `time_zones_for_geographical_number`).

The `phonenumberslite` version of the library does not include the geocoder, carrier and timezone packages,
which can be useful if you have problems installing the main `phonenumbers` library due to space/memory limitations.

If you need to ensure that the metadata memory use is accounted for at start of day (i.e. that a subsequent on-demand
load of metadata will not cause a pause or memory exhaustion):

* Force-load the normal metadata by calling `phonenumbers.PhoneMetadata.load_all()`.
* Force-load the extended metadata by `import`ing the appropriate packages (`phonenumbers.geocoder`,
  `phonenumbers.carrier`, `phonenumbers.timezone`).

The `phonenumberslite` version of the package does not include the geocoding, carrier and timezone metadata,
which can be useful if you have problems installing the main `phonenumbers` package due to space/memory limitations.

Static Typing
-------------

The library includes a set of type [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files) to support static
type checking by library users. These stub files signal the types that should be used, and may also be of use in IDEs 
which have integrated type checking functionalities.

These files are written for Python 3, and as such type checking the library with these stubs on Python 2.5-2.7 is
unsupported.

Project Layout
--------------

* The `python/` directory holds the Python code.
* The `resources/` directory is a copy of the `resources/`
  directory from
  [libphonenumber](https://github.com/google/libphonenumber/tree/master/resources).
  This is not needed to run the Python code, but is needed when upstream
  changes to the master metadata need to be incorporated.
* The `tools/` directory holds the tools that are used to process upstream
  changes to the master metadata.
