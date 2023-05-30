import json

from service_reservation.models import resto



def insert_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            restaurant = resto(name=item['name'], description=item['description'])
            restaurant.save()


file_path = '/home/daour/Sonatel_academy_P5/projet_django/donnees_restos.json'
insert_data_from_json(file_path)
