import csv

class File:
    def __init__(self, file):
        self.file = file
        self.to_check = True
        self.correct_structure = False

    def print_file(self):
        with open(self.file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                print(', '.join(row))
            
    def get_headers(self):
        headers = []
        with open(self.file, newline='') as csvfile:
            headers = next(csv.reader(csvfile, delimiter=';'))
        return headers                