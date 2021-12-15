from ftplib import FTP

from file import File
from datetime import datetime


# Classe s'occupant de l'enregistrement des host ftp
class Host:
    def __init__(self, type, host, repo, username, password):
        self.type = type
        self.url = host
        self.repo = repo
        self.username = username
        self.password = password


# Class regroupant des hosts FTP ainsi que le traitement des fichiers
class Server:
    def __init__(self, ftp_input: Host, ftp_output: Host):
        self.ftp_input = ftp_input
        self.ftp_input_connected = False
        self.ftp_output = ftp_output
        self.ftp_output_connected = False

    # Connection aux hosts FTP
    def connect(self):
        input_ftp = FTP(self.ftp_input.url)
        input_ftp.login(self.ftp_input.username, self.ftp_input.password)
        if input_ftp.getwelcome() == '220 83.166.138.115 FTP server ready':
            self.ftp_input_connected = True
        output_ftp = FTP(self.ftp_output.url)
        output_ftp.login(self.ftp_output.username, self.ftp_output.password)
        if output_ftp.getwelcome() == '220 83.166.138.115 FTP server ready':
            self.ftp_output_connected = True
        return [input_ftp, output_ftp]

    # Récupération des informations de connection
    def get_info(self):
        print('##### Input FTP #####')
        print('Server host: ', self.ftp_input.url)
        print('Server repository: ', self.ftp_input.repo)
        print('Server username: ', self.ftp_input.username)
        print('Server password: ', self.ftp_input.password)

        print('##### Output FTP #####')
        print('Server host: ', self.ftp_output.url)
        print('Server repository: ', self.ftp_output.repo)
        print('Server username: ', self.ftp_output.username)
        print('Server password: ', self.ftp_output.password)

    # Contrôle de la connection aux hosts FTP
    def check_connection(self):
        if (self.ftp_input_connected == True
                and self.ftp_output_connected == True):
            print('Connection aux serveurs FTP effectué avec succès')
            return True
        else:
            print('Problème avec la connection FTP')
            return False

    # Récupération des fichiers présent dans le directory mentionné
    def get_filenames(self, host: Host, directory):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(directory)
        filenames = ftp.nlst()
        ftp.close()
        return [filenames, len(filenames)]

    # Upload d'un fichier dans le host, directory mentionné avec traitement en cas de fichier déjà présent
    def upload_file(self, directory, host: Host, file: File):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        file_to_send = open(file.file, 'rb')
        ftp.cwd(directory)
        if self.check_file_present(host, file.name,
                                   directory) and host.type == 'input':
            print('Ce fichier "', file.name, '" est déjà présent sur',
                  host.url, ', annulation...')
        else:
            status = ftp.storlines('STOR ' + file.name, file_to_send)
            if status == '226 Transfer complete':
                print('Transfert du fichier"', file.name, '" effectué vers',
                      host.url)
            else:
                print(
                    "Une erreur est survenue lors de l'envoi du fichier vers ",
                    host.url)
            file_to_send.close()
            ftp.quit()

    # Contrôle de présence d'un fichier
    def check_file_present(self, host: Host, filename, directory):
        filenames = self.get_filenames(host, directory)[0]
        if filename in filenames:
            return True
        else:
            return False

    # Téléchargement d'un fichier sur la base d'un file_name
    def download_file(self, directory, host: Host, file_name):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(directory)
        if self.check_file_present(host, file_name, directory):
            file_to_download = open(file_name, 'wb')
            ftp.retrbinary('RETR %s' % file_name, file_to_download.write)
        else:
            print("Ce fichier n'est pas présent sur ftp", host.url)

    # Suppression d'un fichier
    def delete_file(self, directory, host: Host, file_name):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(directory)
        if self.check_file_present(host, file_name, directory):
            ftp.delete(directory + '/' + file_name)
            print(file_name, 'a été suprimée avec succès')
        else:
            print("Ce fichier n'est pas présent sur ftp", host.url)

    # Création d'un répertoire sur un host distant
    def create_directory(self, parent_directory, host: Host, directory_name):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(parent_directory)
        ftp.mkd(directory_name)

    # Récupération des dossiers présent sur un host distant
    def get_directories(self, parent_directory, host: Host):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(parent_directory)
        return ftp.nlst()

    # Contrôle de présence de certains dossiers obligatoires
    def check_directories(self):
        for host in [self.ftp_input, self.ftp_output]:
            if host.type == 'input':
                directories = self.get_directories('.', host)
                if 'Erreur' not in directories:
                    self.create_directory('.', host, 'Erreur')
                if 'Fichier traités' not in directories:
                    self.create_directory('.', host, 'Fichier traités')