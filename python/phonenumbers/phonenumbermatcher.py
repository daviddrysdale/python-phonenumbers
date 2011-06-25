"""Functionality to match phone numbers in a piece of text"""

# Based on original Java code:
#     java/src/com/google/i18n/phonenumbers/PhoneNumberMatch.java
#     java/src/com/google/i18n/phonenumbers/PhoneNumberMatcher.java
#   Copyright (C) 2011 Google Inc.
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
import sys
import re

# Extra regexp function; see README
from re_util import fullmatch
import unicode_util
import phonenumberutil


def _limit(lower, upper):
    """Returns a regular expression quantifier with an upper and lower limit."""
    if ((lower < 0) or (upper <= 0) or (upper < lower)):
        raise Exception("Illegal argument to _limit")
    return u"{%d,%d}" % (lower, upper)

# Build the MATCHING_BRACKETS and PATTERN regular expression patterns. The
# building blocks below exist to make the patterns more easily understood.

_OPENING_PARENS = u"(\\[\uFF08\uFF3B"
_CLOSING_PARENS = u")\\]\uFF09\uFF3D"
_NON_PARENS = u"[^" + _OPENING_PARENS + _CLOSING_PARENS + u"]"
# Limit on the number of pairs of brackets in a phone number.
_BRACKET_PAIR_LIMIT = _limit(0, 3)

# Pattern to check that brackets match. Opening brackets should be closed
# within a phone number.  This also checks that there is something inside the
# brackets. Having no brackets at all is also fine.
#
# An opening bracket at the beginning may not be closed, but subsequent ones
# should be.  It's also possible that the leading bracket was dropped, so we
# shouldn't be surprised if we see a closing bracket first. We limit the sets
# of brackets in a phone number to four.
_MATCHING_BRACKETS = re.compile(u"(?:[" + _OPENING_PARENS + u"])?" + u"(?:" + _NON_PARENS + u"+" +
                                u"[" + _CLOSING_PARENS + u"])?" +
                                _NON_PARENS + u"+" +
                                u"(?:[" + _OPENING_PARENS + u"]" + _NON_PARENS +
                                u"+[" + _CLOSING_PARENS + u"])" + _BRACKET_PAIR_LIMIT +
                                _NON_PARENS + u"*")

# Limit on the number of leading (plus) characters.
_LEAD_LIMIT = _limit(0, 2)
# Limit on the number of consecutive punctuation characters.
_PUNCTUATION_LIMIT = _limit(0, 4)
# The maximum number of digits allowed in a digit-separated block. As we allow
# all digits in a single block, set high enough to accommodate the entire
# national number and the international country code.
_DIGIT_BLOCK_LIMIT = (phonenumberutil._MAX_LENGTH_FOR_NSN +
                      phonenumberutil._MAX_LENGTH_COUNTRY_CODE)
# Limit on the number of blocks separated by punctuation. Use _DIGIT_BLOCK_LIMIT
# since some formats use spaces to separate each digit.
_BLOCK_LIMIT = _limit(0, _DIGIT_BLOCK_LIMIT)

# A punctuation sequence allowing white space.
_PUNCTUATION = u"[" + phonenumberutil._VALID_PUNCTUATION + u"]" + _PUNCTUATION_LIMIT
# A digits block without punctuation.
_DIGIT_SEQUENCE = u"(?u)\\d" + _limit(1, _DIGIT_BLOCK_LIMIT)
# Punctuation that may be at the start of a phone number - brackets and plus signs.
_LEAD_CLASS = u"[" + _OPENING_PARENS + phonenumberutil._PLUS_CHARS + u"]"
_LEAD_PATTERN = re.compile(_LEAD_CLASS)

# Phone number pattern allowing optional punctuation.
# This is the phone number pattern used by _find(), similar to
# phonenumberutil._VALID_PHONE_NUMBER, but with the following differences:
# - All captures are limited in order to place an upper bound to the text
#   matched by the pattern.
# - Leading punctuation / plus signs are limited.
# - Consecutive occurrences of punctuation are limited.
# - Number of digits is limited.
# - No whitespace is allowed at the start or end.
# - No alpha digits (vanity numbers such as 1-800-SIX-FLAGS) are currently
#   supported.
_PATTERN = re.compile(u"(?:" + _LEAD_CLASS + _PUNCTUATION + u")" + _LEAD_LIMIT +
                      _DIGIT_SEQUENCE + u"(?:" + _PUNCTUATION + _DIGIT_SEQUENCE + u")" + _BLOCK_LIMIT +
                      u"(?:" + phonenumberutil._KNOWN_EXTN_PATTERNS + u")?",
                      phonenumberutil._REGEX_FLAGS)

# Matches strings that look like publication pages. Example: "Computing
# Complete Answers to Queries in the Presence of Limited Access Patterns.
# Chen Li. VLDB J. 12(3): 211-227 (2003)."
#
# The string "211-227 (2003)" is not a telephone number.
_PUB_PAGES = re.compile(u"\\d{1,5}-+\\d{1,5}\\s{0,4}\\(\\d{1,4}")

# Matches strings that look like dates using "/" as a separator. Examples:
# 3/10/2011, 31/10/96 or 08/31/95.
_SLASH_SEPARATED_DATES = re.compile(u"(?:(?:[0-3]?\\d/[01]?\\d)|(?:[01]?\\d/[0-3]?\\d))/(?:[12]\\d)?\\d{2}")


# Matches white-space, which may indicate the end of a phone number and the
# start of something else (such as a neighbouring zip-code).
_GROUP_SEPARATOR = re.compile(u"(?u)\\s+")  # Unicode Separator, \p{Z}


class Leniency(object):
    """Leniency when finding potential phone numbers in text segments"""
    # Phone numbers accepted are possible (i.e. is_possible_number(number)) but
    # not necessarily valid (is_valid_number(number)).
    POSSIBLE = 0

    # Phone numbers accepted are both possible (is_possible_number(number)) and
    # valid (is_valid_number(PhoneNumber)).
    VALID = 1


def _verify(leniency, numobj):
    """Returns True if number is a verified number according to the
    leniency."""
    if leniency == Leniency.POSSIBLE:
        return phonenumberutil.is_possible_number(numobj)
    elif leniency == Leniency.VALID:
        return phonenumberutil.is_valid_number(numobj)
    else:
        raise Exception("Error: unsupported Leniency value %s" % leniency)


class PhoneNumberMatcher(object):
    """A stateful class that finds and extracts telephone numbers from text.

    Vanity numbers (phone numbers using alphabetic digits such as '1-800-SIX-FLAGS' are
    not found.

    This class is not thread-safe.
    """
    # The potential states of a PhoneNumberMatcher.
    _NOT_READY = 0
    _READY = 1
    _DONE = 2

    def __init__(self, text, region,
                 leniency=Leniency.VALID, max_tries=sys.maxint):
        """Creates a new instance.

        Arguments:
        text -- The character sequence that we will search, None for no text.
        country -- The region that we are expecting the number to be from.
              This is only used if the number being parsed is not written in
              international format (with a leading plus, or with the
              international dialing prefix of the specified region). May be
              None or "ZZ" if only numbers with a leading plus should be
              considered.
        leniency -- The leniency to use when evaluating candidate phone
              numbers.
        max_tries -- The maximum number of invalid numbers to try before
              giving up on the text.  This is to cover degenerate cases where
              the text has a lot of false positives in it. Must be >= 0.
        """
        if leniency is None:
            raise ValueError("Need a leniency value")
        if int(max_tries) < 0:
            raise ValueError("Need max_tries to be positive int")
        # The text searched for phone numbers.
        self.text = text
        if self.text is None:
            self.text = u""
        # The region (country) to assume for phone numbers without an
        # international prefix, possibly None.
        self.preferred_region = region
        # The degree of validation requested.
        self.leniency = leniency
        # The maximum number of retries after matching an invalid number.
        self._max_tries = int(max_tries)
        # The iteration tristate.
        self._state = PhoneNumberMatcher._NOT_READY
        # The last successful match, None unless in state _READY
        self._last_match = None
        # The next index to start searching at. Undefined in state _DONE
        self._search_index = 0

    def has_next(self):
        """Indicates whether there is another match available"""
        if self._state == PhoneNumberMatcher._NOT_READY:
            self._last_match = self._find(self._search_index)
            if self._last_match is None:
                self._state = PhoneNumberMatcher._DONE
            else:
                self._search_index = self._last_match.end
                self._state = PhoneNumberMatcher._READY
        return (self._state == PhoneNumberMatcher._READY)

    def next(self):
        """Return the next match; raises Exception if no next match available"""
        # Check the state and find the next match as a side-effect if necessary.
        if not self.has_next():
            raise StopIteration("No next match")
        # Don't retain that memory any longer than necessary.
        result = self._last_match
        self._last_match = None
        self._state = PhoneNumberMatcher._NOT_READY
        return result

    def __iter__(self):
        while self.has_next():
            yield self.next()

    def _find(self, index):
        """Attempts to find the next subsequence in the searched sequence on or after index
        that represents a phone number. Returns the next match, None if none was found.

        Arguments:
        index -- The search index to start searching at.
        Returns the phone number match found, None if none can be found.
        """
        match = _PATTERN.search(self.text, index)
        while self._max_tries > 0 and match is not None:
            start = match.start()
            candidate = self.text[start:match.end()]

            # Check for extra numbers at the end.
            # TODO: This is the place to start when trying to support
            # extraction of multiple phone number from split notations (+41 79
            # 123 45 67 / 68).
            candidate = self._trim_after_first_match(phonenumberutil._SECOND_NUMBER_START_PATTERN,
                                                     candidate)

            match = self._extract_match(candidate, start)
            if match is not None:
                return match
            # Move along
            index = start + len(candidate)
            self._max_tries -= 1
            match = _PATTERN.search(self.text, index)
        return None

    def _trim_after_first_match(self, pattern, candidate):
        """Trims away any characters after the first match of pattern in
        candidate, returning the trimmed version."""
        trailing_chars_match = pattern.search(candidate)
        if trailing_chars_match:
            candidate = candidate[:trailing_chars_match.start()]
        return candidate

    @classmethod
    def _is_latin_letter(self, letter):
        """Helper method to determine if a character is a Latin-script letter
        or not. For our purposes, combining marks should also return true
        since we assume they have been added to a preceding Latin character."""
        # Combining marks are a subset of non-spacing-mark
        if (not unicode_util.is_letter(letter) and
            unicode_util.Category.get(letter) != unicode_util.Category.NON_SPACING_MARK):
            return False
        block = unicode_util.Block.get(letter)
        return (block == unicode_util.Block.BASIC_LATIN or
                block == unicode_util.Block.LATIN_1_SUPPLEMENT or
                block == unicode_util.Block.LATIN_EXTENDED_A or
                block == unicode_util.Block.LATIN_EXTENDED_ADDITIONAL or
                block == unicode_util.Block.LATIN_EXTENDED_B or
                block == unicode_util.Block.COMBINING_DIACRITICAL_MARKS)

    def _extract_match(self, candidate, offset):
        """Attempts to extract a match from a candidate string.

        Arguments:
        candidate -- The candidate text that might contain a phone number.
        offset -- The offset of candidate within self.text
        Returns the match found, None if none can be found
        """
        # Skip a match that is more likely a publication page reference or a
        # date.
        if (_PUB_PAGES.search(candidate) or
            _SLASH_SEPARATED_DATES.search(candidate)):
            return None

        # If leniency is set to VALID only, we also want to skip numbers that
        # are surrounded by Latin alphabetic characters, to skip cases like
        # abc8005001234 or 8005001234def.
        if self.leniency == Leniency.VALID:
            # If the candidate is not at the start of the text, and does not
            # start with punctuation and the previous character is not a Latin
            # letter, return None.
            if (offset > 0 and
                not _LEAD_PATTERN.match(candidate) and
                self._is_latin_letter(self.text[offset - 1])):
                return None
            last_char_index = offset + len(candidate)
            if (last_char_index < len(self.text) and
                self._is_latin_letter(self.text[last_char_index])):
                return None

        # Try to come up with a valid match given the entire candidate.
        match = self._parse_and_verify(candidate, offset)
        if match is not None:
            return match

        # If that failed, try to find an "inner match" -- there might be a
        # phone number within this candidate.
        return self._extract_inner_match(candidate, offset)

    def _extract_inner_match(self, candidate, offset):
        """Attempts to extract a match from candidate if the whole candidate
        does not qualify as a match.

        Arguments:
        candidate -- The candidate text that might contain a phone number
        offset -- The current offset of candidate within text
        Returns the match found, None if none can be found
        """
        # Try removing either the first or last "group" in the number and see
        # if this gives a result.  We consider white space to be a possible
        # indication of the start or end of the phone number.
        group_match = _GROUP_SEPARATOR.search(candidate)
        if group_match:
            group_start_index = group_match.end()
            # Remove the first group.
            without_first_group = candidate[group_start_index:]
            without_first_group = self._trim_after_first_match(phonenumberutil._UNWANTED_END_CHAR_PATTERN,
                                                               without_first_group)
            match = self._parse_and_verify(without_first_group, offset + group_start_index)
            if match is not None:
                return match
            self._max_tries -= 1

            if self._max_tries > 0:
                last_group_start = group_start_index
                group_match = _GROUP_SEPARATOR.search(candidate, last_group_start)
                while group_match:
                    # Find the last group.
                    last_group_start = group_match.start()
                    group_match = _GROUP_SEPARATOR.search(candidate, group_match.end())
                without_last_group = candidate[:last_group_start]
                without_last_group = self._trim_after_first_match(phonenumberutil._UNWANTED_END_CHAR_PATTERN,
                                                                  without_last_group)
                match = self._parse_and_verify(without_last_group, offset)
                if match is not None:
                    return match
                self._max_tries -= 1
        return None

    def _parse_and_verify(self, candidate, offset):
        """Parses a phone number from the candidate using phonenumberutil.parse and
        verifies it matches the requested leniency. If parsing and verification succeed, a
        corresponding PhoneNumberMatch is returned, otherwise this method returns None.

        Arguments:
        candidate -- The candidate match.
        offset -- The offset of candidate within self.text.
        Returns the parsed and validated phone number match, or None.
        """
        try:
            # Check the candidate doesn't contain any formatting which would
            # indicate that it really isn't a phone number.
            if not fullmatch(_MATCHING_BRACKETS, candidate):
                return None
            numobj = phonenumberutil.parse(candidate, self.preferred_region)
            if _verify(self.leniency, numobj):
                return PhoneNumberMatch(offset, candidate, numobj)
        except phonenumberutil.NumberParseException:
            # ignore and continue
            pass
        return None


class PhoneNumberMatch(object):
    """The immutable match of a phone number within a piece of text.

    Matches may be found using the find() method of PhoneNumberMatcher.

    A match consists of the phone number (in .number) as well as the .start
    and .end offsets of the corresponding subsequence of the searched
    text. Use .raw_string to obtain a copy of the matched subsequence.

    The following annotated example clarifies the relationship between the
    searched text, the match offsets, and the parsed number:

    >>> text = "Call me at +1 425 882-8080 for details."
    >>> country = "US"
    >>> import phonenumbers
    >>> matcher = phonenumbers.PhoneNumberMatcher(text, country)
    >>> matcher.has_next()
    True
    >>> m = matcher.next()  # Find the first phone number match
    >>> m.raw_string # contains the phone number as it appears in the text.
    "+1 425 882-8080"
    >>> (m.start, m.end)  # define the range of the matched subsequence.
    (11, 26)
    >>> text[m.start, m.end]
    "+1 425 882-8080"
    >>> phonenumberutil.parse("+1 425 882-8080", "US") == m.number
    True
    """
    def __init__(self, start, raw_string, numobj):
        if start < 0:
            raise Exception("Start index not >= 0")
        if raw_string is None or numobj is None:
            raise Exception("Invalid argument")
        # The start index into the text.
        self.start = start
        # The raw substring matched.
        self.raw_string = raw_string
        self.end = self.start + len(raw_string)
        # The matched phone number.
        self.number = numobj

    def __eq__(self, other):
        if not isinstance(other, PhoneNumberMatch):
            return False
        return (self.start == other.start and
                self.raw_string == other.raw_string and
                self.end == other.end and
                self.number == other.number)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return ("PhoneNumberMatch(start=%r, raw_string=%r, numobj=%r)" %
                (self.start,
                 self.raw_string,
                 self.number))

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"PhoneNumberMatch [%s,%s) %s" % (self.start, self.end, self.raw_string)
