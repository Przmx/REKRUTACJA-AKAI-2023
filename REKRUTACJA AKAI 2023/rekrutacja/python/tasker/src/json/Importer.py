import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r') as file:
            tasks_data = json.load(file)
        return tasks_data

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        tasks_data = self.read_tasks()
        return tasks_data