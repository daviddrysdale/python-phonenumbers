Version History
===============

Introduction
------------

This file holds summarized version history for code changes affecting the phonenumbers
library.

This file does not generally include descriptions of patch releases (vX.Y.Z
=> vX.Y.Z+1) unless there are significant changes to code, not just metadata
changes.  (Metadata updates are best checked
[upstream](https://github.com/google/libphonenumber/blob/master/release_notes.txt).)

What's new in 8.13.8
--------------------

Merge to
[upstream commit 07cd7bbb8a2f](https://github.com/google/libphonenumber/commit/07cd7bbb8a2f);
relevant code changes:

- Added a check to phonenumberutil.py that the value of the `phone-context` parameter of the tel URI follows the correct
  syntax as defined in [RFC3966](https://www.rfc-editor.org/rfc/rfc3966#section-3).

What's new in 8.13.0
--------------------

Merge to [upstream commit
185004cabd1bb4d3](https://github.com/google/libphonenumber/commit/185004cabd1bb4d3).  Upstream has
removed the `leading_zero_possible` field from the `PhoneMetadata` type as part of this version;
however, this change is *not* mirrored in the Python code due to back-compatibility concerns.

What's new in 8.12.40
---------------------

New `to_string()` methods have been added for enum-like classes, emitting strings that describe
integer values known to be enum values.

What's new in 8.12.32
---------------------

The library now includes `.pyi` stub files providing typing information about the API, thanks
to Adam Turner.

What's new in 8.12.24
---------------------

Merge to
[upstream commit e9d8d84f531b](https://github.com/google/libphonenumber/commit/e9d8d84f531b);
relevant code changes:

- Updated As-You-Type-Formatter to exclude patterns where some digits would be dropped in the output. This also
  fixes the bug where an extra country code is added in some cases to the user's output. b/183053929

What's new in 8.12.29
---------------------

Merge to
[upstream commit 8379f2f53bbe](https://github.com/google/libphonenumber/commit/8379f2f53bbe);
relevant code changes:

- Changes format_out_of_country_calling_number to always use preferred intl prefix if present, not just for numbers
  with a non-unique IDD. This means we will output "8~10" as the prefix if calling formatOutOfCountryCallingNumber
  instead of "810" for some regions that have this tilde in their prefix [designates that the user should wait before
  continuing to dial].

What's new in 8.12.0
---------------------

Merge to
[upstream commit fbfc3639d484](https://github.com/google/libphonenumber/commit/fbfc3639d484);
just metadata changes.

What's new in 8.11.0
---------------------

Merge to
[upstream commit ca195d5aff67](https://github.com/google/libphonenumber/commit/ca195d5aff67);
just metadata changes.

What's new in 8.10.8
---------------------

Merge to
[upstream commit aa1e7af6d637](https://github.com/google/libphonenumber/commit/aa1e7af6d637);
relevant code changes:

- Making the application of alternate formats when finding phone numbers in
  text in strict-grouping and exact-match mode depend on the leading digits
  for each rule. This was always assumed but never actually done. This means
  that the false positive rate will decrease but also that more valid numbers
  are skipped. A subsequent CL will update patterns to increase recall.

What's new in 8.10.3
---------------------

Merge to
[upstream commit 45953266d45d](https://github.com/google/libphonenumber/commit/45953266d45d);
relevant code changes:

- Better documentation for length_of_national_destination_code to emphasise that
  not every number has one.
- Removed unused code in the AsYouTypeFormatter: We no longer have numbers in
  formatting matching patterns, only \d.

What's new in 8.10.0
---------------------

Merge to
[upstream commit d62a8fb2b719](https://github.com/google/libphonenumber/commit/d62a8fb2b719);
relevant code changes:

- AsYouTypeFormatter changed to better choose between rules when dialling
  locally; previously we used the international rules when the national prefix
  was present since this would exclude the local-only rules. However, there are
  some numbers that are not internationally diallable that *do* use the
  national prefix, and this logic precluded formatting them correctly.

What's new in 8.9.12
--------------------

Merge to
[upstream commit d56bf9da349b](https://github.com/google/libphonenumber/commit/d56bf9da349b);
relevant code changes:

- Support Russian extension character "доб" as a valid one while parsing the numbers.

What's new in 8.9.0
-------------------

Just metadata changes.

What's new in 8.8.0
-------------------

Merge to
[upstream commit 7e4e754bda09](https://github.com/google/libphonenumber/commit/7e4e754bda09);
relevant code changes:

- Improve parsing logic to be smarter about national-prefix detection &
  stripping based on possible-lengths (`IS_POSSIBLE_LOCAL_ONLY` and
  `INVALID_LENGTH`). Enables e.g. adding Iran short-codes starting with "096"
  without the need to hack IR's national prefix parsing config.

What's new in 8.7.1
-------------------

Merge to
[upstream commit fb9aa53ecfa3](https://github.com/google/libphonenumber/commit/fb9aa53ecfa3);
relevant code changes:

- Documentation fix for `number_type`

What's new in 8.7.0
-------------------

Merge to
[upstream commit 1ad92eb35a44](https://github.com/google/libphonenumber/commit/1ad92eb35a44);
relevant code changes:

- New method `supported_calling_codes()` API to return all the calling codes
  that the library considers valid, both for geographical and non-geographical
  entities.
- Added `is_sms_service_for_region(numobj, region_dialing_from)` API in
  short number info library. An SMS service is where the primary or only
  intended usage is to receive and/or send text messages (SMSs). This includes
  MMS as MMS numbers downgrade to SMS if the other party isn't MMS-capable. The
  `is_sms_service` metadata is also serialized for the first time.
- Documentation update for private variables `_VALID_PUNCTUATION` and
  `_SINGLE_INTERNATIONAL_PREFIX`, also renaming the latter from
  `_UNIQUE_INTERNATIONAL_PREFIX`.

What's new in 8.6.0
-------------------

Merge to
[upstream commit 242a186f1fbf](https://github.com/google/libphonenumber/commit/242a186f1fbf);
relevant code changes:

- Removing `leading_zero_possible` from the metadata and all the places it is
  referenced in the build and prod code. Will be removed from the metadata
  proto itself in a subsequent release. This should not affect users of the
  library - the only place it was used was `format_in_original_format`, and only
  initially to try and avoid modifying the input number by removing/adding
  digits inadvertently. Now this is checked at the end of the method anyway.
  However slight formatting differences with this method on invalid numbers
  starting with 0s may be noticed in some countries.
- Updated the documentation for the `is_number_geographical` API.
- Small comment improvements for `parse()` method to point users at
  `keep_raw_input` parameter.
- Added a new enum for `CountryCodeSource` called `UNSPECIFIED`. This is used as a
  default value, and will be returned if someone calls `parse(keep_raw_input=False)` and then
  `.country_code_sourc` on the result. If users want an actual value for this
  then they should call `parse(keep_raw_input=True)` instead; the values that were
  previously returned after calling this method will not change.
- Deletion of the possible number pattern in the phonemetadata.proto file and
  all generated code. This has not been used for a long time.

What's new in 8.5.0
-------------------

Merge to
[upstream commit 52cff9d8837f](https://github.com/google/libphonenumber/commit/52cff9d8837f);
relevant code changes:

- Add `can_be_internationally_dialled` public API; This was already in JS.

What's new in 8.4.2
-------------------

Merge to
[upstream commit 9923d9211432](https://github.com/google/libphonenumber/commit/9923d9211432);
relevant code changes:

- Small fix for possible out-of-bounds exception on RFC3966 input where no
  phone context was actually provided.

What's new in 8.4.1
-------------------

Merge to
[upstream commit 02dbc0921cf5](https://github.com/google/libphonenumber/commit/02dbc0921cf5);
relevant code changes:

- Changing `is_possible_with_reason` to return the enums `INVALID_LENGTH` and
  `IS_POSSIBLE_LOCAL_ONLY`, where these apply. `is_possible_number` continues to
  consider `IS_POSSIBLE` or `IS_POSSIBLE_LOCAL_ONLY` numbers as possible to dial.
  Announcement: <https://groups.google.com/d/msg/libphonenumber-discuss/sPhYzdzFCmg/6tYsS1f6DgAJ>
- Doc updates for `region_code_for_number` to clarify that it does not
  work for short-codes or invalid numbers.

What's new in 8.4.0
-------------------

Merge to
[upstream commit 77affd08f65f](https://github.com/google/libphonenumber/commit/77affd08f65f);
relevant code changes:

- Doc changes to update references to ISO country codes to CLDR region codes,
  which are what we actually use. Notice in some of the mapper files the
  country code is still the ISO one, because it's used as part of a description
  of a language only (e.g. zh-TW vs zh-CN). Edited the language comments there
  since they can be two *or* three letters (c.f. fil for filipino). Also edited
  the comment for leadingDigits at the territory level in the
  `phonemetadata.proto` file.
- New API methods: `is_possible_number_for_type` and
  `is_possible_number_for_type_with_reason`, along with `supported_types_for_region` and
  `supported_types_for_non_geo_entity`. These allow you to query which types (e.g.
  Mobile) exist for a particular region, and work out if a number is possible
  for that type (this is a simple length check) rather than for the region as a
  whole.

What's new in 8.3.3
-------------------

Merge to
[upstream commit 46a38545ba01](https://github.com/google/libphonenumber/commit/46a38545ba01);
relevant code changes:

- Doc fix for `geocoder.py` to explain the cases where an empty string might be returned.

What's new in 8.3.2
-------------------

Metadata changes only.

What's new in 8.3.1
-------------------

Merge to
[upstream commit 5507fdbf623f](https://github.com/google/libphonenumber/commit/5507fdbf623f);
relevant code changes:

- Making `national_significant_number` more robust in the face of malicious
  input. This now ignores the `number_of_leading_zeros` if they are less than
  zero.

What's new in 8.3.0
-------------------

Merge to
[upstream commit ad297a10ba19](https://github.com/google/libphonenumber/commit/ad297a10ba19);
relevant code changes:

- Added two new enum values to `ValidationResult` - `IS_POSSIBLE_LOCAL_ONLY` and
  `INVALID_LENGTH`. Added more documentation to the existing values; see the
  docstrings for when these are going to be used. Note that the API for
  `is_possible_number_with_reason` has not yet been changed to return these values.
  `IS_POSSIBLE_LOCAL_ONLY` will be returned for some values which currently
  return `IS_POSSIBLE`, and `INVALID_LENGTH` will be returned for some values which
  currently return `TOO_LONG`.
- Fix for `is_number_match` to ignore the `number_of_leading_zeros` field when comparing
  numbers unless `italian_leading_zero` is `True`, and to consider default values
  to match the same value when explicitly set for these two fields. This fix
  shouldn't be needed for anyone correctly creating phone numbers using "parse"
  as recommended.

What's new in 8.2.0
-------------------

Merge to
[upstream commit 3b16d6b06497](https://github.com/google/libphonenumber/commit/3b16d6b06497);
relevant code changes:

- Exported `normalize_diallable_chars_only`. This method is already public in the C++
  implementation. It has also now been added to the Javascript implementation.

What's new in 8.1.0
-------------------

Merge to
[upstream commit c210dbca4e93](https://github.com/google/libphonenumber/commit/c210dbca4e93);
relevant code changes:

- Introduced new `is_carrier_specific_for_region` API in `shortnumberinfo`.
  This determines whether the provided short code is carrier-specific or
  not when dialed from the given region.

What's new in 8.0.0
-------------------

Merge to
[upstream commit 1eb06f31e1dd](https://github.com/google/libphonenumber/commit/1eb06f31e1dd);
relevant code changes:

- Removing the ability for `.._for_region` methods in `shortnumberinfo.py` to work
  on strings, as well of phone number objects. These have been marked deprecated
  for months. Any users of these methods should call `phonenumbers.parse` first to
  create a `PhoneNumber` object, and pass this in.
- Support semicolon as extension character while parsing phone numbers. This
  is not applicable when you are trying to find the phone numbers.

What's new in 7.7.5
-------------------

Merge to
[upstream commit e905483f87cf](https://github.com/google/libphonenumber/commit/e905483f87cf);
relevant code changes:

- Removing all references to `possible_number_pattern` other than in the metadata
  itself.

What's new in 7.7.4
-------------------

Merge to
[upstream commit fedbc7020703](https://github.com/google/libphonenumber/commit/fedbc7020703);
code changes:

- GitHub project changes:
    - Changed tag to `vX.Y.Z` from `release-X.Y.Z`; this may affect ports and derived projects.
- Metadata structure changes in XML file:
    - Mobile and Fixed-Line blocks are no longer assumed to inherit missing data
      from the GeneralDesc, but are treated like every other phone number type.
      This means that for the non-geographical country codes, like +800, the
      example number has been moved from generalDesc to the relevant number types,
      and the code in getExampleNumberForNonGeoEntity has been changed to look at
      these sub-types for an example number.
      This also means that the "NA" and "-1" blocks present in the metadata to
      indicate that no mobile or fixed-line numbers appear for the entity have been
      removed.
      There should no longer be an `exampleNumber` at the `generalDesc` level, but it
      should be present at every `PhoneNumberDesc` with data.
- Code changes:
    - Using new `possibleLengthInfo` to decide whether a short number is the right
      length or not. This could result in more specific results; whereas before, a
      number from length 3 to length 6 may have been deemed possible, now we may
      exclude a number of length 5.
    - Add hash (#) as a diallable character. Numbers with # in them will no longer
      have formatting applied in `format_n_original_format`, and
      `normalize_diallable_chars_only` now retains the # symbol.
    - `example_number_for_non_geo_entity` has been changed to look at the specific
      number types, not just the generalDesc, for the example numbers; this is a
      necessary change after the metadata structure change detailed above.

What's new in 7.7.3
-------------------

Merge to
[upstream commit ad0ce0c94501](https://github.com/google/libphonenumber/commit/ad0ce0c94501);
code changes:

- Fixed `phonemetadata.py` not to merge from a `NumberFormat`'s unset bool
  `national_prefix_optional_when_formatting`.

What's new in 7.7.2
-------------------

Merge to
[upstream commit 2d0d216f6032](https://github.com/google/libphonenumber/commit/2d0d216f6032);
code changes:

- Stop setting empty `preferred_domestic_carrier_code`, and if we are passed such
  a number then treat the empty field as if unset.

What's new in 7.7.1
-------------------

Merge to
[upstream commit 8c37310deb49](https://github.com/google/libphonenumber/commit/8c37310deb49);
code changes:

- Switching the internal implementation of `is_possible_number` and related functions
  to use the new `possibleLengths` metadata. This affects a lot of countries,
  making `is_possible_number` more restrictive as more precise data is available. It
  also affects parsing ambiguous and invalid numbers, as we decide whether
  to strip a possible national prefix (1) or country code based on the length
  of the number and whether it is possible before or after this.
- Formatting, naming and comment tweaks to follow style guide
- Removal of unneeded `_can_be_geocoded` method in the
  `timezone.py` file, using `phonenumberutil.py` instead

What's new in 7.7.0
-------------------

Merge to
[upstream commit 1ec4d341c3cd](https://github.com/google/libphonenumber/commit/1ec4d341c3cd);
no code changes that affect the Python version so this is just a version bump to
stay in sync with upstream.

What's new in 7.6.1
-------------------

Merge to [upstream commit 7cc500f588db](https://github.com/google/libphonenumber/commit/7cc500f588db); code changes:

- `phonemetadata.py` has two more fields to represent possible lengths of phone
  numbers. Changed `buildmetadatafromxml.py` to alter the way
  that metadata about possible-lengths information is consumed when constructing
  metadata to populate these.
  [Discussion list email](https://groups.google.com/forum/#!topic/libphonenumber-discuss/75TOpTFVi08)

What's new in 7.6.0
-------------------

Merge to [upstream commit ddf60b1c175e](https://github.com/google/libphonenumber/commit/ddf60b1c175e); code changes:

- Made `is_number_geographical()` public and added `is_number_type_geographical()`,
  and changed the geocoder to use this when checking whether to give a detailed
  answer or country-level only.

What's new in 7.5.0
-------------------

Merge to [upstream commit 3f83454ed62b](https://github.com/google/libphonenumber/commit/3f83454ed62b);
no code changes that affect the Python version so this is just a version bump to stay in sync with upstream.

What's new in 7.4.0
-------------------

Merge to [upstream commit 598b9a4f89d6](https://github.com/google/libphonenumber/commit/598b9a4f89d6);
no code changes that affect the Python version so this is just a version bump to stay in sync with upstream.

What's new in 7.3.0
-------------------

Merge to [upstream commit d933631fbf15](https://github.com/google/libphonenumber/commit/d933631fbf15); code changes:

- Added support for `region_code of None in example_number_for_type()`
- Added `invalid_example_number()`
- Improvements to docstring for parse method
- Update `is_number_geographical` to return true for geographical mobile numbers.

What's new in 7.2.0
-------------------

Merge to [upstream commit ab5e61acc087ec9f5](https://github.com/google/libphonenumber/commit/ab5e61acc087ec9f5), which
is 7.2.1 (7.2.0 had an immediate problem on release); upstream changelog mentions no code changes, but the Java
implementation includes a change to use nano protobufs.

What's new in 7.1.0
-------------------

Merge to [upstream commit 903ac5de5b6e1112](https://github.com/google/libphonenumber/commit/903ac5de5b6e1112);
upstream code changelog:

- Only upstream code change doesn't affect python version
  (New `MetadataSource` implementation that reads from a single metadata file with
  all regions' phone number metadata.)

What's new in 7.0.0
-------------------

Merge to upstream Subversion revision 715; upstream code changelog:

- New APIs for ShortNumberInfo. The old APIs have been deprecated and will be
  removed in an upcoming release.

What's new in 6.3.0
-------------------

Merge to upstream Subversion revision 703; upstream code changelog:

- Changing the offline geocoder to not return any country at all if the number
  could belong to multiple countries
- Removing obsolete code that treated countries with no metadata as valid.

What's new in 6.2.0
-------------------

Merge to upstream Subversion revision 674; upstream code changelog:

- Better exclusion of dates when matching phone numbers from text.
- Handle phone input in RFC3966 with missing tel: prefix

What's new in 6.1.0
-------------------

Merge to upstream Subversion revision 656; upstream code changelog:

- Adding MetadataLoader support to allow custom metadata loading from
  alternative sources (should have no visible impact to users).
- Fixing bug where digits could be lost in as-you-type formatting and
  formatting patterns incorrectly applied.

What's new in 6.0.0a
--------------------

Split geographic metadata into chunks.
Generate separate `phonenumbers-lite` package.
(No upstream changes.)

What's new in 6.0.0
-------------------

Removed beta status.
Merge up to upstream Subversion revision 650; upstream code changelog:

- Better support for detecting phone numbers in text that are beside each
  other
- Change to how Japanese numbers beginning with "00" are modelled, with the
  side-effect that the maximum possible number length has been extended by
  1.
- Handle `StringIndexOutOfBoundsException` in the `AsYouTypeFormatter` when the
  national prefix that was extracted was not found in the prefix. This
  affected countries with very long carrier codes, such as Korea.
- Removal of some of the author attributions - contributions to be tracked
  in CONTRIBUTORS file.

What's new in 5.9b1
-------------------

The codebase now supports Python 2.5-2.7 and Python 3.x out of the box, without
needing 2to3 conversion.

The top-level module no longer exports the following functions:

- `country_name_for_number`
- `description_for_number`
- `description_for_valid_number`

These functions now need to be imported via the `phonenumbers.geocoder` submodule.

The short number functions have been renamed:

- `is_possible_short_number_object` becomes `is_possible_short_number`
- `is_possible_short_number` becomes `is_possible_short_number_for_object`
- `is_valid_short_number_object` becomes `is_valid_short_number`
- `is_valid_short_number` becomes `is_valid_short_number_for_object`
- `expected_cost` becomes `expected_cost_for_region`, and there's a new `expected_cost`
  function that takes a `PhoneNumber` object.

Merge up to upstream Subversion revision 622; upstream code changelog:

- Adding support for numbers with multiple Italian leading zeros, by
  adding a field to the phone number proto to allow an arbitrary number of
  leading zeros, and supporting this when parsing, validating and
  formatting.
- Adding more functionality to `ShortNumberInfo` -> such as
  `GetExpectedCostForRegion`.
- Fix for parsing short numbers that start with the national prefix.
- Updating `FormatNumberForMobileDialing` to work with short numbers.
- Stop finding Israeli 4-digit "star" numbers in text when no star is in
  fact present.
- Bug fix for finding phone numbers where the area code was also part of
  the country calling code.

What's new in 5.8b1
-------------------

Rename `shortnumberutil.py` to `shortnumberinfo.py`.
Merge up to upstream Subversion revision 603; upstream code changelog:

- Renamed `ShortNumberUtil` to `ShortNumberInfo` -> the former class is now
  deprecated and will be deleted in a later release. At the moment it just
  delegates to `ShortNumberInfo`.
- New methods in the `ShortNumberInfo` API - `isCarrierSpecific`, singleton interface,
  `isPossibleShortNumber`, `isValidShortNumber`, `getShortNumberCost`. Note this
  is an experimental API at the moment and subject to change.
- Bug fixes:
    - AsYouTypeFormatting: 3-digit numbers can be formatted as a group
      where appropriate
    - AsYouTypeFormatting: Countries with an optional national prefix were
      considered before to have always entered it, resulting in bugs where
      numbers without the national prefix were not properly formatted.
    - Numbers in Chile that overlap with emergency numbers are no longer
      marked as connecting to them
    - Not requiring the NDC to be alone for countries where there is no
      national prefix in strict grouping when extracting phone numbers

What's new in 5.7b2
-------------------

Fix `setup.py` to include new `.shortdata` sub-package.

What's new in 5.7b1
-------------------

Merge up to upstream Subversion revision 594; upstream code changelog:

- Improve phone number extraction recall.
- Add support for loading short number metadata.

What's new in 5.6b1
-------------------

Merge up to upstream Subversion revision 579; upstream code changelog:

- Fix for as-you-type-formatting bug affecting countries with no national prefix
  formatting rule, such as China.

What's new in 5.5b1
-------------------

Merge up to upstream Subversion revision 574; upstream code changelog:

- Changed internal initialization code and made more fields final.
  Note that we now throw an exception if an attempt is made to set the
  metadata more than once (which should only happen during testing).
- Fix problem with `formatNumberForMobileDialing` for HU and CL.

What's new in 5.4b1
-------------------

Load metadata on demand rather than all at start of day.
Merge up to upstream Subversion revision 557; upstream code changelog:

- Switch `formatNumberForMobileDialing` to prefer national format to international format when the
  number is dialed from the same region the phone number is from.

What's new in 5.3b1
-------------------

Merge up to upstream Subversion revision 550; upstream code changelog:

- Handling UAN numbers in Argentina better when dialling them locally from a
  mobile

What's new in 5.2b1
-------------------

Merge up to upstream Subversion revision 532.

What's new in 5.1b1
-------------------

Merge up to upstream Subversion revision 516.

What's new in 5.0b2
-------------------

Merge up to upstream Subversion revision 500.
The upstream metadata at r489 didn't match the
generated Java code in 5.0; this upstream revision
fixed the mismatch.

What's new in 5.0b1
-------------------

Merge up to upstream Subversion revision 492.

What's new in 4.9b1
-------------------

Merge up to upstream Subversion revision 469.

What's new in 4.8b1
-------------------

Merge up to upstream Subversion revision 441.

What's new in 4.7b1
-------------------

Merge up to upstream Subversion revision 431.

What's new in 4.6b1
-------------------

Merge up to upstream Subversion revision 426.
Reinstated Python 2.5 support, accidentally broken since 4.3.

What's new in 4.5b1
-------------------

Merge up to upstream Subversion revision 419.

What's new in 4.4b1
-------------------

Merge up to upstream Subversion revision 411.

What's new in 4.3b1
-------------------

Merge up to upstream Subversion revision 396.
Adjust codebase to allow 2to3 generation of Python 3.x version.

What's new in 4.2b1
-------------------

Merge up to upstream Subversion revision 383.

What's new in 4.1b1
-------------------

Merge up to upstream Subversion revision 374.

What's new in 4.0b1
-------------------

Merge up to upstream Subversion revision 362.

What's new in 3.9b1
-------------------

Merge up to upstream Subversion revision 353.

What's new in 3.8b1
-------------------

Merge up to upstream Subversion revision 325.
Includes initial simplistic implementation of geocoding functionality.

What's new in 3.7b1
-------------------

Merge up to upstream Subversion revision 289 (but
geocoding functionality not yet ported).

What's new in 3.6b1
-------------------

Merge up to upstream Subversion revision 277 (but
geocoding functionality not yet ported).
Require Python 2.5, to allow import unicodedata.

What's new in 3.5b2
-------------------

Fix GH-3: crash in `parse()` for number with blank metadata

What's new in 3.5b1
-------------------

Merge up to upstream Subversion revision 213.

What's new in 3.4b1
-------------------

Merge up to upstream Subversion revision 205.
Changed version marker from a to b.
More unit test coverage

What's new in 3.3a1
-------------------

Merge up to upstream Subversion revision 190.

What's new in 3.2a1
-------------------

Merge up to upstream version 3.3, Subversion revision 171.

What's new in 3.1a1
-------------------

Initial port of libphonenumber, from <http://code.google.com/p/libphonenumber/>

This version based on upstream version 3.2, Subversion revision 166 of:
<http://libphonenumber.googlecode.com/svn/trunk/java>
