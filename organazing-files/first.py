 
import shutil, os, send2trash

# Moving file. Destination folder must already exist.
try:
    shutil.move('./from/testfile', './to/testfile-new')
except FileNotFoundError:
    print('File not found')

# Copy all files from src to dst. Destination folder must not exist. It will be created.If it already exist then there will be exception
try:
    shutil.copytree('./from', './to2')
except FileExistsError:
    print('Folder exist')

# Renaming. Destination folder must already exist.
try:
    shutil.move('./from/testfile-new', './to3/testfile-new')
except FileNotFoundError:
    print('There are no testfile-new in from folder')

try:
    os.unlink('./to/testfile-new')
except FileNotFoundError:
    print('here are no testfile-new in to folder')
    
    
# Deleting directory. Must be empty
#os.rmdir('./to2')
# Deleting directory and everything in it
#os.rmtree('./to2')

send2trash.send2trash('./from/test2')
