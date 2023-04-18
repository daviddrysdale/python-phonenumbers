#!/usr/bin/env python
"""
Script for comparison with https://phonenumber.appspot.com
"""
import phonenumbers
import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone
from phonenumbers import PhoneNumberFormat
import urllib.parse

def main():
    number = prompt("Specify a Phone Number: ")
    country = prompt_or_default("Specify a Default Country: ", None)
    locale = prompt_or_default("Specify a locale for phone number geocoding: ", "en")
    appspot(number, country, locale)

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

def appspot(number, country, locale):
    print("\n\nPhone Number entered: %s" % number)
    print("Default country entered: %s" % country)
    print("Language entered: %s" % locale)
    country = "ZZ" if country is None else country

    numobj = phonenumbers.parse(number, country, keep_raw_input=True)
    print("\nParsing result (parse(keep_raw_input=True))")
    print("country_code                   : %s" % blank_if_none(numobj.country_code))
    print("national_number                : %s" % blank_if_none(numobj.national_number))
    print("extension                      : %s" % blank_if_none(numobj.extension))
    print("country_code_source            : %s" % blank_if_none(phonenumbers.CountryCodeSource.to_string(numobj.country_code_source)))
    print("italian_leading_zero           : %s" % blank_if_none(numobj.italian_leading_zero))
    print("number_of_leading_zeros        : %s" % blank_if_none(numobj.number_of_leading_zeros))
    print("raw_input                      : %s" % blank_if_none(numobj.raw_input))
    print("preferred_domestic_carrier_code: %s" % blank_if_none(numobj.preferred_domestic_carrier_code))

    valid = phonenumbers.is_valid_number(numobj)
    print("\nValidation Results")
    print("Result from isPossibleNumber()      : %s" % phonenumbers.is_possible_number(numobj))
    print("Result from isValidNumber()         : %s" % valid)
    if valid and country != "ZZ":
        print("Result from isValidNumberForRegion(): %s" % phonenumbers.is_valid_number_for_region(numobj, country))
    print("Phone Number region                 : %s" % phonenumbers.region_code_for_number(numobj))
    print("Result from getNumberType()         : %s" % phonenumbers.PhoneNumberType.to_string(phonenumbers.number_type(numobj)))


    print("\nFormatting Results")
    print("E164 format                                            : %s" % (phonenumbers.format_number(numobj, PhoneNumberFormat.E164) if valid else "invalid"))
    print("Original format                                        : %s" % phonenumbers.format_in_original_format(numobj, country))
    print("National format                                        : %s" % phonenumbers.format_number(numobj, PhoneNumberFormat.NATIONAL))
    print("International format                                   : %s" % (phonenumbers.format_number(numobj, PhoneNumberFormat.INTERNATIONAL) if valid else "invalid"))
    print("Out-of-country format from US                          : %s" % (phonenumbers.format_out_of_country_calling_number(numobj, "US") if valid else "invalid"))
    print("Out-of-country format from CH                          : %s" % (phonenumbers.format_out_of_country_calling_number(numobj, "CH") if valid else "invalid"))
    print("Format number for mobile dialing (calling from US)     : %s" % (phonenumbers.format_number_for_mobile_dialing(numobj, "US", True) if valid else "invalid"))
    print("Format for national dialing with preferred carrier code: %s" % (phonenumbers.format_national_number_with_carrier_code(numobj, "") if valid else "invalid"))
    print("   and empty fallback carrier code")


    print("\nAsYouTypeFormatter Results")
    formatter = phonenumbers.AsYouTypeFormatter(country)
    for i in range(len(number)):
        input_char = number[i]
        print("Char entered '%s' Output: %s" % (input_char, formatter.input_digit(input_char)))

    if valid:
        print("\nPhoneNumberOfflineGeocoder Results")
        print("Location: %s" % phonenumbers.geocoder.description_for_number(numobj, locale))

        print("\nPhoneNumberToTimeZonesMapper Results")
        print("Time zone(s): [%s]" % ", ".join(phonenumbers.timezone.time_zones_for_number(numobj)))

        print("\nPhoneNumberToCarrierMapper Results")
        print("Carrier: %s" % phonenumbers.carrier.name_for_number(numobj, locale))

    print("\nPython library version: %s" % phonenumbers.__version__)
    print("\nCompare with: https://libphonenumber.appspot.com/phonenumberparser?number=%s&country=%s" % (urllib.parse.quote_plus(number), country))

if __name__ == '__main__':
    main()
