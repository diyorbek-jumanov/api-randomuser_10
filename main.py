import requests
import json

male_list = list()
female_list = list()
sum_male, sum_female = 0, 0

while sum_female <= 10 or sum_male <= 10:
    url = 'https://randomuser.me/api'
    r = requests.get(url)
    data = r.json()
    if r.status_code == 200:
        name = data['results'][0]['name']
        full_name = name['last'] + ' ' + name['first']
        gender = data['results'][0]['gender']

        if gender == 'male' and sum_male <= 10:
            male_data = {
                'fullName': full_name
            }
            male_list.append(male_data)
            sum_male += 1

        if gender == 'female' and sum_female <= 10:
            female_data = {
                'fullName': full_name
            }
            female_list.append(female_data)
            sum_female += 1

full_list = [
    male_list,
    female_list
]

f = open("data.json", "w")
f.write(json.dumps(full_list, indent=4))
f.close()
