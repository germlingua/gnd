import csv
import json

from abfrageGND import run_api_request
import pandas as pd
from extractGND import get_id_list, get_id_and_name
from filterAutorin import filter_authors, filter_conditions_for_authors
from filterYears import check_birthyear

data = pd.read_csv('data/pataky/cleaned-namelist-pataky-02.csv')
#names = data['Name']
names = data['Name Vorname']
#names = ["Bärwinkel Friedrich Konstantin", "Basel Richard"]
# res_api = run_api_request(names)
# print(res_api)

# with open('outputs/api_bruemmer.json', 'w') as json_file:
#     json.dump(res_api, json_file)
#
with open('outputs/api_pataky-2.json', 'r') as json_file:
    res_api = json.load(json_file)



#print(res_api[:10])
results_filter_year = check_birthyear(res_api)
#print("nach year filter", results_filter_year[:10])
results_filter_author = filter_authors(results_filter_year)
#print("nach author filter", results_filter_author[:10])
gnd_list = get_id_list(results_filter_author)
#print(gnd_list)
final_dict = get_id_and_name(gnd_list, names)
#print(final_dict)

with open('temp/pataky2-29-4-24.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)  # using tab ('\t') as the delimiter
    writer.writerow(['Name', 'GND'])
    for name, gnd in final_dict.items():
        writer.writerow([name] + ([gnd] if isinstance(gnd, str) else gnd))

## to push run git push germlingua master