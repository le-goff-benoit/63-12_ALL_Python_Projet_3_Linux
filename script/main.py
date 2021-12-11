import time
from constants import __CORRECT_HEADERS_WITH_TYPES__
from contact import Contact
from server import Host, Server
from mail import Mail
from file import File
import pathlib
from utils import autoconvert

# Host configuration
input_ftp_host = Host('input', 'd73kw.ftp.infomaniak.com',
                      'Cours/Projet3/Groupe1/Input', 'd73kw_projet3_groupe1_i',
                      '6zNr8c9TrHV4')
output_ftp_host = Host('output', 'd73kw.ftp.infomaniak.com',
                       'Cours/Projet3/Groupe1/Output',
                       'd73kw_projet3_groupe1_o', '84JN59cHQbvg')

# Server initialisation
server = Server(input_ftp_host, output_ftp_host)

# Add recipients
benoit = Contact('Benoît', 'blg@open-net.ch')
cosette = Contact('Cosette', 'cosette.bot@gmail.com')

# Server connection and check all is ok
server.connect()
server.check_connection()

# Add tests files
""" file1 = File('./test/Projet3_Group1_FichierValide.csv')
server.upload_file('.', input_ftp_host, file1) """

# Start of the listening loop (Exit from CTRL+C)
""" while True:
    if server.check_for_new_files():
        new_files = server.get_new_files()
        files_to_clean: list[File] = []
        for new_file in new_files:
            if new_file.compare_headers():
                files_to_clean.append(new_file)
            else:
                alert_mail = Mail()
                alert_mail.send_failed_message([benoit, cosette])
        for file_to_clean in files_to_clean:
            state = file_to_clean.clean()
            file_to_clean.set_daysum_tot()
            if state[0]:
                server.upload_file('.', output_ftp_host, file_to_clean)
                server.move_file('.', './OK/', input_ftp_host,
                                 file_to_clean.name)
                success_mail = Mail()
                success_mail.send_success_message([benoit, cosette], state[1])
            else:
                print('Un problème a eu lieu lors du nettoyage du fichier')
    time.sleep(60) """

while True:
    if server.get_filenames(input_ftp_host, '.')[1] > 3:
        files = server.get_filenames(input_ftp_host, '.')[0][2:]
        downloaded_files = []
        files_to_check: list[File] = []
        files_checked: list[File] = []
        for file in files:
            if pathlib.Path(file).suffix == '.csv':
                downloaded_files.append(file)
        if downloaded_files:
            for file in downloaded_files:
                server.download_file('.', input_ftp_host, file)
                file_to_add = File(file)
                files_to_check.append(file_to_add)
            for file in files_to_check:
                if file.compare_headers():
                    files_checked.append(file)
            print("Ces fichiers vont être traités :")
            for file in files_checked:
                for row in file.dict_read():
                    for cell in row:
                        row[cell] = autoconvert(row[cell])
                        print(cell, ':', row[cell], type(row[cell]))
        else:
            print("Aucun fichier n'est disponible pour téléchargement")
    else:
        print("Aucun fichier n'est disponible pour téléchargement")
    time.sleep(100)
