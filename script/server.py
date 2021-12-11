from ftplib import FTP

from file import File


class Host:
    def __init__(self, type, host, repo, username, password):
        self.type = type
        self.url = host
        self.repo = repo
        self.username = username
        self.password = password


class Server:
    def __init__(self, ftp_input: Host, ftp_output: Host):
        self.ftp_input = ftp_input
        self.ftp_input_connected = False
        self.ftp_output = ftp_output
        self.ftp_output_connected = False

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

    def check_connection(self):
        if (self.ftp_input_connected == True
                and self.ftp_output_connected == True):
            print('Connections to FTP servers successfull')
            return True
        else:
            print('Problem with connection to FTP servers')
            return False

    def waiting_for_input_file(self):
        print(
            "Ecrire une méthode qui attend qui wait une action sur le serveurr"
        )

    def get_filenames(self, host: Host, directory):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(directory)
        filenames = ftp.nlst()
        ftp.close()
        return [filenames, len(filenames)]

    def upload_file(self, directory, host: Host, file: File):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        file_to_send = open(file.file, 'rb')
        ftp.cwd(directory)
        if self.check_file_present(host, file.name, directory):
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

    def check_file_present(self, host: Host, filename, directory):
        filenames = self.get_filenames(host, directory)[0]
        if filename in filenames:
            return True
        else:
            return False

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

    def create_directory(self, parent_directory, host: Host, directory_name):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(parent_directory)
        ftp.mkd(directory_name)

    def get_directories(self, parent_directory, host: Host):
        if host.type == 'input':
            ftp = self.connect()[0]
        if host.type == 'output':
            ftp = self.connect()[1]
        ftp.cwd(parent_directory)
        return ftp.dir()
