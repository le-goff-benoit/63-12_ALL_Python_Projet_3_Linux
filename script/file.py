import csv

from constants import CORRECT_HEADERS

class File:
    def __init__(self, file):
        self.file = file
        self.to_check = True
        self.correct_structure = False
        self.is_pending = True

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
    
    def compare_headers_lenght(self, headers_to_test):
        if len(headers_to_test) == len(CORRECT_HEADERS):
            return True
        else:
            return False

    def compare_headers(self, headers_to_test):
        headers_check = True
        for item in headers_to_test:
            if item in CORRECT_HEADERS:
                pass
            else:
                headers_check = False
                break
        return headers_check
    
    def global_check(self, headers_to_test):
        if self.compare_headers_lenght(headers_to_test) and self.compare_headers(headers_to_test):
            return True
        else:
            return False