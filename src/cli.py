from __future__ import print_function, unicode_literals
from art import text2art
from clint.textui import prompt, validators
from src.backup import Backup
from src.constants import THUNDERBIRD_PATH, OUTLOOK_PATH
from getpass import getpass
from src.process import kill_process

class Cli:
    def __init__(self):
        self.welcome()    
        self.start_cli()
    

    def welcome(self):
        print(text2art('mybackupy'))


    def start_cli(self):   
        while True:     
            response = self.main_menu()
            if response == 'exit':
                print('Finalizado.')
                break
            self.choise_menu_option(response)()
            

    def create_backup(self):
        self.source_dir = self.ask_the_question_path('Digite ou cole o endereço do diretorio para realizar o backup: ')
        self.destination_dir = self.ask_the_question_path('Digite ou cole o diretório de destino do backup: ')
        self.password = self.insert_password()
        self.name_backup = prompt.query('Digite um nome para o backup: ')
        Backup.compress_backup(self, self.name_backup, self.source_dir, self.destination_dir, self.password)
    

    def create_backup_email(self):
        self.email_name = self.select_email()
        self.destination_dir = self.ask_the_question_path('Digite ou cole o diretório de destino do backup: ')
        self.password = self.insert_password()
        self.name_backup = self.email_name
        kill_process(self.name_backup)
        if(self.name_backup == 'thunderbird'):
            Backup.compress_backup(self, self.name_backup, THUNDERBIRD_PATH, self.destination_dir, self.password)
        else:
            Backup.compress_backup(self, self.name_backup, OUTLOOK_PATH, self.destination_dir, self.password)


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
                print('\nSenhas não conferem!\n')
            else:
                return self.password
    

    def extract_backup_cli(self):
        self.source_backup = self.ask_the_question_path('Digite o endereço do backup incluindo o nome do arquivo: ')
        self.destination_backup = self.ask_the_question_path('Digite o destino para extrair o backup:')
        self.password = self.insert_password()
        Backup.extract_backup(self, self.source_backup, self.destination_backup, self.password)


    def choise_menu_option(self, option):
        options = {
            'folder_backup': self.create_backup,
            'email_backup': self.create_backup_email,
            'restore_backup': self.extract_backup_cli,
        }
        return options.get(option)


    def ask_the_question_path(self, question):
        return prompt.query(question, validators=[validators.PathValidator()])
    

    def main_menu(self):
        print('Bem vindo ao utiliario de backup!\n')
        inst_options = [
                {'selector':'1','prompt':'Realizar backup de pasta','return':'folder_backup'},
                {'selector':'2','prompt':'Realizar backup de e-mail','return':'email_backup'},
                {'selector':'3','prompt':'Recuperar backup','return':'restore_backup'},
                {'selector':'4','prompt':'Finalizar','return':'exit'}
        ]

        return prompt.options("Selecione uma opção", inst_options)


    def select_email(self):
        print('Bem vindo ao utiliario de backup!\n')
        email_options = [
                {'selector':'1','prompt':'Outlook','return':'outlook'},
                {'selector':'2','prompt':'Thunderbird','return':'thunderbird'}
        ]
        return prompt.options("Selecione o cliente de e-mail", email_options)
   