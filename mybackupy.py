from src.cli import Cli
from src.backup import Backup 
from src.constants import TEST_NAME_BACKUP, TEST_SOURCE_PATH_BACKUP, TEST_DESTINATION_PATH_BACKUP

def main():
    Cli()

if __name__ == "__main__":
    bkp = Backup()
    bkp.compress_backup(TEST_NAME_BACKUP, TEST_SOURCE_PATH_BACKUP, TEST_DESTINATION_PATH_BACKUP)