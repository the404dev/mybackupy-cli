from colorama import Fore, Style, Back
from date import Date
import os, py7zr
from process import Process as proc

class Backup:

    def compress_backup(zip_filename, source_file, detination_name_path_7zip, destination_backup_folder, password=None):
        os.chdir(destination_backup_folder)
        datetime = Date.get_current_date_and_time()
        with py7zr.SevenZipFile(f'{zip_filename}_{datetime}.7z', 'w', password=password) as archive:
            print(f'\n{Fore.YELLOW}Comprimindo backup... Por favor aguarde...\n')
            archive.writeall(source_file, detination_name_path_7zip)
            print(Fore.GREEN + 'compressão finalizada com sucesso!' + Style.RESET_ALL)
    
    def extract_backup(self, source_backup_path, destination_backup_folder, password=None):
        try:
            archive = py7zr.SevenZipFile(source_backup_path, password=password)
            try:
                print(f'{Fore.YELLOW}Extraindo backup... Por favor aguarde...')
                archive.extractall(path=destination_backup_folder)
            
            except py7zr.exceptions.PasswordRequired:
                print(f'{Fore.RED}Necessária senha para descompactar')
                return
            except:
                print(f'{Fore.RED}Senha incorreta!')
                return
            finally:
                archive.close()
            print('Finalizado com sucesso!')
            print(f'Arquivo disponível em: {destination_backup_folder}')
        except FileNotFoundError:
            print(f'{Fore.RED}Caminho não encontrado! Verifique o caminho digitado!')
            return
            
