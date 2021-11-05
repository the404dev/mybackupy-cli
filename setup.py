from setuptools import setup
import os

version_file = open((f'{os.getcwd()}\VERSION'))
version=version_file.read().strip()

setup(
    name='MyBackupy',
    version=version,
    description='Easily create and recover backups. MyBackupy compresses the contents of your folders into 7zip files for easy recovery.',
    author='Cristian Penteado',
    author_email='contato@cristianpdev.com',
    url='https://github.com/cristianpdev/MyBackupy/',
    packages = [
        'src/backup.py',
        'src/cli.py',
        'src/constants.py'
        'src/date.py'
        'src/process.py'
        ],
    tests_require=['pytest'],
)