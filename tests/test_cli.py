from mybackupy.cli import Cli
from mybackupy.constants import *
from unittest import TestCase

class ProcessTest(TestCase):
    
    def setUp(self) -> None:
        self.cli = Cli()
        return super().setUp()


    def test_backup_with_args_source(self):
        parser = self.cli.parser.parse_args([
            'backup', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-n', TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.source, TEST_SOURCE_PATH_BACKUP)


    def test_backup_with_args_destination(self):
        parser = self.cli.parser.parse_args([
            'backup', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-n', TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.destination, TEST_DESTINATION_PATH_BACKUP)


    def test_backup_with_args_name(self):
        parser = self.cli.parser.parse_args([
            'backup', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-n', TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.name, TEST_NAME_BACKUP)


    def test_backup_with_args_password(self):
        parser = self.cli.parser.parse_args([
            'backup', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-n', TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.password, TEST_PASSWORD)


    def test_backup_without_args_password(self):
        parser = self.cli.parser.parse_args([
            'backup', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-n', TEST_NAME_BACKUP
        ])
        self.assertEqual(parser.password, None)


    def test_extract_with_args_source(self):
        parser = self.cli.parser.parse_args([
            'extract', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.source, TEST_SOURCE_PATH_BACKUP)


    def test_extract_with_args_destination(self):
        parser = self.cli.parser.parse_args([
            'extract', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.destination, TEST_DESTINATION_PATH_BACKUP)


    def test_extract_with_args_password(self):
        parser = self.cli.parser.parse_args([
            'extract', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.password, TEST_PASSWORD)


    def test_extract_without_args_password(self):
        parser = self.cli.parser.parse_args([
            'extract', '-s', TEST_SOURCE_PATH_BACKUP, '-d', TEST_DESTINATION_PATH_BACKUP,
        ])
        self.assertEqual(parser.password, None)


    def test_thunderbird_with_args_destination(self):
        parser = self.cli.parser.parse_args([
            'thunderbird','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.destination, TEST_DESTINATION_PATH_BACKUP)


    def test_thunderbird_with_args_name(self):
        parser = self.cli.parser.parse_args([
            'thunderbird','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.name, TEST_NAME_BACKUP)


    def test_thunderbird_with_args_password(self):
        parser = self.cli.parser.parse_args([
            'thunderbird','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.password, TEST_PASSWORD)


    def test_thunderbird_without_args_password(self):
        parser = self.cli.parser.parse_args([
            'thunderbird','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP,
        ])
        self.assertEqual(parser.password, None)


    def test_outlook_with_args_destination(self):
        parser = self.cli.parser.parse_args([
            'outlook','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.destination, TEST_DESTINATION_PATH_BACKUP)


    def test_outlook_with_args_name(self):
        parser = self.cli.parser.parse_args([
            'outlook','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.name, TEST_NAME_BACKUP)


    def test_outlook_with_args_password(self):
        parser = self.cli.parser.parse_args([
            'outlook','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP, '-p', TEST_PASSWORD
        ])
        self.assertEqual(parser.password, TEST_PASSWORD)


    def test_outlook_without_args_password(self):
        parser = self.cli.parser.parse_args([
            'outlook','-d', TEST_DESTINATION_PATH_BACKUP, '-n' , TEST_NAME_BACKUP,
        ])
        self.assertEqual(parser.password, None)


    def tearDown(self) -> None:
        return super().tearDown()