import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)

class FileOrganizer:
    """Automatically organizes files in a directory based on file types."""
    
    def __init__(self, target_directory):
        """Initialize the FileOrganizer with a target directory."""
        self.target_directory = Path(target_directory)
        
        # Define file categories and their extensions
        self.file_categories = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt', '.rtf'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.tiff', '.webp'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.rb', '.go', '.rs'],
            'Executables': ['.exe', '.msi', '.apk', '.deb', '.rpm', '.dmg'],
            'Others': []  # Catch-all for unrecognized extensions
        }
    
    def create_folders(self):
        """Create category folders if they don't exist."""
        try:
            for category in self.file_categories.keys():
                folder_path = self.target_directory / category
                folder_path.mkdir(exist_ok=True)
                logging.info(f"Folder created/verified: {category}")
        except Exception as e:
            logging.error(f"Error creating folders: {e}")
            raise
    
    def get_file_category(self, file_extension):
        """Determine the category of a file based on its extension."""
        file_extension = file_extension.lower()
        
        for category, extensions in self.file_categories.items():
            if file_extension in extensions:
                return category
        
        return 'Others'  # Default category for unknown extensions
    
    def organize_files(self):
        """Scan and organize files in the target directory."""
        if not self.target_directory.exists():
            logging.error(f"Directory does not exist: {self.target_directory}")
            return
        
        if not self.target_directory.is_dir():
            logging.error(f"Path is not a directory: {self.target_directory}")
            return
        
        # Create necessary folders
        self.create_folders()
        
        files_moved = 0
        files_skipped = 0
        
        try:
            # Iterate through all files in the target directory
            for item in self.target_directory.iterdir():
                # Skip directories and hidden files
                if item.is_dir() or item.name.startswith('.'):
                    continue
                
                try:
                    # Get file extension
                    file_extension = item.suffix
                    
                    # Determine category
                    category = self.get_file_category(file_extension)
                    
                    # Define destination path
                    destination_folder = self.target_directory / category
                    destination_path = destination_folder / item.name
                    
                    # Handle duplicate filenames
                    if destination_path.exists():
                        base_name = item.stem
                        extension = item.suffix
                        counter = 1
                        
                        while destination_path.exists():
                            new_name = f"{base_name}_{counter}{extension}"
                            destination_path = destination_folder / new_name
                            counter += 1
                    
                    # Move the file
                    shutil.move(str(item), str(destination_path))
                    logging.info(f"Moved: {item.name} → {category}/")
                    files_moved += 1
                    
                except Exception as e:
                    logging.error(f"Error moving {item.name}: {e}")
                    files_skipped += 1
            
            # Summary
            logging.info(f"\n{'='*50}")
            logging.info(f"Organization Complete!")
            logging.info(f"Files moved: {files_moved}")
            logging.info(f"Files skipped: {files_skipped}")
            logging.info(f"{'='*50}")
            
        except Exception as e:
            logging.error(f"Error during file organization: {e}")
            raise

def main():
    """Main function to run the file organizer."""
    print("=" * 60)
    print("FILE ORGANIZER - Automatic File Organization Tool")
    print("=" * 60)
    
    # Get target directory from user
    target_dir = input("\nEnter the path of the directory to organize: ").strip()
    
    # Remove quotes if present
    target_dir = target_dir.strip('"').strip("'")
    
    if not target_dir:
        print("Error: No directory path provided.")
        return
    
    # Confirm before proceeding
    print(f"\nTarget Directory: {target_dir}")
    confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("Operation cancelled.")
        return
    
    try:
        # Create organizer instance and organize files
        organizer = FileOrganizer(target_dir)
        organizer.organize_files()
        print("\n✓ Files organized successfully!")
        print(f"Check 'file_organizer.log' for detailed information.")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        logging.error(f"Program error: {e}")

if __name__ == "__main__":
    main()
