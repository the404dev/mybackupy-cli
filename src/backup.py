from src.date import Date
import os
import py7zr

class Backup:

    def __init__(self):
        self.filename = None    

    def compress_backup(self, name, source_path, destination_path, password=None):
        try:
            os.chdir(destination_path)
        except (FileNotFoundError, FileExistsError, OSError, Exception):
            print('Caminho não encontrado! Verifique o caminho digitado!')
            return False
        datetime = Date.get_current_date_and_time()
        self.filename = f'{name}_{datetime}.7z'
                
        with py7zr.SevenZipFile(self.filename, 'w', password=password) as archive:
            print('\nComprimindo backup... Por favor aguarde...\n')
            try:
                archive.writeall(source_path, name)
                print('Compressão finalizada com sucesso!')
                return True
            except FileNotFoundError:
                print('Caminho não encontrado! Verifique o caminho digitado!')
                return False


    def extract_backup(self, source_backup_path, destination_path, password=None):
        try:
            archive = py7zr.SevenZipFile(source_backup_path, password=password)
            try:
                print('Extraindo backup... Por favor aguarde...')
                archive.extractall(path=destination_path)
                print('Finalizado com sucesso!')
                return True  
            except py7zr.exceptions.PasswordRequired:
                print('Necessária senha para descompactar')
                return
            except:
                print('Senha incorreta!')
                return
            finally:
                archive.close()
                print(f'Arquivo disponível em: {destination_path}')
        except FileNotFoundError:
            print(f'Caminho não encontrado! Verifique o caminho digitado!')
            return
