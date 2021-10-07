from art import text2art
from backup import Backup
from colorama import Fore, Style
from getpass import getpass
import colorama


class Cli:
    def __init__(self):
        colorama.init(autoreset=True)
        print(Fore.GREEN + text2art('backupy2win'))
        self.start_cli()

    def start_cli(self):
        print(Fore.BLUE + '''
 -----------------------------------------------
| BEM VINDO AO UTILITÁRO DE BACKUP PARA WINDOWS |
 -----------------------------------------------\n''')
        while True:
            print(Fore.WHITE + '''
 -------------------
| ESCOLHA UMA OPÇÃO |
 -------------------
            ''')
            print(Fore.YELLOW + '''
 -----------------
| 1) FAZER BACKUP |
 -----------------
 ---------------------
| 2) RESTAURAR BACKUP |
 ---------------------
            ''')
            input()

    
    def create_backup_folder(self):
        print(Fore.YELLOW + '''
 -----------------------------
| COMPRIMIR ARQUIVO DE BACKUP |
 -----------------------------\n''')
        print('Digite ou cole o endereço do diretorio para realizar o backup: ')
        self.source_dir = input(Fore.BLUE)
        print(f'{Style.RESET_ALL}Digite ou cole o diretório de destino do backup: ')
        self.destination_dir = input(Fore.BLUE)
        self.insert_password()
        print('Digite um nome para o backup: ')
        self.name_backup = input(Fore.BLUE)
        Backup.compress_backup('folder', self.name_backup, self.source_dir, self.name_backup, self.destination_dir, self.password)

    def insert_password(self):
        while True:
            print(f'{Style.RESET_ALL}Digite a senha para backup - Pressione Enter para deixar em branco')
            self.password = getpass()
            if self.password == '':
                self.password = None
                return self.password
            print('Digite novamente a senha para backup')
            self.repeat_password = getpass()
            if self.password != self.repeat_password:
                print(f'\n{Fore.RED}Senhas não conferem!\n')
            else:
                return self.password
                break
        
        