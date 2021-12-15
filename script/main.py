import time
import pandas
from constants import __CORRECT_HEADERS_WITH_TYPES__
from contact import Contact
from server import Host, Server
from file import File
import pathlib
from mail import Mail

# Configuration des deux hosts
input_ftp_host = Host('input', 'd73kw.ftp.infomaniak.com',
                      'Cours/Projet3/Groupe1/Input', 'd73kw_projet3_groupe1_i',
                      '6zNr8c9TrHV4')
output_ftp_host = Host('output', 'd73kw.ftp.infomaniak.com',
                       'Cours/Projet3/Groupe1/Output',
                       'd73kw_projet3_groupe1_o', '84JN59cHQbvg')

# Initialisation du serveur
server = Server(input_ftp_host, output_ftp_host)

# Création de contact
benoit = Contact('Benoît', 'blg@open-net.ch')
christophe = Contact('Christophe', 'christophe.loureiro@students.hevs.ch')

# Connection au serveur et check (connection + présence des dossier de traitement de fichiers)
server.connect()
server.check_connection()
server.check_directories()

# Pandas configuration
pandas.set_option('display.max_rows', None)
print(server.get_filenames(output_ftp_host, '.'))

file = File('Projet3_Group1_FichierNonValide.csv')
server.upload_file('.', input_ftp_host, file)

# Event loop
while True:
    if server.get_filenames(input_ftp_host, '.')[1] >= 3:
        files = server.get_filenames(input_ftp_host, '.')[0][2:]

        # Initialisation des tableaux de traitement de fichiers
        files_to_download = []
        files_to_check: list[File] = []
        files_checked: list[File] = []

        # Récupération des fichiers csv uniquement
        for file in files:
            if pathlib.Path(file).suffix == '.csv':
                files_to_download.append(file)

        # Téléchargement des fichiers
        if files_to_download:
            print(
                "Ces fichiers sont disponibles sur le FTP et vont être téléchargés: ",
                files_to_download)
            for file in files_to_download:
                server.download_file('.', input_ftp_host, file)
                file_to_add = File(file)
                files_to_check.append(file_to_add)

            # Check des headers du fichier par comparaison
            if files_to_check:
                for file in files_to_check:
                    if True:
                        files_checked.append(file)
                    else:
                        # Déplacement du fichier problématique vers un dossier Erreur
                        server.delete_file('.', input_ftp_host, file)
                        server.upload_file('Erreur', input_ftp_host, file)
                        # Envoi d'un email d'avertissement
                        mail = Mail(file)
                        mail.send_failed_message([benoit])

                # Nettoyage des lignes du fichier
                if files_checked:
                    print("Ces fichiers sont prêt à être traité/nettoyé",
                          files_checked)
                    for file in files_checked:
                        problem_lines = []
                        for i, row in file.panda_frame.iterrows():
                            if file.check_line(row, i):
                                problem_lines += file.check_line(row, i)

                        # En cas de problème sur des lignes
                        if problem_lines:
                            print(
                                "Ces lignes vont être supprimée dans le fichier:",
                                file.name, ':', problem_lines)
                            # Suppression des lignes errones
                            file.panda_frame = file.panda_frame.drop(
                                index=problem_lines)
                        # Ajout de la colonne de somme DaySumTot
                        print("Modification du fichier pour ajouter DaySumTot")
                        file.panda_frame['DaySumTot'] = file.panda_frame[
                            file.get_all_daysum_header()].sum(axis=1)

                        # Déplacement du fichier traité dans un dossier "Fichier déplacés"
                        server.delete_file('.', input_ftp_host, file.name)
                        server.upload_file('Fichier traités', input_ftp_host,
                                           file)

                        # Upload du fichier traité dans le output ftp
                        server.upload_file('.', output_ftp_host, file)

                        # Envoi de l'email de réussite
                        mail = Mail(file)
                        mail.send_success_message([benoit], len(problem_lines))
        else:
            print(
                "Aucun fichier n'est disponible pour téléchargement, nouvel essai dans 15 secondes, CTRL+C pour quitter"
            )
    else:
        print(
            "Aucun fichier n'est disponible pour téléchargement, nouvel essai dans 15 secondes, CTRL+C pour quitter"
        )

    # Temps d'attente avec nouvelle tentative
    time.sleep(15)