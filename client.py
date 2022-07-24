import os 
from pathlib import Path

listOfDirectories = {
    "Picture_Folder": [".jpeg", ".jpg",".gif", ".png"],
    "Video_Folder":[".wmv", ".mov", ".mp4", ".mpg",".mpeg",".mkv"],
    "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".zip"],
    "Music_Folder":[".mp3", ".msv", ".wav", ".wma"],
    "PDF_Folder":[".pdf"],
    "Word_Doc":[".doc", ".docm", ".docx"] 
}

File_Format_Dictionary = {
    final_file_format: directory 
    for directory, file_format_stored in listOfDirectories.items() # For each directory in the dictionary
        for final_file_format in file_format_stored # For each file format in the list of file formats for that directory
}

def organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        
        file_path = Path(entry) # Create a path object from the file name (ex. "test.txt")
        final_file_format = file_path.suffix.lower() # Get the file format (ex. .jpg)
        
        if final_file_format in File_Format_Dictionary: # If the file format is in the dictionary (File_Format_Dictionary)
            directory_path = Path(File_Format_Dictionary[final_file_format]) # Get the directory path from the dictionary (ex. "Pictures")
            os.makedirs(directory_path, exist_ok=True) # Create the directory if it doesn't exist (ex. "Pictures")
            os.rename(file_path, directory_path.joinpath(file_path)) # Move the file to the directory (ex. "test.txt" -> "Pictures/test.txt")
        else:
            # create a folder named "Other_Folder" if it doesn't exist
            other_folder = Path("Other_Folder")
            os.makedirs(other_folder, exist_ok=True)
            # move the file to the "Other_Folder" folder
            os.rename(file_path, 
            os.getcwd() + '/Other_Folder/' + str(file_path)) 
        
if __name__ =="__main__": 
    organizer()