from csv import DictReader

class File:
    def __init__(self, file):
        self.file = file
        self.to_check = True
        self.correct_structure = False

    def print_file(self):
        with open(self.file, newline='') as csvfile:
            csv = DictReader(csvfile)
            for row in csv:
                print(row)
            
    def get_headers(self):
        headers = []
        with open(self.file, newline='') as csvfile:
            headers = next(csv.reader(csvfile, delimiter=';'))
        return headers
    
    def get_inv_header(self):
        inv_headers = []
        with open(self.file, newline='') as csvfile:
            inv_headers = next(csv.reader(csvfile, delimiter=';'))
            return inv_headers.split('INV')