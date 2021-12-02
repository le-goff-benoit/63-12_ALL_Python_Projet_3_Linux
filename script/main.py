import time
from constants import __CORRECT_HEADERS__
from contact import Contact
from server import Host, Server
from mail import Mail
from file import File

# Host configuration
input_ftp_host = Host('input', 'd73kw.ftp.infomaniak.com', 'Cours/Projet3/Groupe1/Input', 'd73kw_projet3_groupe1_i', '6zNr8c9TrHV4' )
output_ftp_host = Host('output', 'd73kw.ftp.infomaniak.com', 'Cours/Projet3/Groupe1/Output', 'd73kw_projet3_groupe1_o', '84JN59cHQbvg')

# Server initialisation
server = Server(input_ftp_host, output_ftp_host)

# Add recipients
benoit = Contact('Benoît', 'blg@open-net.ch')
cosette = Contact('Cosette', 'cosette.bot@gmail.com')

# Server connection and check all is ok
server.connect()
server.check_connection()

# Start of the listening loop (Exit from CTRL+C)
while True:
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
                server.move_file('.', './OK/', input_ftp_host, file_to_clean.name )
                success_mail = Mail()
                success_mail.send_success_message([benoit, cosette], state[1])
            else:
                print('Un problème a eu lieu lors du nettoyage du fichier')
    time.sleep(60)