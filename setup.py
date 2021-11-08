from setuptools import setup, find_packages

setup(
    name='MyBackupy',
    version='1.0.0b0',
    description='Easily create and recover backups. MyBackupy compresses the contents of your folders into 7zip files for easy recovery.',
    author='Cristian Penteado',
    author_email='contato@cristianpdev.com',
    url='https://github.com/cristianpdev/MyBackupy/',
    package_dir={"": "."},
    packages=find_packages(where="src"),
    tests_require=['pytest'],
)