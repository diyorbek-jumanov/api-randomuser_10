import requests
import json

male_list = list()
female_list = list()

paylod1 = {
    'results': 10,
    'gender': 'male'
}
url = 'https://randomuser.me/api'
r = requests.get(url, paylod1)
data1 = r.json()

for x in data1['results']:
    full_name = x['name']['first'] + " " + x['name']['last']
    male_list.append(full_name)

paylod2 = {
    'results': 10,
    'gender': 'female'
}
q = requests.get(url, paylod2)
data2 = q.json()

for x in data2['results']:
    full_name = x['name']['first'] + " " + x['name']['last']
    female_list.append(full_name)

