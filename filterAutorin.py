# nach Autor:innen filtern

autorin_results = []


# TODO: Filter so umbauen, dass er überprüft, ob an zweiter Stelle
#  (nach dem ersten |) überhaupt Text steht
#  wenn das nicht der Fall ist (wenn also keine Berufsbezeichnung erfasst ist)
#  dann den Eintrag mit aufnehmen
#  wenn eine Berufsbezeichnung erfasst ist, überprüfen, ob Autor:in etc.
#  wenn ja -> aufnehmen, wenn nein -> wegschmeißen
def filter_conditions_for_authors(inner_list_api, possible_results):
    if isinstance(inner_list_api, list):
        for entry in inner_list_api:
            label = entry['label']
            subsegments = [segment.strip() for segment in label.split('|')]
            # check if the second entry (if there is) is a year -> means that no profession is listed
            if len(subsegments) >= 2:
                second_entry = subsegments[1]
                contains_numeric = any(char.isdigit() for char in second_entry)
                if contains_numeric:
                    possible_results.append(entry)
                else:
                    if ("Autorin" in subsegments[1] or
                            "Autor" in subsegments[1] or
                            "Schriftstellerin" in subsegments[1] or
                            "Schriftsteller" in subsegments[1]):
                        possible_results.append(entry)
            # Fall, wenn nur der Name der Person bekannt ist
            # Eintrag wird auch zurückgegeben zur Überprüfung
            else:
                possible_results.append(entry)
    elif isinstance(inner_list_api, str):
        possible_results.append(inner_list_api)


def filter_authors(api_results):
    for inner_list_api in api_results:
        possible_results = []
        filter_conditions_for_authors(inner_list_api, possible_results)
        if possible_results:
            autorin_results.append(possible_results)
        else:
            autorin_results.append("im Untersuchungszeitraum, aber Beruf eindeutig nicht als \"Autor:in\" gelabeled")
            #print("kein Treffer im Zusammenhang mit Autorin gefunden", inner_list_api)
    return autorin_results
