import java.util.Locale;
import java.util.HashMap;
/*
 * This class dumps relevant information from the java.util.Locale metadata into
 * a Python format.
 */


class DumpLocale {
  private static final char SINGLE_QUOTE = 39;
  private static final char[] hexChar = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};

  /* Print a Unicode name suitably escaped */
  private static void printName(String name) {
    System.out.print("u'");
    // Need to escape unicode data
    for (int ii=0; ii<name.length(); ii++) {
      char c = name.charAt(ii);
      if ((c >= 32) && (c < 127)) {
        if (c == SINGLE_QUOTE) {
          System.out.print("\\'");
        } else {
          System.out.print(c);
        }
      } else {
        // non-ASCII
        System.out.print("\\u");
        System.out.print(hexChar[(c >> 12) & 0xF]);
        System.out.print(hexChar[(c >> 8) & 0xF]);
        System.out.print(hexChar[(c >> 4) & 0xF]);
        System.out.print(hexChar[c & 0xF]);
      }
    }
    System.out.print("'");
  }

  public static void main(String[] args) {
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