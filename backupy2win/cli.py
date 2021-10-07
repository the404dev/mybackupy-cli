from getpass import getpass
from colors import Color
from art import text2art
from backup import Backup


class Cli:
    def __init__(self):
        print(Color.INFO + text2art('backupy2win') + Color.RESET)
        self.start_cli()

    def start_cli(self):
        print('---------------------------------')
        print('BEM VINDO AO UTILITÁRO DE BACKUP')
        print('---------------------------------\n')
        self.init_menu()

    def init_menu(self):
        self.create_backup_folder()
    
    def create_backup_folder(self):
        print('Digite ou cole o endereço do diretorio para realizar o backup: ')
        self.source_dir = input()
        print(Color.INFO + self.source_dir + Color.RESET)
        print('Digite ou cole o diretório de destino do backup: ')
        self.destination_dir = input()
        print(Color.INFO + self.source_dir + Color.RESET)
        self.insert_password()
        print('Digite um nome para o backup: ')
        self.name_backup = input()
        Backup.compress_backup('folder', self.name_backup, self.source_dir, self.name_backup, self.destination_dir, self.password)

    def insert_password(self):
        while True:
            print('Digite a senha para backup - Pressione Enter para deixar em branco')
            self.password = getpass()
            if self.password == '':
                self.password = None
                return self.password
            print('Digite novamente a senha para backup')
            self.repeat_password = getpass()
            if self.password != self.repeat_password:
                print('Senhas não conferem!')
            else:
                return self.password
                break
        
        