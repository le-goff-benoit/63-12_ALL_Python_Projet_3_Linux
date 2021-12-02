import csv, os

from constants import __CORRECT_HEADERS__

class File:
    def __init__(self, file):
        self.file = file
        self.to_check = True
        self.correct_structure = False
        self.is_pending = True
        self.name = self.extract_file_name()
        self.headers = self.get_headers()

    def extract_file_name(self):
        return os.path.basename(self.file)

    def read(self, file):
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            return reader
    
    def get_headers(self):
        with open(self.file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                for column in row:
                    headers = column.split(';')
                break
        return headers

    def compare_headers (self):
        list_dif = [i for i in self.headers + __CORRECT_HEADERS__ if i not in self.headers or i not in __CORRECT_HEADERS__]
        if not list_dif:
            return True
        else:
            return False