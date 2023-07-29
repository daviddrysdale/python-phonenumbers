#!/usr/bin/env python
"""
Script for comparison with https://phonenumber.appspot.com
"""
import getopt
import phonenumbers
import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone
from phonenumbers import PhoneNumberFormat
import sys
import urllib.parse


def interactive_query():
    number = prompt("Specify a Phone Number: ")
    country = prompt_or_default("Specify a Default Country: ", None)
    locale = prompt_or_default("Specify a locale for phone number geocoding: ", "en")
    return (number, country, locale)


def prompt(msg):
    result = input(msg)
    return result.strip()


def prompt_or_default(msg, default):
    result = prompt(msg)
    if not result:
        return default
    else:
        return result


def blank_if_none(val):
    if val is None:
        return ""
    else:
        return val


class Table(object):
    def __init__(self, title):
        self.title = title
        self.lines = []
        self.longest_msg = 0

    def append(self, msg, val=None):
        if val is None:
            self.lines.append((msg,))
            return
        if len(msg) > self.longest_msg:
            self.longest_msg = len(msg)
        self.lines.append((msg, val))

    def render(self):
        print("")
        print("## %s" % self.title)
        for line in self.lines:
            if len(line) == 1:
                print(line[0])
            else:
                pad = ' ' * (self.longest_msg - len(line[0]))
                fmt = line[0] + pad + ": %s"
                print(fmt % line[1])


def appspot(number, country, locale):
    print("\n\nPhone Number entered: %s" % number)
    print("Default country entered: %s" % country)
    print("Language entered: %s" % locale)
    country = "ZZ" if country is None else country

    # Parse and analyse.  Compare with:
    # java/demo/src/main/java/com/google/phonenumbers/demo/render/ResultRenderer.java
    numobj = phonenumbers.parse(number, country, keep_raw_input=True)
    has_default_country = country != "" and country != "ZZ"

    is_possible_number = phonenumbers.is_possible_number(numobj)
    is_valid_number = phonenumbers.is_valid_number(numobj)
    if is_valid_number and has_default_country:
        is_valid_number_for_region = phonenumbers.is_valid_number_for_region(numobj, country)
    else:
        is_valid_number_for_region = None
    phone_number_region = phonenumbers.region_code_for_number(numobj)
    number_type = phonenumbers.number_type(numobj)
    validation_result = phonenumbers.is_possible_number_with_reason(numobj)

    is_possible_short_number = phonenumbers.is_possible_short_number(numobj)
    is_valid_short_number = phonenumbers.is_valid_short_number(numobj)
    if has_default_country:
        is_possible_short_number_for_region = phonenumbers.is_possible_short_number_for_region(numobj, country)
        is_valid_short_number_for_region = phonenumbers.is_valid_short_number_for_region(numobj, country)
    else:
        is_possible_short_number_for_region = None
        is_valid_short_number_for_region = None

    # Render. Compare with:
    # java/demo/src/main/resources/com/google/phonenumbers/demo/result.soy
    table = Table("Parsing result (parse(keep_raw_input=True))")
    table.append("country_code", blank_if_none(numobj.country_code))
    table.append("national_number", blank_if_none(numobj.national_number))
    table.append("extension", blank_if_none(numobj.extension))
    table.append("country_code_source", blank_if_none(phonenumbers.CountryCodeSource.to_string(numobj.country_code_source)))
    table.append("italian_leading_zero", blank_if_none(numobj.italian_leading_zero))
    table.append("number_of_leading_zeros", blank_if_none(numobj.number_of_leading_zeros))
    table.append("raw_input", blank_if_none(numobj.raw_input))
    table.append("preferred_domestic_carrier_code", blank_if_none(numobj.preferred_domestic_carrier_code))
    table.render()

    table = Table("Validation Results")
    table.append("Result from isPossibleNumber()", is_possible_number)
    if is_possible_number:
        if validation_result == phonenumbers.ValidationResult.IS_POSSIBLE_LOCAL_ONLY:
            table.append("Result from isPossibleNumberWithReason()", phonenumbers.ValidationResult.to_string(validation_result))
            table.append("Number is considered invalid as it is not a possible national number.")
        else:
            table.append("Result from isValidNumber()", is_valid_number)
            if is_valid_number_for_region is not None:
                table.append("Result from isValidNumberForRegion()", is_valid_number_for_region)
            table.append("Phone Number region", phone_number_region)
            table.append("Result from getNumberType()", phonenumbers.PhoneNumberType.to_string(number_type))
    else:
        table.append("Result from isPossibleNumberWithReason()", phonenumbers.ValidationResult.to_string(validation_result))
        table.append("Note: Numbers that are not possible have type UNKNOWN, an unknown region, and are considered invalid.")
    table.render()

    if not is_valid_number:
        table = Table("Short Number Results")
        table.append("Result from isPossibleShortNumber()", is_possible_short_number)
        if is_possible_short_number:
            table.append("Result from isValidShortNumber()", is_valid_short_number)
        if is_possible_short_number_for_region is not None:
            table.append("Result from isPossibleShortNumberForRegion()", is_possible_short_number_for_region)
            if is_valid_short_number_for_region is not None:
                table.append("Result from isValidShortNumberForRegion()", is_valid_short_number_for_region)
        table.render()

    table = Table("Formatting Results")
    table.append("E164 format", (phonenumbers.format_number(numobj, PhoneNumberFormat.E164) if is_valid_number else "invalid"))
    table.append("Original format", phonenumbers.format_in_original_format(numobj, phone_number_region))
    table.append("National format", phonenumbers.format_number(numobj, PhoneNumberFormat.NATIONAL))
    table.append("International format", (phonenumbers.format_number(numobj, PhoneNumberFormat.INTERNATIONAL) if is_valid_number else "invalid"))
    table.append("Out-of-country format from US", (phonenumbers.format_out_of_country_calling_number(numobj, "US") if is_valid_number else "invalid"))
    table.append("Out-of-country format from CH", (phonenumbers.format_out_of_country_calling_number(numobj, "CH") if is_valid_number else "invalid"))
    table.append("Format number for mobile dialing (calling from US)", (phonenumbers.format_number_for_mobile_dialing(numobj, "US", True) if is_valid_number else "invalid"))
    table.append("Format for national dialing with preferred carrier code", (phonenumbers.format_national_number_with_carrier_code(numobj, "") if is_valid_number else "invalid"))
    table.append("   and empty fallback carrier code")
    table.render()

    table = Table("AsYouTypeFormatter Results")
    formatter = phonenumbers.AsYouTypeFormatter(country)
    for i in range(len(number)):
        input_char = number[i]
        table.append("Char entered '%s' Output" % input_char, formatter.input_digit(input_char))
    table.render()

    if is_valid_number:
        table = Table("PhoneNumberOfflineGeocoder Results")
        table.append("Location", phonenumbers.geocoder.description_for_number(numobj, locale))
        table.render()

        table = Table("PhoneNumberToTimeZonesMapper Results")
        table.append("Time zone(s)", "[%s]" % ", ".join(phonenumbers.timezone.time_zones_for_number(numobj)))
        table.render()

        if (number_type == phonenumbers.PhoneNumberType.MOBILE or
            number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE or
            number_type == phonenumbers.PhoneNumberType.PAGER):
            table = Table("PhoneNumberToCarrierMapper Results")
            table.append("Carrier", phonenumbers.carrier.name_for_number(numobj, locale))
            table.render()

    print("\nPython library version: %s" % phonenumbers.__version__)
    print("\nCompare with: https://libphonenumber.appspot.com/phonenumberparser?number=%s&country=%s" % (urllib.parse.quote_plus(number), country))


def usage():
    print("./appspot.py [opts]")
    print("  --number <val>  / -n <val>  : number to parse")
    print("  --country <val> / -c <val>  : default country for parsing (default None)")
    print("  --locale <val>  / -l <val>  : language (default 'en')")
    print("  --help          / -h        : show this message")


if __name__ == '__main__':
    number = None
    country = None
    locale = "en"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:c:l:", ["help", "number=", "country=", "locale="])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-n", "--number"):
            number = a
        elif o in ("-c", "--country"):
            country = a
        elif o in ("-l", "--locale"):
            locale = a
        else:
            assert False, "unhandled option"
    if number is None:
        (number, country, locale) = interactive_query()
    appspot(number, country, locale)
