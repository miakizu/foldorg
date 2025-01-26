import os
import shutil
import time
from pathlib import Path

# Define the Downloads folder path
DOWNLOADS_PATH = str(Path.home() / "Downloads")

# Define categories and their corresponding file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".ppt", ".pptx", ".txt", ".md"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json", ".xml"],
    "Others": []  # For files that don't fit into any category
}

def create_category_folders():
    """Create folders for each category if they don't already exist."""
    for category in CATEGORIES:
        folder_path = os.path.join(DOWNLOADS_PATH, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def get_file_category(file_extension):
    """Return the category for a given file extension."""
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_downloads():
    """Organize files in the Downloads folder into their respective categories."""
    for filename in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        # Get file extension and category
        file_extension = os.path.splitext(filename)[1]
        category = get_file_category(file_extension)

        # Move the file to the appropriate folder
        destination_folder = os.path.join(DOWNLOADS_PATH, category)
        destination_path = os.path.join(destination_folder, filename)

        if not os.path.exists(destination_path):
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} -> {category}")
        else:
            print(f"Skipped: {filename} (already exists in {category})")

def main():
    print("Auto-Organize Downloads Folder Script")
    print("-------------------------------------")
    create_category_folders()
    organize_downloads()
    print("Organization complete!")

if __name__ == "__main__":
    main()
