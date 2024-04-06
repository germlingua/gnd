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

def extract_year_from_date(date_str):
    return int(date_str[-4:])



# gibt Liste der Treffer zurück, deren Geburtsjahr im spezifizierten Bereich liegt
def find_valid_birthyears(results):
    in_date_range = []
    if isinstance(results, list):
        for result in results:
            print(result)
            birth_year = extract_birth_year(result["label"])
            if birth_year is not None:
                if 1749 < birth_year < 1890:
                    print(result)
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





