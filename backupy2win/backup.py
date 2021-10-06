import os, py7zr
from datetime import datetime
class Backup:
    def __init__(self) -> None:
        pass

    def compress_backup(backup_type, zip_filename, source_file, detination_name_path):
        if backup_type == 'email':
            print('closing e-mail client')
            os.system('taskkill /f /im thunderbird.exe')
            os.system('taskkill /f /im outlook.exe')
        
        os.chdir(r'C:\Backups')

        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

        with py7zr.SevenZipFile(f'{zip_filename}_{dt_string}.7z', 'w', password=os.environ['ENCRYPT']) as archive:
            print('Realizando backup...')
            print('Por favor aguarde...')
            archive.writeall(source_file, detination_name_path)
