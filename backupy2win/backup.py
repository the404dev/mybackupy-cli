import os, py7zr
from process import Process as proc
from date import Date

class Backup:

    def compress_backup(backup_type, zip_filename, source_file, detination_name_path_7zip, destination_backup_folder):
        if backup_type == 'email':
            proc.kill_process('thunderbird', 'outlook')
            
        os.chdir(destination_backup_folder)
        datetime = Date.get_current_date_and_time()
        with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=os.environ['ENCRYPT']) as archive:
            print('Realizando backup...')
            print('Por favor aguarde...')
            archive.writeall(source_file, detination_name_path_7zip)
