import java.util.Locale;
import java.util.HashMap;
/*
 * This class dumps relevant information from the java.util.Locale metadata into
 * a Python format.
 */


class DumpLocale {
  private static final char SINGLE_QUOTE = 39;
  private static final char BACKSLASH = 92;
  private static final char[] hexChar = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};

  /* Print a Unicode name suitably escaped */
  private static void printName(String name) {
    // Need to escape Unicode data if we find it.
    boolean seenUnicode = false;
    StringBuilder sb = new StringBuilder();
    for (int ii=0; ii<name.length(); ii++) {
      char c = name.charAt(ii);
      if ((c >= 32) && (c < 127)) {
        if (c == SINGLE_QUOTE) {
          sb.append("\\'");
        } else if (c == BACKSLASH) {
          sb.append("\\\\");
        } else {
          sb.append(c);
        }
      } else {
        // Non-ASCII.  Assume nothing outside of the BMP
        seenUnicode = true;
        sb.append("\\u");
        sb.append(hexChar[(c >> 12) & 0xF]);
        sb.append(hexChar[(c >> 8) & 0xF]);
        sb.append(hexChar[(c >> 4) & 0xF]);
        sb.append(hexChar[c & 0xF]);
      }
    }
    if (seenUnicode) {
      System.out.print("u('");
      System.out.print(sb.toString());
      System.out.print("')");
    } else {
      System.out.print("'");
      System.out.print(sb.toString());
      System.out.print("'");
    }
  }

  private static void printProperty(String propName) {
    String propVal = System.getProperty(propName, null);
    if (propVal != null) {
      System.out.println("  " + propName + "=" + propVal);
    }
  }

  private static void printProlog() {
    System.out.println("\"\"\"Locale information.");
    System.out.println("Holds a map from ISO 3166-1 country code (e.g. GB) to a dict.");
    System.out.println("Each dict maps from an ISO 639-1 language code (e.g. ja) to the country's name in that language.");
    System.out.println("");
    System.out.println("Generated from java.util.Locale, generation info:");
    printProperty("java.version");
    printProperty("java.vendor");
    printProperty("os.name");
    printProperty("os.arch");
    printProperty("os.version");
    System.out.println("");
    System.out.println("Auto-generated file, do not edit by hand.");
    System.out.println("\"\"\"");
    System.out.println("from ..util import u");
  }

  public static void main(String[] args) {
    // Check for mode
    printProlog();
    System.out.println("LOCALE_DATA = {");
    String[] all_countries = Locale.getISOCountries();
    String[] all_langs = Locale.getISOLanguages();
    // Name => first language code that maps to that name
    HashMap<String, String> name_to_lang = new HashMap<String, String>();
    for (String country: all_countries) {
      System.out.print("  '"+country+"': {");
      Locale country_locale = new Locale("", country);
      for (String lang: all_langs) {
        Locale lang_locale = new Locale(lang);
        String country_in_lang = country_locale.getDisplayCountry(lang_locale);
        if ((country_in_lang != null) && (country_in_lang.length() != 0)) {
          String previous_lang = name_to_lang.get(country_in_lang);
          if (previous_lang != null) {
            // Already seen this name before.  Print the name as "*<otherlang>"
            // on the assumption that this will save a lot of space (about 30%)
            System.out.print("'"+lang+"':");
            System.out.print("'*"+previous_lang+"'");
            System.out.print(",");
          } else {
            // First time we've seen this name
            name_to_lang.put(country_in_lang, lang);
            System.out.print("'"+lang+"':");
            printName(country_in_lang);
            System.out.print(",");
          }
        }
      }
      System.out.println("},");
    }
    System.out.println("}");
  }
}