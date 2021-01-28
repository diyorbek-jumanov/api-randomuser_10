import requests
import json

male_list = list()
female_list = list()
sum_male, sum_female = 0, 0

while sum_female <= 10 or sum_male <= 10:
    url = 'https://randomuser.me/api'
    r = requests.get(url)
    data = r.json()
    
