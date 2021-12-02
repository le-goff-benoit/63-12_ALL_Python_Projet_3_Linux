from file import File
from constants import __CORRECT_HEADERS__
from contact import Contact
from server import Host, Server

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

correct_file = File('./test/Projet3_Group1_FichierValide_test.csv' )
server.upload_file('.', input_ftp_host, correct_file)

print(server.get_filenames(input_ftp_host, '.'))
server.download_file('.', input_ftp_host, 'Projet3_Group1_FichierValide_test23.csv')

#mail = Mail(correct_file)
#mail.send_success_message([benoit, cosette])
#mail.send_failed_message([cosette])