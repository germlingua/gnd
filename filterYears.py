from abfrageGND import res_api
from abfrageGND import request_res_list
from abfrageGND import results_temp

# Variable, die pro Eintrag entweder eine leere Liste, eine GND-Nummer (String) oder eine Liste mit Dictionaries enthält

# print(results_temp)


# extracts the year from the list of birthdates
# only Brümmer!
def extract_year_from_date(date_str):
    return int(date_str[-4:])


# Funktion, die die gnd von der url aus dem api Datensatz extrahiert
def extract_id_from_url(url):
    # Extracts the number after the last '/'
    return url.rsplit('/', 1)[-1]


# #### only Brümmer
# def find_id_from_results(results, dob):
#     for result in results:
#         birth_year = extract_birth_year(result["label"])
#         if birth_year is not None:
#             if dob != ".":
#                 dob_year = extract_year_from_date(dob)
#                 if birth_year == int(dob_year) and 1770 < birth_year < 1870:
#                     return extract_id_from_url(result["id"])
#     return None


def extract_year_from_date(date_str):
    return int(date_str[-4:])


# ### pataky only weil wir kein geb datum zum abgleichen haben -> "birth-date" bezieht sich entweder auf geburtsjahr
# oder wirkungsjahr (von api Abfrage)
# gibt Liste der Treffer zurück, deren Geburtsjahr im spezifizierten Bereich liegt
def find_valid_birthyears(results):
    in_date_range = []
    if isinstance(results, list):
        for result in results:
            print(result)
            birth_year = extract_birth_year(result["label"])
            if birth_year is not None:
                if 1770 < birth_year < 1970:
                    in_date_range.append(result)
    return in_date_range


# Funktion, die aus dem api Datensatz das Datum, wenn vorhanden, herausfiltert
# erkennt 1900-01-01 und 1900
def extract_birth_year(label):
    try:
        for part in label.split('|'):
            cleaned_part = part.strip()
            # Check for the format "1800-05-12"
            if len(cleaned_part) == 10 and cleaned_part[4] == '-' and cleaned_part[7] == '-':
                year_part = cleaned_part[:4]
                if year_part.isdigit():
                    return int(year_part)
            # Check for the format "1800"
            elif cleaned_part.isdigit() and len(cleaned_part) == 4:
                return int(cleaned_part)

        # Return None if no valid format is found
        return None
    except TypeError as te:
        print(f"Error extracting birth year: {te}")
        return None


# führt den Abgleich der Jahreszahlen durch
# ruft Hilfsfunktionen zum Abgleich und zum Extrahieren der Jahreszahlen
# gibt Liste zurück mit
def check_birthyear(temp_results):
    year_results = []
    for entry in temp_results:

        # print(f"Checking results for {name}:")
        if not entry:
            year_results.append("kein Eintrag von api gefunden")
        # if gnd already found in previous step
        elif isinstance(entry, str):
            year_results.append(entry)
        # wenn mehrere Treffer in Eintrag
        elif isinstance(entry, list):
            in_date_range = find_valid_birthyears(entry)
            # wenn ein Eintrag mit passendem Jahr gefunden wurde, dann diesen zurückgeben
            if in_date_range:
                year_results.append(in_date_range)
            # wenn kein Eintrag mit passendem Jahr gefunden wurde -> vollständigen Eintrag zurückgeben
            else:
                year_results.append(entry)
    return year_results




