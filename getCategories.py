import requests

def getCategories(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the 'id' field from each object in the 'member' array
        ids = [member['id'] for member in data.get('member', [])]

    else:
        print("Error:", response.status_code)
    return ids

categories = {
    'schriftstellerin': 'https://lobid.org/gnd/search?q=broaderTermGeneral.id%3A"https://d-nb.info/gnd/4053311-6"',
    'schriftsteller': 'https://lobid.org/gnd/search?q=broaderTermGeneral.id%3A"https://d-nb.info/gnd/4053309-8"',
    'autorin': 'https://lobid.org/gnd/search?q=broaderTermGeneric.id%3A"https://d-nb.info/gnd/4258697-5"',
    'autor': 'https://lobid.org/gnd/search?q=broaderTermGeneric.id%3A"https://d-nb.info/gnd/4003982-1"'
}

# for category in categories:
#     sub = getCategories(categories[category])

# length: 39 (keine doppelungen)

# TODO: Liste abgleichen mit Janas Liste
links = [
    "https://d-nb.info/gnd/7628949-7",
    "https://d-nb.info/gnd/4798808-3",
    "https://d-nb.info/gnd/4509449-4",
    "https://d-nb.info/gnd/7624358-8",
    "https://d-nb.info/gnd/7693197-3",
    "https://d-nb.info/gnd/4683584-2",
    "https://d-nb.info/gnd/4643578-5",
    "https://d-nb.info/gnd/4178446-7",
    "https://d-nb.info/gnd/4618865-4",
    "https://d-nb.info/gnd/4997034-3",
    "https://d-nb.info/gnd/4391928-5",
    "https://d-nb.info/gnd/4182594-9",
    "https://d-nb.info/gnd/4480046-0",
    "https://d-nb.info/gnd/7587036-8",
    "https://d-nb.info/gnd/7624356-4",
    "https://d-nb.info/gnd/4168391-2",
    "https://d-nb.info/gnd/4651476-4",
    "https://d-nb.info/gnd/4398215-3",
    "https://d-nb.info/gnd/4124076-5",
    "https://d-nb.info/gnd/4201653-8",
    "https://d-nb.info/gnd/4692295-7",
    "https://d-nb.info/gnd/1274269121",
    "https://d-nb.info/gnd/1041695977",
    "https://d-nb.info/gnd/7567940-1",
    "https://d-nb.info/gnd/7637197-9",
    "https://d-nb.info/gnd/1088451845",
    "https://d-nb.info/gnd/1098063473",
    "https://d-nb.info/gnd/7693202-3",
    "https://d-nb.info/gnd/4053311-6",
    "https://d-nb.info/gnd/1059558653",
    "https://d-nb.info/gnd/4053309-8",
    "https://d-nb.info/gnd/1098063139",
    "https://d-nb.info/gnd/4359312-4",
    "https://d-nb.info/gnd/4157321-3",
    "https://d-nb.info/gnd/7693201-1",
    "https://d-nb.info/gnd/4294338-3",
    "https://d-nb.info/gnd/4303304-0",
    "https://d-nb.info/gnd/4145403-0",
    "https://d-nb.info/gnd/4670833-9"
]

# https://d-nb.info/gnd/7628949-7
# https://d-nb.info/gnd/4798808-3
# https://d-nb.info/gnd/4509449-4
# https://d-nb.info/gnd/7624358-8
# https://d-nb.info/gnd/7693197-3
# https://d-nb.info/gnd/4683584-2
# https://d-nb.info/gnd/4643578-5
# https://d-nb.info/gnd/4178446-7
# https://d-nb.info/gnd/4618865-4
# https://d-nb.info/gnd/4997034-3
# https://d-nb.info/gnd/4391928-5
# https://d-nb.info/gnd/4182594-9
# https://d-nb.info/gnd/4480046-0
# https://d-nb.info/gnd/7587036-8
# https://d-nb.info/gnd/7624356-4
# https://d-nb.info/gnd/4168391-2
# https://d-nb.info/gnd/4651476-4
# https://d-nb.info/gnd/4398215-3
# https://d-nb.info/gnd/4124076-5
# https://d-nb.info/gnd/4201653-8
# https://d-nb.info/gnd/4692295-7
# https://d-nb.info/gnd/1274269121
# https://d-nb.info/gnd/1041695977
# https://d-nb.info/gnd/7567940-1
# https://d-nb.info/gnd/7637197-9
# https://d-nb.info/gnd/1088451845
# https://d-nb.info/gnd/1098063473
# https://d-nb.info/gnd/7693202-3
# https://d-nb.info/gnd/4053311-6
# https://d-nb.info/gnd/1059558653
# https://d-nb.info/gnd/4053309-8
# https://d-nb.info/gnd/1098063139
# https://d-nb.info/gnd/4359312-4
# https://d-nb.info/gnd/4157321-3
# https://d-nb.info/gnd/7693201-1
# https://d-nb.info/gnd/4294338-3
# https://d-nb.info/gnd/4303304-0
# https://d-nb.info/gnd/4145403-0
# https://d-nb.info/gnd/4670833-9