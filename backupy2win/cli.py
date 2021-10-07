from typing import Match
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
        option = 0
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
 -------------------
| 0) PARA FINALIZAR |
 -------------------
 -----------------
| 1) FAZER BACKUP |
 -----------------
 ---------------------
| 2) RESTAURAR BACKUP |
 ---------------------
            ''')
            option = int(input())
            if option == 0:
                print(f'{Fore.BLUE}Finalizado.')
                break

            self.choise_menu_option(option)()    

    def create_backup(self):
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
        Backup.compress_backup(self.name_backup, self.source_dir, self.name_backup, self.destination_dir, self.password)

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
    
    def extract_backup(self):
        print(Fore.YELLOW + ''' 
             ---------------------------
            | EXTRAIR ARQUIVO DE BACKUP |
             ---------------------------\n''')
        print('Digite o endereço do backup incluindo o nome do arquivo: ')
        self.source_backup = input(Fore.BLUE)
        print(f'{Style.RESET_ALL}Digite o destino para extrair o backup:')
        self.destination_backup = input(Fore.BLUE)
        print(f'{Style.RESET_ALL} Digite a senha para extrair o arquivo - Deixe em branco se não possuir')
        self.password = getpass()
        Backup.extract_backup(self.source_backup, self.destination_backup, self.password)

    def choise_menu_option(self, option):
        options = {
            1: self.create_backup,
            2: self.extract_backup,
        }
        return options.get(option)