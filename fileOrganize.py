import os
import shutil
path=r"C:\Users\sharm\Downloads"
a=shutil.disk_usage(path)
fileList=os.listdir(path)
for i in fileList:
    base_name, extension = os.path.splitext(i)
    print(f"File Name: {i}, Extension: {extension}")
