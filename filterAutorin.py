# nach Autor:innen filtern

autorin_results = []


def filter_conditions_for_authors(inner_list_api, possible_results):

    if isinstance(inner_list_api, list):
        for entry in inner_list_api:
            print(entry)
            if ("Autorin" in entry['label'] or
                    "Autor" in entry['label'] or
                    "Schriftstellerin" in entry['label'] or
                    "Schriftsteller" in entry['label']):
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
            autorin_results.append("kein Treffer gefunden")
    return autorin_results
