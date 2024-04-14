import os
import shutil

source = r"C:\Users\sharm\Downloads"
file_list = os.listdir(source)

for file_name in file_list:
    file_path = os.path.join(source, file_name)
    
    if os.path.isfile(file_path):
        base_name, extension = os.path.splitext(file_name)
        print(f"Extension: {extension}")
        destination_dir = os.path.join(source, extension.strip('.').lower())

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        shutil.move(file_path, os.path.join(destination_dir, file_name)) 
        print(f"Moved {file_name} to {destination_dir}")

    else:
        print(f"{file_name} is not a regular file")
