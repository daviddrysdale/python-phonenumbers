"""PhoneNumber object definition"""

# Based on original Java code and protocol buffer:
#     resources/phonenumber.proto
#     java/src/com/google/i18n/phonenumbers/Phonenumber.java
#   Copyright (C) 2010-2011 The Libphonenumber Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .util import UnicodeMixin


class CountryCodeSource(object):
    """The source from which a country code is derived."""

    # The country_code is derived based on a phone number with a leading "+",
    # e.g. the French number "+33 (0)1 42 68 53 00".
    FROM_NUMBER_WITH_PLUS_SIGN = 1

    # The country_code is derived based on a phone number with a leading IDD,
    # e.g. the French number "011 33 (0)1 42 68 53 00", as it is dialled
    # from US.
    FROM_NUMBER_WITH_IDD = 5

    # The country_code is derived based on a phone number without a leading
    # "+", e.g. the French number "33 (0)1 42 68 53 00" when default_country is
    # supplied as France.
    FROM_NUMBER_WITHOUT_PLUS_SIGN = 10

    # The country_code is derived NOT based on the phone number itself, but
    # from the default_country parameter provided in the parsing function by
    # the clients. This happens mostly for numbers written in the national
    # format (without country code). For example, this would be set when
    # parsing the French number "(0)1 42 68 53 00", when default_country is
    # supplied as France.
    FROM_DEFAULT_COUNTRY = 20


class PhoneNumber(UnicodeMixin):
    """Class representing international telephone numbers.

    This class is hand-created based on phonenumber.proto. Please refer
    to that file for detailed descriptions of the meaning of each field.
    """

    def __init__(self,
                 country_code=None,
                 national_number=None,
                 extension=None,
                 italian_leading_zero=False,
                 raw_input=None,
                 country_code_source=None,
                 preferred_domestic_carrier_code=None):
        # The country calling code for this number, as defined by the
        # International Telecommunication Union (ITU). Fox example, this would
        # be 1 for NANPA countries, and 33 for France.
        #
        # None if not set, of type int otherwise.
        self.country_code = country_code  # None or int

        # National (significant) Number is defined in International
        # Telecommunication Union Recommendation E.164. It is a
        # language/country-neutral representation of a phone number at a
        # country level. For countries which have the concept of Area Code, the
        # National (significant) Number contains the area code. It contains a
        # maximum number of digits which equal to 15 - n, where n is the number
        # of digits of the country code. Take note that National (significant)
        # Number does not contain National(trunk) prefix.
        #
        # None if not set, of type long otherwise (and so it will never
        # contain any formatting (hypens, spaces, parentheses), nor any
        # alphanumeric spellings).
        self.national_number = national_number  # None or long

        # Extension is not standardized in ITU recommendations, except for
        # being defined as a series of numbers with a maximum length of 40
        # digits.
        #
        # When present, it is a Unicode string to accommodate for the
        # possible use of a leading zero in the extension (organizations
        # have complete freedom to do so, as there is no standard defined).
        # However, only ASCII digits should be stored here.
        self.extension = extension  # None or u'[0-9]+'

        # In some countries, the national (significant) number starts with
        # a "0" without this being a national prefix or trunk code of some
        # kind. For example, the leading zero in the national (significant)
        # number of an Italian phone number indicates the number is a
        # fixed-line number. There have been plans to migrate fixed-line
        # numbers to start with the digit two since December 2000, but it has
        # not happened yet. See http://en.wikipedia.org/wiki/%2B39 for more
        # details.
        #
        # This field can be safely ignored (there is no need to set it) for
        # most countries. Some limited amount of countries behave like Italy;
        # for these cases, if the leading zero of a number would be
        # retained even when dialling internationally, set this flag to true.
        #
        # Clients who use the parsing functionality of the phonenumbers
        # library will have this field set if necessary automatically.
        self.italian_leading_zero = italian_leading_zero  # bool

        # The next few fields are non-essential fields for a phone number.
        # They retain extra information about the form the phone number was
        # in when it was provided to us to parse. They can be safely
        # ignored by most clients.

        # This field is used to store the raw input string containing phone
        # numbers before it was canonicalized by the library. For example, it
        # could be used to store alphanumerical numbers such as
        # "1-800-GOOG-411".
        self.raw_input = raw_input  # None or Unicode string

        # The source from which the country_code is derived. This is not set
        # in the general parsing method, but in the method that parses and
        # keeps raw_input. New fields could be added upon request.
        self.country_code_source = country_code_source
        # None or CountryCodeSource.VALUE

        # The carrier selection code that is preferred when calling this
        # phone number domestically. This also includes codes that need to
        # be dialed in some countries when calling from landlines to mobiles
        # or vice versa. For example, in Columbia, a "3" needs to be dialed
        # before the phone number itself when calling from a mobile phone to
        # a domestic landline phone and vice versa.
        #
        # Note this is the "preferred" code, which means other codes may work
        # as well.
        self.preferred_domestic_carrier_code = preferred_domestic_carrier_code
        # None or Unicode string

    def clear(self):
        """Erase the contents of the object"""
        self.country_code = None
        self.national_number = None
        self.extension = None
        self.italian_leading_zero = False
        self.raw_input = None
        self.country_code_source = None
        self.preferred_domestic_carrier_code = None

    def merge_from(self, other):
        """Merge information from another PhoneNumber object into this one."""
        if other.country_code is not None:
            self.country_code = other.country_code
        if other.national_number is not None:
            self.national_number = other.national_number
        if other.extension is not None:
            self.extension = other.extension
        if other.italian_leading_zero is not None:
            self.italian_leading_zero = other.italian_leading_zero
        if other.raw_input is not None:
            self.raw_input = other.raw_input
        if other.country_code_source is not None:
            self.country_code_source = other.country_code_source
        if other.preferred_domestic_carrier_code is not None:
            self.preferred_domestic_carrier_code = other.preferred_domestic_carrier_code

    def __eq__(self, other):
        if not isinstance(other, PhoneNumber):
            return False
        return (self.country_code == other.country_code and
                self.national_number == other.national_number and
                self.extension == other.extension and
                self.italian_leading_zero == other.italian_leading_zero and
                self.raw_input == other.raw_input and
                self.country_code_source == other.country_code_source and
                self.preferred_domestic_carrier_code == other.preferred_domestic_carrier_code)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return (("PhoneNumber(country_code=%r, national_number=%r, extension=%r, " +
                 "italian_leading_zero=%r, country_code_source=%r, preferred_domestic_carrier_code=%r)") %
                (self.country_code,
                 self.national_number,
                 self.extension,
                 self.italian_leading_zero,
                 self.country_code_source,
                 self.preferred_domestic_carrier_code))

    def __unicode__(self):
        result = ("Country Code: %s National Number: %s" %
                  (self.country_code, self.national_number))
        if self.italian_leading_zero is not None:
            result += " Leading Zero: %s" % self.italian_leading_zero
        if self.extension is not None:
            result += " Extension: %s" % self.extension
        if self.country_code_source is not None:
            result += " Country Code Source: %s" % self.country_code_source
        if self.preferred_domestic_carrier_code is not None:
            result += (" Preferred Domestic Carrier Code: %s" %
                       self.preferred_domestic_carrier_code)
        return result


class FrozenPhoneNumber(PhoneNumber):
    """Immutable version of PhoneNumber"""
    _mutable = False

    def __hash__(self):
        return hash((self.country_code,
                     self.national_number,
                     self.extension,
                     self.italian_leading_zero,
                     self.raw_input,
                     self.country_code_source,
                     self.preferred_domestic_carrier_code))

    def __setattr__(self, name, value):
        if self._mutable or name == "_mutable":
            super(FrozenPhoneNumber, self).__setattr__(name, value)
        else:
            raise TypeError("Can't modify immutable instance")

    def __delattr__(self, name):
        if self._mutable:
            super(FrozenPhoneNumber, self).__delattr__(name)
        else:
            raise TypeError("Can't modify immutable instance")

    def __init__(self, *args, **kwargs):
        old_mutable = self._mutable
        self._mutable = True
        try:
            if len(kwargs) == 0 and len(args) == 1 and isinstance(args[0], PhoneNumber):
                super(FrozenPhoneNumber, self).__init__(**args[0].__dict__)
            else:
                super(FrozenPhoneNumber, self).__init__(*args, **kwargs)
        finally:
            self._mutable = old_mutable
