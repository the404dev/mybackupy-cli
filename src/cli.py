from __future__ import print_function, unicode_literals
from art import text2art
from src.backup import Backup
from src.constants import THUNDERBIRD_PATH, OUTLOOK_PATH
import argparse

class Cli:
    def __init__(self):
        self.welcome()   
        self.start_cli()
    

    def welcome(self):
        print(text2art('mybackupy'))


    def compress_backup(self, source):
        Backup.compress_backup(self, self.args.name, source, self.args.destination, self.args.password)
    
    def extract_backup(self):
        Backup.extract_backup(self, self.args.source, self.args.destination, self.args.password)

    def start_cli(self):
        self.parser = argparse.ArgumentParser(prog="MyBackupy",description='Easily create and recover backups. MyBackupy compresses the contents of your folders into 7zip files for easy recovery.')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.2')

        self.subparser = self.parser.add_subparsers(title="commands", dest='command')
        self.backup = self.subparser.add_parser('backup_folder', add_help=True, description='Backup your folders')
        self.extract = self.subparser.add_parser('extract_backup', add_help=True, description='Extract your backups back into folders')
        self.email_thunderbird = self.subparser.add_parser('backup_thunderbird', add_help=True, description='Backup your Thunderbird emails')
        self.email_outlook = self.subparser.add_parser('backup_outlook', add_help=True, description='Backup your Outlook emails')

        self.backup.add_argument('-s', '--source', type=str, help='directory to compress and backup', required=True)
        self.backup.add_argument('-d', '--destination', type=str, help='destination directory for backup', required=True)
        self.backup.add_argument('-n', '--name', type=str, help='name for backup file', required=True)
        self.backup.add_argument('-p', '--password', type=str, help='password to protect the backup file')

        self.extract.add_argument('-s' ,'--source', type=str, help='full path including backup file name', required=True)
        self.extract.add_argument('-d' ,'--destination', type=str, help='directory for backup extraction', required=True)
        self.extract.add_argument('-p' ,'--password', type=str, help='password to extract the backup file', default=None)    

        self.email_thunderbird.add_argument('-d','--destination', type=str, help='destination directory for Thunderbird backup', required=True)
        self.email_thunderbird.add_argument('-n','--name', type=str, help='name for backup file', required=True)
        self.email_thunderbird.add_argument('-p','--password', type=str, help='password to protect the backup file')

        self.email_outlook.add_argument('-d','--destination', type=str, help='destination directory for Outlook backup', required=True)
        self.email_outlook.add_argument('-n','--name', type=str, help='name for backup file', required=True)
        self.email_outlook.add_argument('-p','--password', type=str, help='password to protect the backup file')


        self.args = self.parser.parse_args()
        self.check_args()


    def check_args(self):
        if self.args.command == 'backup_folder': self.compress_backup(self.args.source)
        elif self.args.command == 'extract_backup': self.extract_backup()
        elif self.args.command == 'backup_thunderbird': self.extract_backup(THUNDERBIRD_PATH)
        elif self.args.command == 'backup_outlook': self.extract_backup(OUTLOOK_PATH)
        else: self.parser.print_help()
