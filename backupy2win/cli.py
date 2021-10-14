from art import text2art
import colorama, os, py7zr
from colorama import Fore, Style
from datetime import datetime
from getpass import getpass
import os

class Process:
    def kill_process(*args):
        for title in args:
            os.system(f'taskkill /f /im {title}.exe')

class Date:
    def get_current_date_and_time():
        now = datetime.now()
        str_datetime = now.strftime("%d_%m_%Y_%H_%M_%S")
        return str_datetime

class Backup:

    def compress_backup(zip_filename, source_file, detination_name_path_7zip, destination_backup_folder, password=None):
        try:
            os.chdir(destination_backup_folder)
        except (FileNotFoundError, FileExistsError):
            print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
            return
        datetime = Date.get_current_date_and_time()
                
        with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=password) as archive:
            print(f'\n{Fore.YELLOW}Comprimindo backup... Por favor aguarde...\n')
            try:
                archive.writeall(source_file, detination_name_path_7zip)
                print(Fore.GREEN + 'compressão finalizada com sucesso!' + Style.RESET_ALL)
            except FileNotFoundError:
                print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
                return
    
    def extract_backup(self, source_backup_path, destination_backup_folder, password=None):
        try:
            archive = py7zr.SevenZipFile(source_backup_path, password=password)
            try:
                print(f'{Fore.YELLOW}Extraindo backup... Por favor aguarde...')
                archive.extractall(path=destination_backup_folder)
            
            except py7zr.exceptions.PasswordRequired:
                print(f'{Fore.RED}Necessária senha para descompactar')
                return
            except:
                print(f'{Fore.RED}Senha incorreta!')
                return
            finally:
                archive.close()
            print('Finalizado com sucesso!')
            print(f'Arquivo disponível em: {destination_backup_folder}')
        except FileNotFoundError:
            print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
            return
            
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
 --------------------------
| 1) FAZER BACKUP DE PASTA |
 --------------------------
 ---------------------------
| 2) FAZER BACKUP DE E-MAIL |
 ---------------------------
 ---------------------
| 3) RESTAURAR BACKUP |
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
        self.source_dir = self.ask_the_question('Digite ou cole o endereço do diretorio para realizar o backup: ')
        self.destination_dir = self.ask_the_question('Digite ou cole o diretório de destino do backup: ')
        self.insert_password()
        self.name_backup = self.ask_the_question('Digite um nome para o backup: ')
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
        self.source_backup = self.ask_the_question('Digite o endereço do backup incluindo o nome do arquivo: ')
        self.destination_backup = self.ask_the_question('Digite o destino para extrair o backup:')
        print('Digite a senha para extrair o arquivo - Deixe em branco se não possuir')
        self.password = self.insert_password()
        Backup.extract_backup(self.source_backup, self.destination_backup, self.password)

    def create_backup_email(self):
        Process.kill_process('thunderbird','outlook')
        self.create_backup()

    def choise_menu_option(self, option):
        options = {
            1: self.create_backup,
            2: self.create_backup_email,
            3: self.extract_backup,
        }
        return options.get(option)
    
    def ask_the_question(self, question):
        print(Fore.YELLOW + question)
        self.response = input(Fore.BLUE)
        print(Style.RESET_ALL)
        return self.response
        

def main():
    Cli()

if __name__ == "__main__":
    main()