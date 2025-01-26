import os
import shutil
import argparse
from pathlib import Path

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

def create_category_folders(folder_path):
    """Create folders for each category if they don't already exist."""
    for category in CATEGORIES:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def get_file_category(file_extension):
    """Return the category for a given file extension."""
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    """Organize files in the specified folder into their respective categories."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        # Get file extension and category
        file_extension = os.path.splitext(filename)[1]
        category = get_file_category(file_extension)

        # Move the file to the appropriate folder
        destination_folder = os.path.join(folder_path, category)
        destination_path = os.path.join(destination_folder, filename)

        if not os.path.exists(destination_path):
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} -> {category}")
        else:
            print(f"Skipped: {filename} (already exists in {category})")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Organize files in a folder into subfolders based on file type.")
    parser.add_argument(
        "folder",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Path to the folder you want to organize (default: Downloads folder)"
    )
    args = parser.parse_args()

    # Validate folder path
    if not os.path.exists(args.folder):
        print(f"Error: The folder '{args.folder}' does not exist.")
        return

    print(f"Auto-Organize Folder: {args.folder}")
    print("-------------------------------------")
    create_category_folders(args.folder)
    organize_folder(args.folder)
    print("Organization complete!")

if __name__ == "__main__":
    main()
