# Importing the following libraries: os for file and directory operations, shutil for copying files, argparse for the CLI, schedule for scheduling tasks and time for time-related operations.
# I had to 'pip install schedule' 
import os
import shutil
import argparse
import schedule
import time

# Creating a function to check that we have source and backup folder
def backup_files(source_folder, backup_folder, file_extensions=None):
    # Check if the source and backup folders exist.
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder '{source_folder}' not found.")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder) # Create the backup folder if it doesn't exist.

    # If file extensions are specified, filter files based on extensions.
    if file_extensions:
        selected_files = [f for f in os.listdir(source_folder) if f.endswith(tuple(file_extensions))]
    else:
        selected_files = os.listdir(source_folder)

    # Copy selected files to the backup folder. A for loop is used to iterate over the selected files
    for file in selected_files:
        source_path = os.path.join(source_folder, file)
        backup_path = os.path.join(backup_folder, file)
        shutil.copy2(source_path, backup_path)
        print(f"Copied '{file}' to '{backup_folder}'")


# Define the function to schedule daily backups
def schedule_daily_backups(source_folder, backup_folder, file_extensions=None):
    # Schedule a daily backup job.
    schedule.every().day.at("02:00").do(backup_files, source_folder, backup_folder, file_extensions)

    # Infinite loop to run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(60)  # Sleep for 1 minute and check for scheduled tasks.

# Define function to create CLI
def create_cli():
    parser = argparse.ArgumentParser(description="File Backup Script")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("backup_folder", help="Path to the backup folder")
    parser.add_argument("--extensions", nargs="+", help="List of file extensions to back up")
    parser.add_argument("--schedule", action="store_true", help="Enable scheduled backups")

    args = parser.parse_args()

    if args.schedule:
        schedule_daily_backups(args.source_folder, args.backup_folder, args.extensions)
    else:
        backup_files(args.source_folder, args.backup_folder, args.extensions)

# Main function to run the CLI
if __name__ == "__main__":
    create_cli()

    




