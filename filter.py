from abfrageGND import run_api_request
import pandas as pd
from filterAutorin import filter_authors, filter_conditions_for_authors
from filterYears import check_birthyear

data = pd.read_csv('data/pataky/cleaned-namelist-pataky-01.csv')
names = data['Name Vorname']
# only for Brümmer
# dateOfBirth = data['Geburtsdatum']
#res_api = run_api_request(names[:10])
res_api = [[{'label': 'Adler, Helene | Schriftstellerin | 1894-12-20 | 1282819828',
             'id': 'https://d-nb.info/gnd/1282819828', 'category': 'Individualisierte Person'},
            {'label': 'Adler, Helene | Schriftstellerin | 1649 | 11646853X', 'id': 'https://d-nb.info/gnd/11646853X',
             'category': 'Individualisierte Person'},
            {'label': 'Adler, Helene | Komikerin | 1849 | 11646853X', 'id': 'https://d-nb.info/gnd/11646853X',
             'category': 'Individualisierte Person'}],
           [],
           [{'label': 'Adler, Helena | Schriftstellerin | 1594-12-20 | 1282819828',
             'id': 'https://d-nb.info/gnd/1282819828', 'category': 'Individualisierte Person'},
            ]
           ]

# print(res_api)
# results_filter_year = check_birthyear(res_api)
# print("nach year filter", results_filter_year)
# results_filter_author = filter_authors(results_filter_year)
# print("nach author filter", results_filter_author)

results_filter_author = filter_authors(res_api)
print("nach author filter", results_filter_author)
results_filter_year = check_birthyear(results_filter_author)
print("nach year filter", results_filter_year)