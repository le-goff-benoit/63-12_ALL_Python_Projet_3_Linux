from ftplib import FTP

class Host :
    def __init__(self, type, host, repo, username, password):
        self.type = type
        self.url = host
        self.repo = repo
        self.username = username
        self.password = password

class Server:
    def __init__(self, ftp_input:Host, ftp_output:Host):
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
        if (self.ftp_input_connected == True and self.ftp_output_connected == True):
            print('Connections to FTP servers successfull')
            return True
        else:
            print('Problem with connection to FTP servers')
            return False

    def waiting_for_input_file(self):
        print("Ecrire une méthode qui attend qui wait une action sur le serveurr")
    