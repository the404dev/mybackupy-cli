from getpass import getuser
import os

""" Windows path"""
THUNDERBIRD_PATH= "C:/Users/"+getuser()+"/AppData/Roaming/Thunderbird"
OUTLOOK_PATH= "C:/Users/"+getuser()+"Documents/Arquivos do Outlook"

""" Tests """
TEST_NAME_BACKUP="test"
TEST_SOURCE_PATH_BACKUP="C:/Tests"
TEST_DESTINATION_PATH_BACKUP="C:/Backups"
TEST_PASSWORD="1234"

""" Version """
version_file = open((f'{os.getcwd()}\VERSION'))
VERSION=version_file.read().strip()

""" CLI """
CLI_NAME="MyBackupy"
CLI_DESCRIPTION="Easily create and recover backups. MyBackupy compresses the contents of your folders into 7zip files for easy recovery."
CLI_BACKUP_DESCRIPTION="Backup your folders"
CLI_EXTRACT_DESCRIPTION="Extract your backups back into folders"
CLI_THUNDERBIRD_DESCRIPTION="Backup your Thunderbird emails"
CLI_OUTLOOK_DESCRIPTION="Backup your Outlook emails"

""" Help CLI """
HELP_BACKUP_SRC="directory to compress and backup"
HELP_EXTRACT_SRC="full path including backup file name"

HELP_BACKUP_DEST="destination directory for backup"
HELP_EXTRACT_DEST="directory for backup extraction"
HELP_THUNDERBIRD_DEST="destination directory for Thunderbird backup"
HELP_OUTLOOK_DEST="destination directory for Outlook backup"

HELP_NAME="name for backup file"

HELP_PASSWORD="password to protect the backup file"
HELP_EXTRACT_PASSWORD="password to extract the backup file"
