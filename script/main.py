from file import File
from constants import __CORRECT_HEADERS__
from mail import Mail
from server import Host, Server

# Host configuration
input_ftp_host = Host('input', 'd73kw.ftp.infomaniak.com', 'Cours/Projet3/Groupe1/Input', 'd73kw_projet3_groupe1_i', '6zNr8c9TrHV4' )
output_ftp_host = Host('output', 'd73kw.ftp.infomaniak.com', 'Cours/Projet3/Groupe1/Output', 'd73kw_projet3_groupe1_o', '84JN59cHQbvg')

# Server initialisation
server = Server(input_ftp_host, output_ftp_host)

# Server connection and check all is ok
server.connect()
server.check_connection()

correct_file = File('./test/Projet3_Group1_FichierValide.csv')
print(correct_file.global_check(__CORRECT_HEADERS__))

mail = Mail()
mail.send('blg@open-net.ch', 'salut')