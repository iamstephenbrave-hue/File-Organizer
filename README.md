============================================================
FILE ORGANIZER - Automatic File Organization Tool
============================================================

Enter the path of the directory to organize: C:\Users\John\Downloads

Target Directory: C:\Users\John\Downloads
Do you want to proceed? (yes/no): yes

 Files organized successfully!
Check 'file_organizer.log' for detailed information.
Output
After execution, you'll find:

Organized Folders: Category folders created in the target directory
Log File: file_organizer.log with detailed operation history
Moved Files: All files sorted into appropriate category folders

 Safety Features

Non-Destructive: Only moves files, never deletes
Duplicate Protection: Renames files to prevent overwriting
Skips System Files: Ignores hidden files and folders
Detailed Logging: Complete audit trail of all operations
Error Recovery: Continues operation even if individual files fail

Log File
The script creates a file_organizer.log file that records:

Timestamp of each operation
Files moved and their destinations
Any errors encountered
Summary statistics

Example log entry:
2025-10-10 14:30:15 - INFO - Folder created/verified: Documents
2025-10-10 14:30:15 - INFO - Moved: report.pdf → Documents/
2025-10-10 14:30:15 - INFO - Moved: photo.jpg → Images/
🔧 Customization
To add or modify file categories, edit the file_categories dictionary in the script:
pythonself.file_categories = {
    'YourCategory': ['.ext1', '.ext2', '.ext3'],
    # Add more categories as needed
}
Important Notes

Backup First: Consider backing up important files before running
Path Format: Use absolute paths for best results
Permissions: Ensure you have read/write permissions for the target directory
Nested Files: The script only organizes files in the root of the target directory

Troubleshooting
Issue: "Directory does not exist"

Solution: Verify the path is correct and accessible

Issue: "Permission denied"

Solution: Run with administrator/sudo privileges or check folder permissions

Issue: Files not moving

Solution: Check the log file for specific error messages

License
This project is created for educational purposes as part of a Python internship program.
Author
Created as part of Python Internship Project
Contributing
Feel free to suggest improvements or report issues!

Version: 1.0.0
Last Updated: October 2025
