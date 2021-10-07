import os, py7zr
from colors import Color
from process import Process as proc
from date import Date

class Backup:

    def compress_backup(backup_type, zip_filename, source_file, detination_name_path_7zip, destination_backup_folder, password=None):
        if backup_type == 'email':
            proc.kill_process('thunderbird', 'outlook')
            
        os.chdir(destination_backup_folder)
        datetime = Date.get_current_date_and_time()
        with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=password) as archive:
            print(Color.INFO + 'Comprimindo backup...' + Color.RESET)
            print(Color.INFO + 'Por favor aguarde...' + Color.RESET)
            archive.writeall(source_file, detination_name_path_7zip)
            print(Color.OK + 'compressão finalizada com sucesso!' + Color.RESET)
    
    def decompress_backup(source_backup_path, destination_backup_folder, password=None):
        try:
            archive = py7zr.SevenZipFile(source_backup_path, password=password)
            print(Color.INFO + 'Descomprimindo backup...' + Color.RESET)
            print(Color.INFO + 'Por favor aguarde...' + Color.RESET)
            archive.extractall(path=destination_backup_folder)
        except py7zr.exceptions.PasswordRequired:
            print(Color.FAIL + 'Necessária senha para descompactar' + Color.RESET)
            archive.close()
            return
        except:
            print(Color.FAIL + 'Senha incorreta!' + Color.RESET)
            archive.close()
            return
        print(Color.OK + 'Finalizado com sucesso!' + Color.RESET)
        print(Color.INFO + f'Arquivo disponível em: {destination_backup_folder}' + Color.RESET)
        archive.close()
