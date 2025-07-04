# folderflow/cli.py
import os
import shutil
import argparse
from datetime import datetime

extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
}

def log_action(message, enable_log):
    if enable_log:
        with open("log.txt", "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            log_file.write(f"{timestamp} {message}\n")

def organize_files(directory, enable_log=False):
    if not os.path.exists(directory):
        print("❌ The specified path does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = os.path.splitext(filename)[1].lower()
            folder_name = extensions.get(file_extension, "Other")
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            destination_path = os.path.join(folder_path, filename)
            try:
                shutil.move(filepath, destination_path)
                msg = f"Moved {filename} → {folder_name}/"
                print(msg)
                log_action(msg, enable_log)
            except Exception as e:
                error_msg = f"❌ Failed to move {filename}: {e}"
                print(error_msg)
                log_action(error_msg, enable_log)

def main():
    parser = argparse.ArgumentParser(description="📂 FolderFlow - Auto File Organizer")

    parser.add_argument(
        "--path", type=str, required=True,
        help="Path to the folder to organize (e.g. E:/Downloads)"
    )
    parser.add_argument(
        "--log", type=str, default="false",
        help="Enable logging (true/false)"
    )

    args = parser.parse_args()
    log_enabled = args.log.lower() == "true"

    organize_files(args.path, log_enabled)
