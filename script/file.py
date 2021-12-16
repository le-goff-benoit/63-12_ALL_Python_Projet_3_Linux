import os
import pandas
from pandas.core.frame import DataFrame
from constants import __CORRECT_HEADERS_WITH_TYPES__
from utils import is_a_date, is_a_time


# Class de traitement des fichiers locaux/distants
class File:
    def __init__(self, file):
        self.file = file
        self.name = self.extract_file_name()
        self.panda_frame = self.read()
        self.headers = self.get_header()

    # Extraction du nom : xxxxx.csv --> xxxxx
    def extract_file_name(self):
        return os.path.basename(self.file)

    # Comparaison des en-têtes avec les valeurs par défaut provenant de constants.py
    def compare_headers(self):
        header_check = True
        headers = self.get_header('brut')
        for item in headers:
            if item in __CORRECT_HEADERS_WITH_TYPES__.keys():
                pass
            else:
                header_check = False
                break

    # Lecture du fichier csv local/distant et transformation en pandas/dataframe
    def read(self):
        frame = pandas.read_csv(self.file, delimiter=';')
        return frame

    # Récupération des en-tête du fichier csv avec option "brut" pour éviter la déduplication de pandas
    def get_header(self, type=''):
        panda_columns = self.panda_frame.columns
        if type == 'brut':
            brut_columns = []
            for element in panda_columns:
                brut_columns.append(element.split('.')[0])
            return brut_columns
        else:
            return panda_columns

    # Nettoyage des éléments du headers pour éviter les xxx.1, xxx.2, xxx.3 de pandas, utilisé dans le cadre de traitement des daySum
    def purge_header_item(self, header):
        return header.split('.')[0]

    # Récupération des n headers daySum.n
    def get_all_daysum_header(self):
        panda_columns = self.panda_frame.columns
        daysum_columns = []
        for element in panda_columns:
            if element.split('.')[0] == 'DaySum':
                daysum_columns.append(element)
        return daysum_columns

    # Contrôle d'intégrité des lignes, un contrôle a uniquement été implémenté pour les deux premiers headers : #Date et Time
    def check_line(self, line, index):
        line_with_problems = []
        for header in self.get_header():
            if header == '#Date' and is_a_date(line['#Date']) == False:
                line_with_problems.append(index)
            elif header == 'Time' and is_a_time(line['Time']) == False:
                line_with_problems.append(index)
        return line_with_problems