import os
import shutil

# Functions to organize the files to folders.
def audioFiles(file):
    return os.path.splitext(file)[1] in audio

def archiveFiles(file):
    return os.path.splitext(file)[1] in archives

def documentFiles(file):
    return os.path.splitext(file)[1] in documents

def executableFiles(file):
    return os.path.splitext(file)[1] in executables

def imageFiles(file):
    return os.path.splitext(file)[1] in images

def videoFiles(file):
    return os.path.splitext(file)[1] in video


# Extensions
audio = (".mp3", ".wav")
video = (".mp4", ".flv", ".mov")
images = (".jpg", ".jpeg", ".png", ".gif")
documents = (".doc", ".docx", ".pdf", ".txt")
executables = (".exe", ".msi")
archives = (".rar", ".zip")

# Directory of where the files are located for sorting. 
sourceDirectory = "C:/Users/jepla/Downloads"

# Destination directories.
destinationDirs = {
    "audioFiles": "D:/Python Organized Files/Audio Files",
    "archiveFiles": "D:/Python Organized Files/ArchiveFiles",
    "documentFiles": "D:/Python Organized Files/Document Files",
    "executableFiles": "D:/Python Organized Files/Executable Files",
    "imageFiles": "D:/Python Organized Files/Image Files",
    "videoFiles": "D:/Python Organized Files/Video Files"
}

# Create the directory if the folders on exist.
for directory_path in destinationDirs.values():
    os.makedirs(directory_path, exist_ok=True)

# Logic for organizing the files to folders.
print("Start organizing files...")

for file in os.listdir():
    sourcePath = os.path.join(sourceDirectory, file)
    print(f"Processing file: {file}")

    try:
        if archiveFiles(file):
            shutil.move(sourcePath, destinationDirs["archiveFiles"])
        elif audioFiles(file):
            shutil.move(sourcePath, destinationDirs["audioFiles"])
        elif documentFiles(file):
            shutil.move(sourcePath, destinationDirs["documentFiles"])
        elif executableFiles(file):
            shutil.move(sourcePath, destinationDirs["executableFiles"])
        elif imageFiles(file):
            shutil.move(sourcePath, destinationDirs["imageFiles"])
        else:
            shutil.move(sourcePath, destinationDirs["videoFiles"])
        
        print(f"Move {file} successfully.")
    except Exception as e:
        print(f"Error moving {file}: {e}")

print("Finished organizing files.")