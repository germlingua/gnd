import requests

res_api = []
request_res_list = []
results_temp = []


def api_request(query):
    url = "https://lobid.org/gnd/search"
    params = {
        'q': query,
        'format': 'json:preferredName,professionOrOccupation,dateOfBirth,periodOfActivity'
    }
    # params = {
    #     'q': query
    # }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None


def run_api_request(names):
    #res_api = api_request(names)
    for item in names:
        res_api.append(api_request(item))
    return res_api
