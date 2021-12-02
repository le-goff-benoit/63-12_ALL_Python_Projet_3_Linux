import time
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

while True:
    print(server.get_filenames(input_ftp_host, '.')[1], 'fichiers sont présent sur', input_ftp_host.url)
    time.sleep(10)