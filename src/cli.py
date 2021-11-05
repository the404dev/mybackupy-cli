from __future__ import print_function, unicode_literals
import argparse, os
from art import text2art
from src.backup import Backup
from src.constants import *

class Cli:
    def __init__(self):
        self.welcome()   
        self.start_cli()
    

    def welcome(self):
        print(text2art(CLI_NAME))


    def add_backup_args(self):
        self.backup.add_argument('-s', '--source', type=str, help=HELP_BACKUP_SRC, required=True)
        self.backup.add_argument('-d', '--destination', type=str, help=HELP_BACKUP_DEST, required=True)
        self.backup.add_argument('-n', '--name', type=str, help=HELP_NAME, required=True)
        self.backup.add_argument('-p', '--password', type=str, help=HELP_PASSWORD)
    

    def add_extract_args(self):
        self.extract.add_argument('-s' ,'--source', type=str, help=HELP_EXTRACT_SRC, required=True)
        self.extract.add_argument('-d' ,'--destination', type=str, help=HELP_EXTRACT_DEST, required=True)
        self.extract.add_argument('-p' ,'--password', type=str, help=HELP_EXTRACT_PASSWORD, default=None)    


    def add_thunderbird_args(self):
        self.email_thunderbird.add_argument('-d','--destination', type=str, help=HELP_THUNDERBIRD_DEST, required=True)
        self.email_thunderbird.add_argument('-n','--name', type=str, help=HELP_NAME, required=True)
        self.email_thunderbird.add_argument('-p','--password', type=str, help=HELP_PASSWORD)


    def add_outlook_args(self):
        self.email_outlook.add_argument('-d','--destination', type=str, help=HELP_OUTLOOK_DEST, required=True)
        self.email_outlook.add_argument('-n','--name', type=str, help=HELP_NAME, required=True)
        self.email_outlook.add_argument('-p','--password', type=str, help=HELP_PASSWORD)


    def pre_load_args(self):
        self.parser = argparse.ArgumentParser(prog=CLI_NAME,description=CLI_DESCRIPTION)
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s version: '+VERSION)
        self.subparser = self.parser.add_subparsers(title="commands", dest='command')
        self.backup = self.subparser.add_parser('backup', add_help=True, description=CLI_BACKUP_DESCRIPTION)
        self.extract = self.subparser.add_parser('extract', add_help=True, description=CLI_EXTRACT_DESCRIPTION)
        self.email_thunderbird = self.subparser.add_parser('thunderbird', add_help=True, description=CLI_THUNDERBIRD_DESCRIPTION)
        self.email_outlook = self.subparser.add_parser('outlook', add_help=True, description=CLI_OUTLOOK_DESCRIPTION)
        

    def start_cli(self):
        self.pre_load_args()
        self.add_backup_args()
        self.add_extract_args()
        self.add_thunderbird_args()
        self.add_outlook_args()
        self.args = self.parser.parse_args()
        self.check_args()


    def check_args(self):
        if self.args.command == 'backup': self.compress_backup(self.args.source)
        elif self.args.command == 'extract': self.extract_backup()
        elif self.args.command == 'thunderbird': self.extract_backup(THUNDERBIRD_PATH)
        elif self.args.command == 'outlook': self.extract_backup(OUTLOOK_PATH)
        else: self.parser.print_help()


    def compress_backup(self, source):
        Backup.compress_backup(self, self.args.name, source, self.args.destination, self.args.password)


    def extract_backup(self):
        Backup.extract_backup(self, self.args.source, self.args.destination, self.args.password)

