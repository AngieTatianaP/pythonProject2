import random

import hum
import pres
import temp
import json

cities = ([])
def create_list():
    path = 'data/cities.json'
    with open(path) as file:
        data = json.load(file)
    for city in data['cities']:
        name = city['name']
        cities.append(name)

def sensors_init():
    while(True):
        ciudad = random.choice(cities)
        print(ciudad)
        temp.run(ciudad)
        hum.run(ciudad)
        pres.run(ciudad)

if __name__ == '__main__':
    create_list()
    sensors_init()