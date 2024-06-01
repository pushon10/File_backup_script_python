# File_backup_script_python
Documenting my SRE project which backs up files

### README.md

```markdown
# File Backup Script

## Purpose

The File Backup Script is a Python script designed to automate the process of backing up important files from a source folder to a specified backup folder. It allows users to specify which file extensions or types to back up and optionally schedule backups at their convenience.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd file-backup-script
   ```

2. **Install dependencies:**

   Ensure you have Python installed. You can install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

   The script uses the following libraries:
   - `schedule` for scheduling tasks.
   - `argparse` for creating a command-line interface (CLI).

## Usage

### Command-Line Interface (CLI)

Run the script using the following command:

```bash
python backup_script.py <source_folder> <backup_folder> [--extensions EXT [EXT ...]] [--schedule]
```

#### Arguments:

- `source_folder`: Path to the source folder containing the files you want to back up.
- `backup_folder`: Path to the folder where the backup copies will be stored.
- `--extensions EXT [EXT ...]` (optional): List of file extensions to back up. Example: `.sh .txt`.
- `--schedule` (optional): Enable scheduled backups.

#### Examples:

1. **Perform a one-time backup:**

   ```bash
   python backup_script.py "C:/Users/User/Documents/Linux_Automation_Scripts" "C:/Users/User/Downloads/backup" --extensions .sh .txt
   ```

   This command will copy files with extensions `.sh` and `.txt` from `C:/Users/User/Documents/Linux_Automation_Scripts` to `C:/Users/User/Downloads/backup`.

2. **Enable scheduled backups:**

   ```bash
   python backup_script.py "C:/Users/User/Documents/Linux_Automation_Scripts" "C:/Users/User/Downloads/backup" --extensions .sh .txt --schedule
   ```

   This command will schedule daily backups at 2:00 AM for files with extensions `.sh` and `.txt`.

### Scheduling Backups

To configure scheduled backups, use the `--schedule` option when running the script:

```bash
python backup_script.py <source_folder> <backup_folder> --schedule
```

Scheduled backups are set to run daily at 2:00 AM by default. You can customize the schedule by editing the `schedule_daily_backups` function in the script.

### Additional Tips

- **Customizing Backup Locations:** You can modify the `source_folder` and `backup_folder` paths directly in the script or specify them using command-line arguments.
  
- **Handling Exceptions:** The script includes error handling to ensure that the source folder exists and that the backup folder is created if it doesn't exist.

- **Contributing:** Contributions are welcome! Fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

## Test Cases for Backup Script (Tested on 01/06/2024)

### 1. test_successful_backup
- **Description**: Test successful backup of files.
- **Input**: Valid source and backup folder paths.
- **Expected Result**: All files from the source folder should be copied to the backup folder.
- **Actual Result**: All files from the source folder copied to the backup folder.

### 2. test_backup_with_extensions
- **Description**: Test backup of files with specific extensions.
- **Input**: Valid source and backup folder paths with specified extensions (e.g., `.txt`, `.jpg`).
- **Expected Result**: Only files with the specified extensions should be copied to the backup folder.
- **Actual Result**: Only files with the specified extensions copied to the backup folder.

### 3. test_source_folder_not_exist
- **Description**: Test backup when the source folder does not exist.
- **Input**: Non-existent source folder path.
- **Expected Result**: Raises `FileNotFoundError`.
- **Actual Result**: Raises `FileNotFoundError`.

### 4. test_backup_folder_creation
- **Description**: Test backup when the backup folder does not exist (should create the folder).
- **Input**: Valid source folder path and a non-existent backup folder path.
- **Expected Result**: The backup folder should be created, and files should be copied.
- **Actual Result**: The backup folder is created, and files are copied.

### 5. test_backup_with_no_extensions
- **Description**: Test backup with no file extensions specified.
- **Input**: Valid source and backup folder paths.
- **Expected Result**: All files from the source folder should be copied to the backup folder.
- **Actual Result**: All files from the source folder copied to the backup folder.

### 6. test_backup_with_empty_source_folder
- **Description**: Test backup with an empty source folder.
- **Input**: Empty source folder path and a valid backup folder path.
- **Expected Result**: The backup folder should be created, but no files should be copied.
- **Actual Result**: The backup folder is created, but no files should be copied.



