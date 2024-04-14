import os
import shutil
path=r"C:\Users\sharm\Downloads\Python 3 Deep Dive (Part 1 - Functional)\[TutsNode.org] - Python 3 Deep Dive (Part 1 - Functional)\10 - Python Updates"
a=shutil.disk_usage(path)
fileList=os.listdir(path)
print(fileList)