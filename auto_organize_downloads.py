#!/usr/bin/env python3
import os
import shutil
import time
import sys
import logging
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Setup logging: only errors will be printed now.
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define file extensions for each category
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.cs', '.rb', '.php']
}

def get_category(file_ext):
    """Return the category for a given file extension."""
    file_ext = file_ext.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    return 'Others'

def print_progress(success_count, fail_count, processed, total):
    """Print three lines updating the progress in place."""
    # ANSI code to clear the line and return carriage
    clear_line = "\033[K"
    # Construct progress lines with color
    success_line = f"{Fore.GREEN}Successful: {success_count}{Style.RESET_ALL}"
    fail_line = f"{Fore.RED}Failed: {fail_count}{Style.RESET_ALL}"
    progress_line = f"Processed: {processed} / {total}"
    
    # Move cursor up three lines (if not the first iteration)
    sys.stdout.write("\033[3F")
    # Overwrite the lines with cleared content and new text
    sys.stdout.write(f"{clear_line}{success_line}\n")
    sys.stdout.write(f"{clear_line}{fail_line}\n")
    sys.stdout.write(f"{clear_line}{progress_line}\n")
    sys.stdout.flush()

def main():
    try:
        print("Welcome to The Digger!")
        source_dir = input("Enter the folder destination to search: ").strip()

        if not os.path.isdir(source_dir):
            logging.error(f"The provided path '{source_dir}' is not a valid directory.")
            input("Press Enter to exit.")
            return

        # Create an output directory named "Organized_Files_TIMESTAMP" in the current directory
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_dir = os.path.join(os.getcwd(), f"Organized_Files_{timestamp}")
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            logging.error(f"Error creating output directory '{output_dir}': {e}")
            input("Press Enter to exit.")
            return

        # Create subdirectories for each category and an "Others" folder
        target_dirs = {}
        for category in list(FILE_CATEGORIES.keys()) + ['Others']:
            target_path = os.path.join(output_dir, category)
            try:
                os.makedirs(target_path, exist_ok=True)
                target_dirs[category] = target_path
            except Exception as e:
                logging.error(f"Error creating folder for {category}: {e}")

        # Walk through the directory and gather all file paths
        print("\nScanning files...")
        all_files = []
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                all_files.append(full_path)
        total_files = len(all_files)
        print(f"Found {total_files} files in total.\n")

        if total_files == 0:
            print("No files found in the specified directory.")
            input("Press Enter to exit.")
            return

        # Initialize counters
        success_count = 0
        fail_count = 0
        processed_count = 0

        # Print initial progress lines (reserve three lines)
        print(f"{Fore.GREEN}Successful: {success_count}{Style.RESET_ALL}")
        print(f"{Fore.RED}Failed: {fail_count}{Style.RESET_ALL}")
        print(f"Processed: {processed_count} / {total_files}")
        
        # Process files and update progress without spamming new lines
        for file_path in all_files:
            try:
                _, ext = os.path.splitext(file_path)
                category = get_category(ext)
                dest_path = os.path.join(target_dirs[category], os.path.basename(file_path))
                shutil.copy2(file_path, dest_path)
                success_count += 1
            except Exception as e:
                fail_count += 1
                logging.error(f"Error copying '{file_path}': {e}")
            processed_count += 1
            print_progress(success_count, fail_count, processed_count, total_files)
        
        print(f"\nFinished! Successfully copied {success_count} files (Failed: {fail_count}) into '{output_dir}'.")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
    finally:
        input("Press Enter to exit.")

if __name__ == '__main__':
    main()
