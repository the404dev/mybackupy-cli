import os, py7zr
from process import Process as proc
from date import Date

class Backup:

    def compress_backup(backup_type, zip_filename, source_file, detination_name_path_7zip, destination_backup_folder, password=None):
        if backup_type == 'email':
            proc.kill_process('thunderbird', 'outlook')
            
        os.chdir(destination_backup_folder)
        datetime = Date.get_current_date_and_time()
        with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=password) as archive:
            print('Comprimindo backup...')
            print('Por favor aguarde...')
            archive.writeall(source_file, detination_name_path_7zip)
            print('compressão finalizada com sucesso!')
    
    def decompress_backup(source_backup_path, destination_backup_folder, password=None):
        try:
            archive = py7zr.SevenZipFile(source_backup_path, password=password)
            print('Descomprimindo backup...')
            print('Por favor aguarde...')
            archive.extractall(path=destination_backup_folder)
        except py7zr.exceptions.PasswordRequired:
            print('Necessária senha para descompactar')
            archive.close()
            return
        except:
            print('Senha incorreta!')
            archive.close()
            return
        print('Finalizado com sucesso!')
        print(f'Arquivo disponível em: {destination_backup_folder}')
        archive.close()
