import csv, os

from constants import __CORRECT_HEADERS__

class File:
    def __init__(self, file):
        self.file = file
        self.to_check = True
        self.correct_structure = False
        self.is_pending = True
        self.name = self.extract_file_name()

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
    
    def compare_headers_lenght(self, headers_to_test):
        if len(headers_to_test) == len(__CORRECT_HEADERS__):
            return True
        else:
            return False

    def compare_headers(self, headers_to_test):
        headers_check = True
        for item in headers_to_test:
            if item in __CORRECT_HEADERS__:
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