import os
import shutil


directory = "E:/"

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

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in extensions:
            folder_name = extensions[file_extension]
        else:
            folder_name = "Other"

        # Create folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        #  Move the file
        destination_path = os.path.join(folder_path, filename)
        try:
            shutil.move(filepath, destination_path)
            print(f"Moved {filename} to {folder_name} folder.")
        except Exception as e:
            print(f"Failed to move {filename}: {e}")
