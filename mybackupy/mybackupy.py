from __future__ import print_function, unicode_literals
from art import text2art
import colorama, os, py7zr
from colorama import Fore, Style
from datetime import datetime
from getpass import getpass, getuser
import os
from PyInquirer import prompt


def kill_process(*args):
    for title in args:
        os.system(f'taskkill /f /im {title}.exe')



def get_current_date_and_time():
    now = datetime.now()
    str_datetime = now.strftime("%d_%m_%Y_%H_%M_%S")
    return str_datetime


def compress_backup(zip_filename, source_file, detination_name_path_7zip, destination_backup_folder, password=None):
    try:
        os.chdir(destination_backup_folder)
    except (FileNotFoundError, FileExistsError, OSError, Exception):
        print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
        return
    datetime = get_current_date_and_time()
            
    with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=password) as archive:
        print(f'\n{Fore.YELLOW}Comprimindo backup... Por favor aguarde...\n')
        try:
            archive.writeall(source_file, detination_name_path_7zip)
            print(Fore.GREEN + 'compressão finalizada com sucesso!' + Style.RESET_ALL)
        except FileNotFoundError:
            print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
            return


def extract_backup(source_backup_path, destination_backup_folder, password=None):
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
        self.welcome()    
        self.start_cli()
    

    def welcome(self):
        colorama.init(autoreset=True)
        print(Fore.GREEN + text2art('mybackupy'))


    def start_cli(self):   
        while True:     
            print(f'{Fore.BLUE}Bem vindo ao utiliario de backup!\n')
            response = prompt(self.main_menu())  
            if response['menu_principal'] == 'finalizar':
                print(f'{Fore.BLUE}Finalizado.')
                break
            

    def create_backup(self):
        self.source_dir = self.ask_the_question('Digite ou cole o endereço do diretorio para realizar o backup: ')
        self.destination_dir = self.ask_the_question('Digite ou cole o diretório de destino do backup: ')
        self.password = self.insert_password()
        self.name_backup = self.ask_the_question('Digite um nome para o backup: ')
        compress_backup(self.name_backup, self.source_dir, self.name_backup, self.destination_dir, self.password)
    

    def create_backup_email(self):
        THUNDERBIRD_PATH= "C:/Users/"+getuser()+"/AppData/Roaming/Thunderbird"
        OUTLOOK_PATH= "C:/Users/"+getuser()+"Documents/Arquivos do Outlook"

        self.email_name = prompt(self.select_email())
        self.destination_dir = self.ask_the_question('Digite ou cole o diretório de destino do backup: ')
        self.password = self.insert_password()
        self.name_backup = self.email_name['email_select']
        kill_process(self.name_backup)
        if(self.name_backup == 'thunderbird'):
            compress_backup(self.name_backup, THUNDERBIRD_PATH, self.name_backup, self.destination_dir, self.password)
        else:
            compress_backup(self.name_backup, OUTLOOK_PATH, self.name_backup, self.destination_dir, self.password)


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
    

    def extract_backup_cli(self):
        self.source_backup = self.ask_the_question('Digite o endereço do backup incluindo o nome do arquivo: ')
        self.destination_backup = self.ask_the_question('Digite o destino para extrair o backup:')
        self.password = self.insert_password()
        extract_backup(self.source_backup, self.destination_backup, self.password)


    def choise_menu_option(self, option):
        options = {
            'backup de pasta': self.create_backup,
            'backup de e-mail': self.create_backup_email,
            'extrair backup': self.extract_backup_cli,
        }
        return options.get(option)


    def ask_the_question(self, question):
        print(Fore.YELLOW + question)
        self.response = input(Fore.BLUE)
        print(Style.RESET_ALL)
        return self.response
    

    def main_menu(self):
        return [
            {
            'type': 'list',
            'name': 'menu_principal',
            'message': 'Escolha uma opção de backup:',
            'choices': ['backup de pasta', 'backup de e-mail', 'extrair backup', 'finalizar'],
            'filter': lambda i: self.choise_menu_error(i),
            'default': 'finalizar'
            }
        ]
    

    def choise_menu_error(self, option):
        try: self.choise_menu_option(option)() 
        except Exception:  return option


    def select_email(self):
        return {
            'type': 'list',
            'name': 'email_select',
            'message': 'Selecione de qual e-mail deseja fazer backup:',
            'choices': ['outlook', 'thunderbird'],
            'filter': lambda option:option,
        }
            

def main():
    Cli()

if __name__ == "__main__":
    main()