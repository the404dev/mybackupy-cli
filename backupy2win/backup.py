import os, py7zr
from datetime import datetime
class Backup:
    def __init__(self) -> None:
        pass
        

    def compress_7z_and_backup(type, filename, source_path, final_path):
        if type == 'email':
            print('closing Thunderbird')
            os.system('taskkill /f /im thunderbird.exe')
        
        os.chdir(r'C:\Backups')

        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

        with py7zr.SevenZipFile(f'{filename}_{dt_string}.7z', 'w', password=os.environ['ENCRYPT']) as archive:
            print('Realizando backup...')
            print('Por favor aguarde...')
            archive.writeall(source_path, final_path)