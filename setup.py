from setuptools import setup

setup(
    packages = [
        'src/backup.py',
        'src/cli.py',
        'src/constants.py'
        'src/date.py'
        'src/process.py'
        ],
    tests_require=['pytest'],
)