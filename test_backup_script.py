import unittest
import os
import shutil
# This should go without saying, but the idea here is that 'backup_script should be in the same directory as 'test_backup_script. Duh!'
from backup_script import backup_files

class TestBackupScript(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.source_folder = 'test_source'
        self.backup_folder = 'test_backup'
        self.extensions = ['.txt', '.jpg']

        # Create test source folder and files
        os.makedirs(self.source_folder, exist_ok=True)
        with open(os.path.join(self.source_folder, 'file1.txt'), 'w') as f:
            f.write("This is a test file.")
        with open(os.path.join(self.source_folder, 'file2.jpg'), 'w') as f:
            f.write("This is another test file.")
        with open(os.path.join(self.source_folder, 'file3.pdf'), 'w') as f:
            f.write("This is a PDF file.")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.source_folder):
            shutil.rmtree(self.source_folder)
        if os.path.exists(self.backup_folder):
            shutil.rmtree(self.backup_folder)

    def test_successful_backup(self):
        """Test successful backup of files."""
        backup_files(self.source_folder, self.backup_folder)
        self.assertTrue(os.path.exists(self.backup_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file2.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file3.pdf')))

    def test_backup_with_extensions(self):
        """Test backup of files with specific extensions."""
        backup_files(self.source_folder, self.backup_folder, self.extensions)
        self.assertTrue(os.path.exists(self.backup_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file2.jpg')))
        self.assertFalse(os.path.exists(os.path.join(self.backup_folder, 'file3.pdf')))

    def test_source_folder_not_exist(self):
        """Test backup when the source folder does not exist."""
        with self.assertRaises(FileNotFoundError):
            backup_files('non_existent_folder', self.backup_folder)

    def test_backup_folder_creation(self):
        """Test backup when the backup folder does not exist (should create the folder)."""
        backup_files(self.source_folder, 'new_backup_folder')
        self.assertTrue(os.path.exists('new_backup_folder'))
        shutil.rmtree('new_backup_folder')

    def test_backup_with_no_extensions(self):
        """Test backup with no file extensions specified."""
        backup_files(self.source_folder, self.backup_folder)
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file2.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.backup_folder, 'file3.pdf')))

    def test_backup_with_empty_source_folder(self):
        """Test backup with empty source folder."""
        empty_folder = 'empty_source'
        os.makedirs(empty_folder, exist_ok=True)
        backup_files(empty_folder, self.backup_folder)
        self.assertTrue(os.path.exists(self.backup_folder))
        self.assertEqual(len(os.listdir(self.backup_folder)), 0)
        shutil.rmtree(empty_folder)

if __name__ == '__main__':
    unittest.main()
