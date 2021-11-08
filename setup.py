from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='MyBackupy',
    version='1.0.0b0',
    description='Easily create and recover backups. MyBackupy compresses the contents of your folders into 7zip files for easy recovery.',
    author='Cristian Penteado',
    author_email='contato@cristianpdev.com',
    url='https://github.com/cristianpdev/MyBackupy/',
    package_dir={"": "."},
    packages=find_packages(where="src"),
    console=['mybackupy.py'],
    entry_points = ''' 
        [console_scripts] 
        mybackupy = mybackupy:main 
    ''', 
    tests_require=['pytest'],
)