import os

def kill_process(*args):
    for title in args:
        os.system(f'taskkill /f /im {title}.exe')
