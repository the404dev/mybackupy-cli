from src.backup import Backup
from src.constants import TEST_NAME_BACKUP, TEST_SOURCE_PATH_BACKUP, TEST_DESTINATION_PATH_BACKUP
from unittest import TestCase

class ProcessTest(TestCase):
    
    def setUp(self) -> None:
        return super().setUp()


    def test_compress_backup(self):
        backup = Backup()
        compress = backup.compress_backup(
            TEST_NAME_BACKUP,
            TEST_SOURCE_PATH_BACKUP,
            TEST_DESTINATION_PATH_BACKUP
        )
              
        self.assertTrue(compress)
    
    def test_extract_backup(self):
        backup = Backup()

        backup.compress_backup(
            TEST_NAME_BACKUP,
            TEST_SOURCE_PATH_BACKUP,
            TEST_DESTINATION_PATH_BACKUP
        )
        extract = backup.extract_backup(backup.filename, TEST_DESTINATION_PATH_BACKUP)

        self.assertTrue(extract)
    
    def tearDown(self) -> None:
        return super().tearDown()