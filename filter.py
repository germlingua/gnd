import csv
import json
from abfrageGND import run_api_request
import pandas as pd
from extractGND import get_id_list, get_id_and_name
from filterAutorin import filter_authors, filter_conditions_for_authors
from filterYears import check_birthyear

data = pd.read_csv('data/pataky/cleaned-namelist-pataky-01.csv')
names = data['Name Vorname']

#res_api = run_api_request(names)

# with open('outputs/api_bruemmer.json', 'w') as json_file:
#     json.dump(res_api, json_file)
#
with open('outputs/api_pataky-1.json', 'r') as json_file:
    res_api = json.load(json_file)

#print(res_api)
results_filter_year = check_birthyear(res_api)
#print("nach year filter", results_filter_year)
results_filter_author = filter_authors(results_filter_year)
#print("nach author filter", results_filter_author)
gnd_list = get_id_list(results_filter_author)
#print(gnd_list)
final_dict = get_id_and_name(gnd_list, names)
#print(final_dict)

with open('outputs/pataky-gnd-01-23-03-2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')  # using tab ('\t') as the delimiter
    writer.writerow(['Name', 'GND'])
    for name, gnd in final_dict.items():
        writer.writerow([name] + ([gnd] if isinstance(gnd, str) else gnd))

