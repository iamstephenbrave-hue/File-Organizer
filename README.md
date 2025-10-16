File Organizer - Automatic File Organization Tool
📋 Project Description
A Python automation script that automatically organizes files in a target directory based on their file types. The script scans a specified directory, identifies file types by their extensions, creates appropriate category folders, and moves files accordingly.
🎯 Features

Automatic File Classification: Identifies and categorizes files based on extensions
Dynamic Folder Creation: Creates category folders automatically
Duplicate Handling: Renames duplicate files to prevent overwriting
Comprehensive Logging: Records all operations with timestamps
Error Handling: Robust exception handling for safe operation
Multiple Categories: Organizes into 8 predefined categories

📁 File Categories
The script organizes files into the following categories:

Documents: PDF, DOC, DOCX, TXT, XLSX, XLS, PPT, PPTX, ODT, RTF
Images: JPG, JPEG, PNG, GIF, BMP, SVG, ICO, TIFF, WEBP
Videos: MP4, AVI, MKV, MOV, WMV, FLV, WEBM, M4V
Audio: MP3, WAV, FLAC, AAC, OGG, WMA, M4A
Archives: ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ
Code: PY, JAVA, CPP, C, JS, HTML, CSS, PHP, RB, GO, RS
Executables: EXE, MSI, APK, DEB, RPM, DMG
Others: All unrecognized file types

🚀 Installation
Prerequisites

Python 3.6 or higher
No external libraries required (uses only standard library)

Setup

Download the file_organizer.py script
Save it to your desired location
No additional installation needed!

💻 Usage
Basic Usage

Open Terminal/Command Prompt

bash   cd path/to/script/location

Run the Script

bash   python file_organizer.py

Enter Directory Path

When prompted, enter the full path of the directory you want to organize
Example: C:\Users\YourName\Downloads


Confirm Operation

Review the target directory
Type yes or y to proceed



Example
bash$ python file_organizer.py

============================================================
FILE ORGANIZER - Automatic File Organization Tool
============================================================

Enter the path of the directory to organize: C:\Users\John\Downloads

Target Directory: C:\Users\John\Downloads
Do you want to proceed? (yes/no): yes

✓ Files organized successfully!
Check 'file_organizer.log' for detailed information.
📊 Output
After execution, you'll find:

Organized Folders: Category folders created in the target directory
Log File: file_organizer.log with detailed operation history
Moved Files: All files sorted into appropriate category folders

🛡️ Safety Features

Non-Destructive: Only moves files, never deletes
Duplicate Protection: Renames files to prevent overwriting
Skips System Files: Ignores hidden files and folders
Detailed Logging: Complete audit trail of all operations
Error Recovery: Continues operation even if individual files fail

📝 Log File
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
⚠️ Important Notes

Backup First: Consider backing up important files before running
Path Format: Use absolute paths for best results
Permissions: Ensure you have read/write permissions for the target directory
Nested Files: The script only organizes files in the root of the target directory

🐛 Troubleshooting
Issue: "Directory does not exist"

Solution: Verify the path is correct and accessible

Issue: "Permission denied"

Solution: Run with administrator/sudo privileges or check folder permissions

Issue: Files not moving

Solution: Check the log file for specific error messages

📄 License
This project is created for educational purposes as part of a Python internship program.
👨‍💻 Author
Created as part of Python Internship Project
🤝 Contributing
Feel free to suggest improvements or report issues!

Version: 1.0.0
Last Updated: October 2025
