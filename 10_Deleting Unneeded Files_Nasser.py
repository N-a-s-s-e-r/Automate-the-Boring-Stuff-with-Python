import os

def list_files_scandir(path='.'):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                if os.path.getsize(entry.path) > 104857600:
                    print(entry.path)
            elif entry.is_dir():
                list_files_scandir(entry.path)


# Specify the directory path you want to start from
directory_path = r"C:\Users\ekull\Downloads"
list_files_scandir(directory_path)
