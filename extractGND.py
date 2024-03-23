def extract_id(entry):
    if isinstance(entry, str):
        return entry
    elif isinstance(entry, list):
        if len(entry) == 1 and isinstance(entry[0], str):
            return entry[0]
        elif len(entry) == 1 and isinstance(entry[0], dict):
            return entry[0]['id'].split('/')[-1]
        elif all(isinstance(item, dict) for item in entry):
            return [item['id'] for item in entry]
    return None


def get_id_list(data):
    gnd_list = []
    for entry in data:
        gnd_list.append(extract_id(entry))
    return gnd_list


def get_id_and_name(gnd_list, names):
    name_gnd = {}
    for entry, name in zip(gnd_list, names):
        name_gnd[name] = entry
    return name_gnd



