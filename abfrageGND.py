
import requests

res_api = []
request_res_list = []
results_temp = []


def autocomplete_search_test(query):
    url = "https://lobid.org/gnd/search"
    params = {
        'q': query,
        'format': 'json:preferredName,professionOrOccupation,gndSubjectCategory,dateOfBirth,'
                  'periodOfActivity'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None


def run_api_request(names):
    #res_api = autocomplete_search_test(names)
    for item in names:
        res_api.append(autocomplete_search_test(item))
    return res_api
