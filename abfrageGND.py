import pandas as pd
import requests

res_api = []
request_res_list = []
results_temp = []

data = pd.read_csv('data/pataky/cleaned-namelist-pataky-01.csv')

names = data['Name Vorname']
# only for Brümmer
# dateOfBirth = data['Geburtsdatum']

def autocomplete_search_test(query):
    url = "https://lobid.org/gnd/search"
    params = {
        'q': f'preferredName:{query} OR variantName:{query}',
        'format': 'json:preferredName,professionOrOccupation,gndSubjectCategory,dateOfBirth,periodOfActivity,gndIdentifier'
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
    res_api = autocomplete_search_test(names)
    # for item in names:
    #     res_api.append(autocomplete_search_test(item))
    return res_api
